import json

from flask_restful import Resource, reqparse, abort

import os
import config
import pandas as pd


class DataSet(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('name', type=str, required=True)
        self.parser.add_argument('data', type=dict, required=True, action='append')

    def post(self):
        data = self.parser.parse_args()
        data_df = pd.DataFrame(data['data'])
        try:
            data_df.to_csv(os.path.join(config.DATA_PATH, data['name']), encoding='utf-8', index=False, mode='w')
        except RuntimeError:
            abort(403)
        return {"message": "success"}

    def get(self):
        data = self.parser.parse_args()
        data_path = os.path.join(config.DATA_PATH, data['name'])
        data_df = pd.DataFrame()
        try:
            data_df = pd.read_csv(data_path)
        except FileNotFoundError:
            abort(403)
        return data_df

    def delete(self):
        data = self.parser.parse_args()
        data_path = os.path.join(config.DATA_PATH, data['name'])
        data_df = pd.DataFrame()
        try:
            data_df = pd.read_csv(data_path)
        except FileNotFoundError:
            abort(403)
        return data_df

    def put(self):
        data = self.parser.parse_args()
        data_path = os.path.join(config.DATA_PATH, data['name'])
        data_df = pd.DataFrame()
        try:
            data_df = pd.read_csv(data_path)
        except FileNotFoundError:
            abort(403)
        return {"message": "success"}
