from apps.sentiment_analysis.sentiment_analysis import SentimentAnalysis
import numpy as np


def init_app():
    sentiment_analysis = SentimentAnalysis()
    sentiment_analysis.prepare_model()
    return_val = sentiment_analysis.predict_outcome('I feel you are very good president, here to help people')
    print(return_val)


if __name__ == "__main__":
    init_app()
