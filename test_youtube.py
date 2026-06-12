from app.scrapers.youtube import get_channel_videos

videos = get_channel_videos(
    "UCYO_jab_esuFRV4b17AJtAw"
)

print(f"Found {len(videos)} videos\n")

for video in videos[:5]:
    print(video["title"])
    print(video["url"])
    print(video["published"])
    print("-" * 50)