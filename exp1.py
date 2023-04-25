import requests
video_id="b1kbLwvqugk"
api_key="AIzaSyCY-q1PsTSWj2VLC3XAvZNBTf6rRqZcUaw"
print("Retrieve video information")
video_info_url=f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
video_info_response=requests.get(video_info_url)
video_info_data=video_info_response.json()
video_info_data


print("Retrieve video Comments")
comment_url=f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
comments_response=requests.get(comment_url)
comments_data=comments_response.json()
comments_data


comments=[item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]for item in
comments_data["items"]]
comments
