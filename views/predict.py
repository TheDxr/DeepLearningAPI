from flask_restful import Resource, reqparse, abort

from inference_service import InferenceService


class Predict(Resource):
    def __init__(self):
        self.inference = InferenceService.INSTANCE
        if self.inference is None:
            abort(403, message="尚未训练模型")
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def post(self):
        self.parser.add_argument('data', type=dict, required=True)
        data = self.parser.parse_args()
        ret = dict()
        ret['model'] = self.inference.get_model_name()
        try:
            ret['prediction'] = self.inference.get_prediction(data)
        except Exception:
            abort(403, message='参数错误')
        return ret

    def get(self):
        ret = dict()
        ret['model'] = self.inference.get_model_name()
        return ret
