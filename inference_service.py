from models import *
from models.model import Model
from flask_restful import abort
import config
import torch_utils
import os
import difflib


class InferenceService:
    __model: Model
    __result: dict
    __dataset_path: str
    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否已经被赋值
        if cls.INSTANCE is None:
            cls.INSTANCE = super().__new__(cls)
        # 返回类属性的单例引用
        return cls.INSTANCE


    def train_model(self, model_name, parameter: dict):
        """
        :return: 训练情况(string),训练结果(dict)
        """
        if model_name == config.Models.XGBoost.value:
            self.__model = XGBoost()
        if model_name == config.Models.DeepFM.value:
            # TODO
            pass
        # 获取数据集
        dataset = torch_utils.get_dataset_from_file(self.__dataset_path)
        # 训练模型
        try:
            self.__model.load_data(dataset)  # TODO
            result = self.__model.fit(parameter)
        except RuntimeError:
            return 'fit error', None
        self.__result = result
        return 'success', result


    def get_result(self):
        """
        :return: 训练结果(dict)
        """
        return self.__result


    def get_prediction(self, data):
        return self.__model.get_prediction(data)


    def solve_dataset(self, dataset_path: str):
        try:
            file_list = os.listdir(config.dataPath)
            closest: list = difflib.get_close_matches(dataset_path, file_list, n=1)
            self.__dataset_path = closest[0]
        except IndexError as e:
            abort(404, message='该数据集不存在')



