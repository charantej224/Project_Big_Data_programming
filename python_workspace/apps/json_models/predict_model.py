import json
from flask import jsonify


class PredictModel(object):
    def __init__(self, positive, negative, neutral):
        self.positive = positive
        self.negative = negative
        self.neutral = neutral

    def to_json_message(self):
        return jsonify({
            "positive": "{:.8f}".format(float(self.positive)),
            "negative": "{:.8f}".format(float(self.negative)),
            "neutral": "{:.8f}".format(float(self.neutral))
        })

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
