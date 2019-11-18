import threading


class ModelTriggers:

    def __init__(self, sentiment_model, fake_news_model):
        self.sentiment_model = sentiment_model
        self.fake_news_model = fake_news_model

    def setup_models(self):
        self.trigger_fake_news_model()
        self.trigger_sentiment_model()

    def trigger_sentiment_model(self):
        self.sentiment_model.prepare_model()

    def trigger_fake_news_model(self):
        self.fake_news_model.prepare_model()
