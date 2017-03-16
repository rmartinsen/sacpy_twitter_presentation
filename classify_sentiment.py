
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def classify_sentiment(tweet_text):
    sentiment = sia.polarity_scores(tweet_text)

    return sentiment["compound"]
