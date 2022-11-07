from flask_restful import Resource, reqparse
from flask import jsonify
from inference_service import InferenceService


import config


class MLView(Resource):
    def __init__(self):
        self.inference = InferenceService()
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def post(self):
        # 主要参数
        self.parser.add_argument('model', choices=[el.value for el in config.Models], required=True)
        self.parser.add_argument('dataset', required=True)
        self.parser.add_argument('parameter', required=True)
        data = self.parser.parse_args()
        # 向接口传训练参数
        self.inference.solve_dataset(data['dataset'])
        status, detail = self.inference.train_model(data['model'], data['parameter'])
        if status == 'success':
            data['data'] = detail
        else:
            data['data'] = status
        return jsonify(data)

    def get(self):
        data = {'data': self.inference.get_result()}
        return jsonify(data)





