import config
import torch_utils
import os
import difflib

from models import *


class InferenceService:
    INSTANCE = None

    def __init__(self):
        self.__model = None
        self.__result = None
        self.__model_name = str()
        self.__dataset_path = str()

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
        # 判断模型名称
        if model_name in models_list:
            self.__model = eval(models_class_dict[model_name])()
        else:
            raise ModuleNotFoundError('ModuleNotFoundError')
        self.__model_name = model_name
        # 获取数据集
        dataset = torch_utils.get_dataset_from_file(self.__dataset_path)
        # 训练模型
        try:
            self.__model.load_data(dataset)
            result = self.__model.fit(parameter)
            self.__result = result
        except RuntimeError:
            raise RuntimeError('fit error')
        except FileNotFoundError:
            raise FileNotFoundError('dataset error')
        return self.__result

    def get_result(self):
        """
        :return: 训练结果(dict)
        """
        return self.__result

    def get_prediction(self, data):
        return self.__model.get_prediction(data)

    def solve_dataset(self, dataset_path: str):
        try:
            file_list = os.listdir(config.DATA_PATH)
            closest: list = difflib.get_close_matches(dataset_path, file_list, n=1)
            self.__dataset_path = closest[0]
        except IndexError as e:
            raise FileNotFoundError('dataset error')

    def get_model_name(self):
        return self.__model_name



