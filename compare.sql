select 'Cat', avg(sentiment) from twitter_dev.tweets where lower(tweet_text) like '%cat%' UNION
select 'Dog', avg(sentiment) from twitter_dev.tweets where lower(tweet_text) like '%dog%'