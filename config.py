from enum import Enum


class Models(Enum):
    XGBoost = 'xgboost'
    DeepFM = 'deepFM'
    RandomForest = 'random_forest'
    Knn = 'knn'
    Kmeans='k-means'

# models = ('xgboost', 'DeepFM','random_forest' ,'knn')
models = [el.value for el in Models]
defaultData = 'diabetes_binary_health_indicators_BRFSS2015.csv'
dataPath = 'D:\\DataSets\\diabetes\\'

