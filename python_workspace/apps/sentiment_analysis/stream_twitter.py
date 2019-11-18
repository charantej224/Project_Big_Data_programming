import base64
import json
from datetime import datetime
from datetime import timedelta
import tweepy
from apps.reports.write_report import WriteReport
import threading


class TwitterStreamer(tweepy.StreamListener):

    def __init__(self, time_limit, file_name, sentiment, fake_news_detector):
        self.file_name = file_name
        self.start_time = datetime.now()
        self.delta_time = timedelta(minutes=time_limit)
        self.end_time = self.start_time + self.delta_time
        super(TwitterStreamer, self).__init__()
        self.tweet_list = []
        self.sentiment = sentiment
        self.fake_news_detector = fake_news_detector
        self.setup_stream()

    def setup_stream(self):
        f = open('config.json', 'r')
        config = json.load(f)

        # Keys secured.
        consumer_key = base64.b64decode(config['consumer_key1']).decode("utf-8")
        consumer_secret = base64.b64decode(config['consumer_secret1']).decode("utf-8")

        # After the step above, you will be redirected to your app's page.
        # Create an access token under the the "Your access token" section
        access_token = base64.b64decode(config['access_token1']).decode("utf-8")
        access_token_secret = base64.b64decode(config['access_token_secret1']).decode("utf-8")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Open/Create a file to append data
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()
        myStream = tweepy.Stream(auth=api.auth, listener=self)
        myStream.filter(languages=["en"], track=['political', 'impeachment', 'trump'])

    def on_status(self, status):
        try:
            self.tweet_list.append(status.text)
            # print(status.text + "\n")
            if datetime.now() > self.end_time:
                sentiment_predicted = self.sentiment.predict_outcome_list(self.tweet_list)
                fake_news_predicted = self.fake_news_detector.predict_outcome_list(self.tweet_list)
                WriteReport(self.tweet_list, sentiment_predicted, fake_news_predicted).write_file(self.file_name)
                return False
        except BaseException as e:
            print('problem collecting tweet', str(e))

        return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
