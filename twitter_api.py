import tweepy
import csv
import unicodedata

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
csvFile = open('nausea.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id', 'Time','Tweet'])
for tweet in tweepy.Cursor(api.search_tweets, q = "nausea", count = "2000", lang = "en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.user.id, tweet.created_at, unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')])
    print(tweet.user.id, tweet.created_at, tweet.text)
csvFile.close()