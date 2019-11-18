import threading

from flask import Flask, request

from apps.sentiment_analysis.stream_twitter import TwitterStreamer
from apps.json_models.sentiment_model import SentimentModel
from apps.sentiment_analysis.sentiment_analysis import SentimentAnalysis
from apps.fakenews_analysis.fake_news_detection import FakeNewDetector

from apps.model_handlers.handle_models import ModelTriggers

app = Flask(__name__)

sentiment_analysis = SentimentAnalysis()
fake_news_detector = FakeNewDetector()

@app.route('/')
def twitter_analysis():
    return '<html><b>Twitter Streaming App<b></html>'


@app.route('/sentiment-analyse', methods=['POST'])
def sentiment_of_message():
    message = request.get_json()
    val = sentiment_analysis.predict_outcome(str(message['message']))
    sentiment_model = SentimentModel(val[0])
    return sentiment_model.to_json_message()


def start_stream(val, file_name):
    TwitterStreamer(val, file_name, sentiment_analysis)


@app.route('/sentiment-analyse-stream', methods=['POST'])
def stream_twitter_message():
    message = request.get_json()
    val = int(str(message['time']))
    file_name = message['writeFile']
    thread = threading.Thread(target=start_stream, args=(val, file_name,))
    thread.start()
    return 'Streaming Request Processed'


def init_app():
    model_triggers = ModelTriggers(sentiment_analysis, fake_news_detector)
    model_triggers.setup_models()


if __name__ == "__main__":
    init_app()
    app.run()
