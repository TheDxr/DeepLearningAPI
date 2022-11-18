import config

from flask_restful import Resource, reqparse, abort
from inference_service import InferenceService


class ModelView(Resource):
    def __init__(self):
        self.inference = InferenceService()
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def post(self, model_name):
        # 主要参数
        if model_name not in config.models:
            abort(404, message="模型名称错误")

        self.parser.add_argument('dataset', required=True)
        self.parser.add_argument('parameter', required=True)
        data = self.parser.parse_args()
        # 向接口传训练参数
        self.inference.solve_dataset(data['dataset'])
        try:
            status, detail = self.inference.train_model(model_name, data['parameter'])
        except FileNotFoundError:
            abort(400, message="数据集不存在")
        if status == 'success':
            return {'data': detail}
        else:
            return {'data': status}

    def get(self, model_name):
        if model_name not in config.models:
            abort(404, message="模型名称错误")
        return {'data': self.inference.get_result()}
