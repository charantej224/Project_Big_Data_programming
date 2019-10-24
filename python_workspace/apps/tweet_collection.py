import csv  # Import csv
import json
import tweepy  # Import tweepy

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after

f = open('config.json', 'r')
config = json.load(f)

consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section

access_token = config['access_token']
access_token_secret = config['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Open/Create a file to append data
csvFile = open('Writetweetsdata.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)

api = tweepy.API(auth)

public_tweets = api.home_timeline()


# for tweet in public_tweets:
#   print(tweet.text)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            csvWriter.writerow([status.created_at, status.entities, status.text.encode('utf-8')])
            # csvWriter.writerow([status._json])
            print(status._json)

        except BaseException as e:
            print('problem collecting tweet', str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(languages=["en"], track=['political', 'gossip', 'impeachment', 'trump'])

csvFile.close()
