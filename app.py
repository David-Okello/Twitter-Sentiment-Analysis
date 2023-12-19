# Import all necessary modules & packages
import os
import tweepy
from dotenv import load_dotenv
from flair.models import TextClassifier
from flair.data import Sentence

# Load environment variables
load_dotenv()

# Load Twitter API credentials from environment variables
api_key = os.getenv("API_Key")
api_secret = os.getenv("API_Key_Secret")
bearer_token = os.getenv("Bearer_Token")
access_token = os.getenv("Access_Token")
access_token_secret = os.getenv("Access_Token_Secret")

'''
# Uncomment to use twitter API v2 to get tweets the handle the pre processing steps
# otherwise use a python list with hard coded tweets if you haven't paid for the twitter developer account

# Authenticate with the Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Test API connection by posting a tweet
#client.create_tweet(text="Testing my Connection")

# Get realtime tweets from twitter
response = client.search_all_tweets('#crypto')
#response = client.search_recent_tweets('#crypto')

tweets = response.data

for tweet in tweets:
    print(tweet.text)
    print("----------")
'''

tweets = [
    "I love spending time with my family!",
    "The weather is fantastic today!",
    "Just got a promotion at work, feeling on top of the world!",
    "Enjoying a delicious meal with great company.",
    "This book is incredibly inspiring and uplifting.",
    "The traffic is moving at a normal pace.",
    "I have a meeting at 2 PM.",
    "Today is an average day.",
    "Just finished my daily routine.",
    "Neutral statement about current events.",
    "Feeling under the weather today.",
    "Stuck in traffic for hours. This day can't get any worse.",
    "Received some bad news. Trying to stay positive.",
    "Disappointed with the service at the restaurant.",
    "This movie was a complete waste of time."
]

# Sentiment Analysis
classifier = TextClassifier.load('en-sentiment')
def get_tweet_sentiment(tweet):
    sentence = Sentence(tweet)
    classifier.predict(sentence)
    return str(sentence.labels[0].value)

for tweet in tweets:
    print(get_tweet_sentiment(tweet))