import base64
import json

import tweepy

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after

f = open('config.json', 'r')
config = json.load(f)

# Keys secured.
# consumer_key = config['consumer_key']
# consumer_secret = config['consumer_secret']
consumer_key = base64.b64decode(config['consumer_key1']).decode("utf-8")
consumer_secret = base64.b64decode(config['consumer_secret1']).decode("utf-8")

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
# access_token = config['access_token']
# access_token_secret = config['access_token_secret']
access_token = base64.b64decode(config['access_token1']).decode("utf-8")
access_token_secret = base64.b64decode(config['access_token_secret1']).decode("utf-8")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Open/Create a file to append data
csvFile = open('Writetweetsdata.csv', 'a')
api = tweepy.API(auth)
public_tweets = api.home_timeline()


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            self.form_string(status)

        except BaseException as e:
            print('problem collecting tweet', str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

    def form_string(self, status):
        author = self.clean_string(status.author.name)
        author_location = self.clean_string(status.author.location)
        about_author = self.clean_string(status.author.description)
        created_at = status.created_at
        source = self.clean_string(status.source)
        tweet_message = self.clean_string(status.text)
        final = author + "," + author_location + "," + about_author + "," + str(
            created_at) + "," + source + "," + tweet_message
        print(final)
        if final:
            csvFile.write(final + "\n")

    def clean_string(self, input):
        if input is not None:
            return_string = input.encode("ascii", errors="ignore").decode().replace('\n', '')
            return_string = return_string.strip().replace('["]', '')
            return_string = return_string.replace(',', '')
            return return_string
        else:
            return ""


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(languages=["en"], track=['political', 'impeachment', 'trump'])
csvFile.close()
