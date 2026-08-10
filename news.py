if text == "📰 اخبار مجتمع فنی تهران":

    return Response.json({
        "type": "link",
        "body": "مشاهده آخرین اخبار مجتمع فنی تهران",
        "url": "https://mftplus.com/news"
    })
