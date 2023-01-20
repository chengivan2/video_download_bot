import tweepy
import requests

# Authenticate with Twitter API
# Replace with your own API keys
consumer_key = 'CxKhgA6o7EwhfN3N08u2ssg5a'#API Key
consumer_secret = 'H7DmPNGwCK51TCFmuiWzggmFQg5E6WcbRtZTF4fDEuJ6ONVopa'#API Key Secret
access_token = '1484916856905420806-wzQGr3Cvhook5KTANvPjQR9YC9A7St'
access_token_secret = 'MqoeXgFAeLuaYSec6TSwSDXqd26aAxqK36ArmXRFkdhCD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Search for tweets mentioning the bot
def download_video(status):
    tweet_id = status.id
    try:
        # Get the video URL from the tweet
        video_url = status.extended_entities['media'][0]['video_info']['variants'][0]['url']
    except:
        return
    # Download the video
    video = requests.get(video_url)
    # Save the video to a file
    with open("video.mp4", "wb") as f:
        f.write(video.content)
    print("Video downloaded successfully")
    # Reply to the tweet with the video
    media = api.media_upload("video.mp4")
    api.update_status(status='@'+status.user.screen_name+' here you go!', in_reply_to_status_id=tweet_id,)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if '@yourbotname' in status.text:
            download_video(status)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@yourbotname'])
