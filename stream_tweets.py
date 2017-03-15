import tweepy
from tweepy.streaming import StreamListener

from db import save_tweet_to_db

from tweet_settings import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET


keywords = ["cat", "dog"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


class TweetListener(StreamListener):
	
	def on_data(self, data):
		save_tweet_to_db(data)

	def on_error(self, status):
		print("Error code " + str(status))


twitter_stream = tweepy.Stream(auth, TweetListener())
twitter_stream.filter(track=keywords)


