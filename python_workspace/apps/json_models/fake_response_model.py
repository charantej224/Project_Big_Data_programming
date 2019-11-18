import json

from flask import jsonify


class FakeDetectionModel(object):
    def __init__(self, fake_news):
        self.fake_news = fake_news

    def to_json_message(self):
        return jsonify({
            "prediction": self.fake_news
        })

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
