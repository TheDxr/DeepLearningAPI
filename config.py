from enum import Enum


class Models(Enum):
    XGBoost = 'xgboost'
    DeepFM = 'deepFM'


# models = ('xgboost', 'DeepFM')

defaultData = 'diabetes_binary_health_indicators_BRFSS2015.csv'
dataPath = 'D:\\DataSets\\diabetes\\'

