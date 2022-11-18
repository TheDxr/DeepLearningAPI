from enum import Enum


class Models(Enum):
    XGBoost = 'xgboost'



defaultData = 'diabetes_binary_health_indicators_BRFSS2015.csv'
dataPath = 'D:\\DataSets\\diabetes\\'
models = [el.value for el in Models]
