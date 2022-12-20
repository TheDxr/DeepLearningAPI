import json

import pandas as pd
from torch_utils import StructDataset
from .model import Model
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

import xgboost as xgb
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score


class XGBoost(Model):
    def __init__(self):
        self.dataset = None
        self.Xgb = xgb.XGBRFClassifier(learning_rate=0.1)  # TODO
        self.acc = float()

    def fit(self, parameter: dict):

        train_x, test_x = train_test_split(self.dataset.dataframe, test_size=0.1, shuffle=False)
        train_y = train_x.pop('Diabetes_binary')

        test_y = test_x.pop('Diabetes_binary')
        weight = [1] * len(train_y)
        for i in range(0, len(train_y)):
            if train_y[i] == 1:
                weight[i] = 1  # 权重调整
        # 训练
        self.Xgb.fit(train_x, train_y, sample_weight=weight)
        preds = self.Xgb.predict(test_x)
        self.acc = self.Xgb.score(test_x, test_y)
        return classification_report(test_y, preds, output_dict=True)

    def load_data(self, dataset: StructDataset):
        self.dataset = dataset

    def get_prediction(self, data):
        test = pd.DataFrame([data['data']])
        ret = dict()
        if self.Xgb.predict(test)[0] == 0:
            ret['prediction'] = "false"
        else:
            ret['prediction'] = "true"
        ret['precision'] = self.acc
        return ret

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass
