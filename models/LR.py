from torch.utils.data import Dataset
from models.model import Model
from sklearn.linear_model import LogisticRegression
from torch_utils import StructDataset
from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.metrics import classification_report
import pandas as pd


class LR(Model):
    def __init__(self):
        self.dataset = None
        self.Lr = LogisticRegression()
        self.acc = float()

    def get_prediction(self, data) -> dict:
        test = pd.DataFrame([data['data']])
        ret = dict()
        if self.Lr.predict(test)[0] == 0:
            ret['prediction'] = "false"
        else:
            ret['prediction'] = "true"
        ret['precision'] = self.acc
        return ret

    def fit(self, parameter: dict) -> dict:
        train_x, test_x = train_test_split(self.dataset.dataframe, test_size=0.2, shuffle=False)
        train_y = train_x.pop('Diabetes_binary')
        test_y = test_x.pop('Diabetes_binary')
        weight = [1] * len(train_y)
        for i in range(0, len(train_y)):
            if train_y[i] == 1:
                weight[i] = 1  # 权重调整
        # 训练
        self.Lr.fit(train_x, train_y, sample_weight=weight)
        preds = self.Lr.predict(train_x)
        self.acc = self.Lr.score(train_x, train_y)

        return classification_report(train_y, preds, output_dict=True)

    def load_data(self, dataset: Dataset):
        self.dataset = dataset

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass
