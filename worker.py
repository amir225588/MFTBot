from workers import WorkerEntrypoint, Response


BOT_NAME = "مجتمع فنی تهران - مرکزی (سعادت آباد)"
PHONE = "0212729"
SITE = "https://mftplus.com"


WELCOME = f"""
👋 به ربات رسمی {BOT_NAME} خوش آمدید.

از طریق این ربات می‌توانید:

📚 آشنایی با دپارتمان‌ها
🎓 مشاهده دوره‌ها
☎️ دریافت مشاوره
🌐 ورود به سایت

یکی از گزینه‌ها را انتخاب کنید.
"""


DEPARTMENTS = {
    "💻 فناوری اطلاعات و ارتباطات": """
با طی دوره‌های تخصصی و مهارتی در مرکز آموزش‌های ICT مجتمع فنی تهران با دنیای IT همگام باشید.

نمونه دوره‌ها:

• ICDL
• Python
• Java
• C#
• طراحی سایت
• React
• شبکه
• امنیت
• لینوکس
• DevOps
• هوش مصنوعی
""",

    "⚙ علوم مهندسی": """
پیشرو در اجرای آموزش‌های تخصصی فنی و مهندسی

نمونه دوره‌ها:

• AutoCAD
• SolidWorks
• CATIA
• MATLAB
• Abaqus
• ANSYS
""",

    "⚡ برق و الکترونیک": """
پیشگام در آموزش برق و الکترونیک

نمونه دوره‌ها:

• PLC
• اتوماسیون صنعتی
• برق ساختمان
• برق صنعتی
• ابزار دقیق
""",

    "👦 کودک و نوجوان": """
آموزش مهارت‌های کاربردی برای کودکان و نوجوانان

• رباتیک
• برنامه‌نویسی
• زبان
• خلاقیت
""",

    "🌍 زبانهای خارجی": """
برگزاری دوره‌های زبان

• انگلیسی
• آلمانی
• فرانسه
• ترکی
• ایتالیایی
""",

    "🩺 دانش سلامت": """
دوره‌های سلامت و زیبایی

• مراقبت پوست
• ماساژ
• تغذیه
""",

    "🏛 معماری": """
دوره‌های معماری

• AutoCAD
• Revit
• 3Ds Max
• Lumion
""",

    "👗 فناوری مد و پوشاک": """
دوره‌های طراحی لباس

• طراحی لباس
• الگوسازی
• دوخت
""",

    "🎨 هنر، سینما و تولید محتوا": """
دوره‌های هنری

• Photoshop
• Illustrator
• Premiere
• After Effects
• موشن گرافیک
""",

    "🌎 مرکز همکاری های بین الملل": """
اعطای مدارک بین المللی

• ترجمه رسمی مدارک
• گواهینامه‌های بین‌المللی
""",

    "✈ تشریفات و گردشگری": """
دوره‌های

• کافی شاپ
• آشپزی
• هتلداری
• گردشگری
""",

    "💰 علوم مالی و حسابداری": """
دوره‌های

• حسابداری
• بورس
• ارز دیجیتال
• سرمایه گذاری
""",

    "🚢 صنایع دریایی": """
دوره‌های

• غواصی صنعتی
• امور دریایی
""",

    "📈 مدیریت و کسب و کار": """
دوره‌های

• MBA
• DBA
• مدیریت فروش
• منابع انسانی
""",

    "⚖ حقوق": """
آموزش قوانین و مقررات

• حقوق خصوصی
• حقوق کیفری
• حقوق تجارت
"""
}


class Default(WorkerEntrypoint):

    async def fetch(self, request):

        # صفحه اصلی
        if request.method == "GET":
            return Response("MFT Bot is Running.")

        # فقط POST برای وبهوک
        if request.method == "POST":

            try:
                data = await request.json()
            except Exception:
                data = {}

            text = data.get("body", "")

            if text == "/start":
                return Response.json({
                    "type": "text",
                    "body": WELCOME
                })

            if text == "دپارتمان ها":
                return Response.json({
                    "type": "text",
                    "body": "\n".join(DEPARTMENTS.keys())
                })

            if text in DEPARTMENTS:
                return Response.json({
                    "type": "text",
                    "body": DEPARTMENTS[text]
                })

            if text == "تماس":
                return Response.json({
                    "type": "text",
                    "body": f"☎️ {PHONE}\n🌐 {SITE}"
                })

            return Response.json({
                "type": "text",
                "body": "لطفا از منو استفاده کنید."
            })

        return Response("Method Not Allowed", status=405)
