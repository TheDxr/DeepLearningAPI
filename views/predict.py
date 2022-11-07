from flask_restful import Resource, reqparse, abort
from flask import jsonify
from inference_service import InferenceService

from inference_service import InferenceService
import config


class Predict(Resource):
    def __init__(self):
        self.inference = InferenceService.INSTANCE
        if self.inference is None:
            abort(403, message="尚未训练模型")
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def post(self):
        self.parser.add_argument('data', required=True)
        data = self.parser.parse_args()
        data['prediction'] = self.inference.get_prediction(data)
        return jsonify(data)

    def get(self):
        self.parser.add_argument('data', type=dict, required=True)
        data = self.parser.parse_args()
        return jsonify(self.inference.get_prediction(data))
