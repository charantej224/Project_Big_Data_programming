from apps.sentiment_analysis.sentiment_analysis import SentimentAnalysis
from flask import Flask, request
from apps.models.predict_model import PredictModel
from apps.models.sentiment_model import SentimentModel
from apps.data_extraction.stream_twitter import TwitterStreamer
import numpy as np

app = Flask(__name__)

sentiment_analysis = SentimentAnalysis()


@app.route('/')
def twitter_analysis():
    return '<html><b>Twitter Streaming App<b></html>'


@app.route('/sentiment-analyse', methods=['POST'])
def sentiment_of_message():
    message = request.get_json()
    val = sentiment_analysis.predict_outcome(str(message['message']))
    sentiment_model = SentimentModel(val[0])
    return sentiment_model.to_json_message()


@app.route('/sentiment-analyse-stream', methods=['POST'])
def stream_twitter_message():
    message = request.get_json()
    val = int(str(message['time']))
    stream = TwitterStreamer(val, sentiment_analysis)
    return '<html><b>Twitter Streaming App<b></html>'


def init_app():
    sentiment_analysis.prepare_model()


if __name__ == "__main__":
    init_app()
    app.run()
