from app.scrapers.youtube import get_channel_videos
from app.database.connection import SessionLocal
from app.database.repository import Repository


CHANNELS_ID = [
    {
        "name": "AI Explained",
        "channel_id": "UCYO_jab_esuFRV4b17AJtAw",
        "url": "https://youtube.com/@AIExplained"
    },
    {
        "name": "Fireship",
        "channel_id": "UCsBjURrPoezykLs9EqgamOA",
        "url": "https://youtube.com/@Fireship"
    },
    {
        "name": "Matt Wolfe",
        "channel_id": "UCiT9RITQ9PW6BhXK0y2jaeg",
        "url": "https://youtube.com/@mreflow"
    },
    {
        "name": "Two Minute Papers",
        "channel_id": "UCbfYPyITQ-7l4upoX8nvctg",
        "url": "https://youtube.com/@TwoMinutePapers"
    }
]


def process_youtube():

    db = SessionLocal()
    repo = Repository(db)

    for channel in CHANNELS_ID:

        source = repo.create_source(
            name=channel["name"],
            url=channel["url"],
            source_type="youtube"
        )

        videos = get_channel_videos(
            channel["channel_id"]
        )

        for video in videos:
            repo.create_article(
                source_id=source.id,
                title=video["title"],
                content="",
                url=video["url"]
            )

        print(f"Inserted {len(videos)} videos")

    db.close()