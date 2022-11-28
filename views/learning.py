from flask_restful import Resource, reqparse, abort
from inference_service import InferenceService


class ModelView(Resource):
    def __init__(self):
        self.inference = InferenceService().INSTANCE
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def post(self, model_name):
        # 主要参数
        self.parser.add_argument('dataset', required=True)
        self.parser.add_argument('parameter', required=True)
        data = self.parser.parse_args()
        # 向接口传训练参数
        detail = dict()
        try:
            self.inference.solve_dataset(data['dataset'])
            detail = self.inference.train_model(model_name, data['parameter'])
        except FileNotFoundError:
            abort(400, message="数据集不存在")
        except ModuleNotFoundError:
            abort(404, message="模型名称错误")
        return {'data': detail}

    def get(self, model_name):
        abort(403)
        # if model_name not in config.models:
        #     abort(404, message="模型名称错误")
        #
        # self.parser.add_argument('data', type=dict, required=True)
        # data = self.parser.parse_args()
        # return self.inference.get_prediction(data)

        # return {'data': self.inference.get_result()}
