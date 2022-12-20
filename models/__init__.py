from enum import Enum
from .xgboost import XGBoost
from .k_means import Kmeans
from .knn import KNN
from .random_forest import RandomForest
from .sgd import SGD


# 模型枚举 (类名称 = 调用名称)
class Models(Enum):
    XGBoost = 'xgboost'
    RandomForest = 'random_forest'
    KNN = 'knn'
    Kmeans = 'k_means'
    LR = 'linear_regression'


models_class_dict: dict = {}  # 通过小写名称查找大写
for item in Models:
    models_class_dict[item.value] = item.name

models_list: list = [el.value for el in Models]
models_class_name: list = [model.name for model in Models]
__all__ = ['models_list', 'models_class_dict', 'models_class_name'] + models_class_name


