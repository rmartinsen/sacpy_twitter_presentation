import pymysql
import json

from tweet_settings import password, user

connection = pymysql.connect(host="localhost",
							 user=user,
							 password=password,
							 db="twitter_dev",
							 charset="utf8mb4"
							 )

def save_tweet_to_db(tweet):
	tweet_dict = json.loads(tweet)

	if "text" in tweet_dict.keys():
		tweet_user = tweet_dict["user"]["screen_name"].encode("utf-8")
		tweet_text = tweet_dict["text"].encode("utf-8")

		sql = "insert into tweets(user, tweet_text) values(%s, %s)"

		with connection.cursor() as cursor:
			cursor.execute(sql, [tweet_user	, tweet_text])
			connection.commit()


















