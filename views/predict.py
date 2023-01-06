from flask_restful import Resource, reqparse, abort

from inference_service import InferenceService


class Predict(Resource):
    def __init__(self):
        self.inference = InferenceService.INSTANCE
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def post(self):
        self.parser.add_argument('data', type=dict, required=True)
        self.parser.add_argument('model', type=str)
        data = self.parser.parse_args()

        if data['model'] is None and self.inference is None:
            abort(403, message="尚未训练模型")
        if data['model'] is not None:
            self.inference = InferenceService().INSTANCE
            self.inference.load_model_from_file(data['model'])
            print(data['model'])

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
