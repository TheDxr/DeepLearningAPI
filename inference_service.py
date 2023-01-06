import config
import dataset_utils
import os
import difflib
import pickle

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
        dataset = dataset_utils.get_dataset_from_file()
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
        """
        利用当前模型做预测
        :param data: 预测数据
        :return: 预测结果
        """

        return self.__model.get_prediction(data)

    def save_current_model(self, path='./saves/test.model'):
        """
        保存当前模型
        :param path:
        :return:
        """
        with open(path, "wb") as f:
            pickle.dump(self.__model, f)

    def load_model_from_file(self, path):
        with open(path, "rb") as f:
            self.__model = pickle.load(f)

    def get_prediction_from_saved_model(self, data, path='D:/SourceCode/PythonCode/DeepLearningAPI/saves/test.model'):
        """
        利用已保存模型做预测
        :param data: 预测数据
        :param path: 已训练模型的路径
        :return: 预测结果
        """
        with open(path, "rb") as f:
            self.__model = pickle.load(f)
        return self.__model.get_prediction(data)

    def get_model_name(self):
        """
        获取当前模型名称
        :return: 模型名称(str)
        """
        return self.__model_name
