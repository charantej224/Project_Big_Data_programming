import json
from flask import jsonify


class SentimentModel(object):
    def __init__(self, class_value):
        self.class_value = class_value
        self.sentiment = None

    def to_json_message(self):
        if self.class_value == 0:
            self.sentiment = "Negative"
        elif self.class_value == 1:
            self.sentiment = "Neutral"
        else:
            self.sentiment = "Positive"

        return jsonify({
            "sentiment": self.sentiment
        })

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
