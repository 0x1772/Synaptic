from youtubesearchpython import VideosSearch
import sys

query = sys.argv[1]

videosSearch = VideosSearch(query, limit=1)
video_result = videosSearch.result()
video_id = video_result["result"][0]["id"]
video_url = f"https://www.youtube.com/watch?v={video_id}"
print(video_url)