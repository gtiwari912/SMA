# To scrap the comments from YouTube and perform sentiment analysis.
api_key = "AIzaSyC6ZHngVmQRc6VdyF4cY0F-wL68X2uzZvk"
video_id = "1d3hvhgNFsA"
import requests
video_id = "2CRilTPouRU"
api_key = "AIzaSyC6ZHngVmQRc6VdyF4cY0F-wL68X2uzZvk"



# Retrieve video information
video_info_url =(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}")
video_info_response = requests.get(video_info_url)
video_info_data = video_info_response.json()
video_info_data



# Retrieve video compnts
comments_url =f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
comments_response= requests.get(comments_url)
comments_data = comments_response.json()
comments_data


# Extract the carnents
comments = [item["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for item in comments_data["items"]]
print(comments)


from textblob import TextBlob
def get_comment_sentiment(comment):
  analysis = TextBlob(comment)
  if analysis.sentiment.polarity > 0:
    return "Positive"
  elif analysis.sentiment.polarity == 0:
    return "neutral"
  else:
    return "negative"
comment_list = []
sentiment_list = []
for comment in comments:
  sentiment = get_comment_sentiment(comment)
  comment_list.append(comment)
  sentiment_list.append(sentiment)
  print(f"{comment} : {sentiment}")
  
  
  
import pandas as pd
sentiment_df = pd.DataFrame({"Comments": comment_list,"Sentiment":
sentiment_list})
sentiment_df.head()
sentiment_df.to_csv("YouTube_Comments_Sentiment.csv")
