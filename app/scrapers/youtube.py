import feedparser

def get_channel_videos(channel_id):

    feed = feedparser.parse(
        f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    )

    videos = []

    for entry in feed.entries:
        videos.append({
            "title": entry.title,
            "url": entry.link,
            "published": entry.published
        })

    return videos