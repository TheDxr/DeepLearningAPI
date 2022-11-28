import pandas as pd

from torch_utils import StructDataset
from .model import Model
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class Kmeans(Model):
    def __init__(self):
        self.dataset = None
        self.kmeans=KMeans()
        self.acc = float()

    def best_n(self):
        train_x, test_x = train_test_split(self.dataset.dataframe, test_size=0.2, shuffle=False)
        train_y = train_x.pop('Diabetes_binary')
        test_y = test_x.pop('Diabetes_binary')
        sc_X = StandardScaler()
        train_x = sc_X.fit_transform(train_x)
        test_x = sc_X.transform(test_x)
        sc_y = StandardScaler()
        y_train = sc_y.fit_transform(train_y)

        wcss = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
            kmeans.fit(train_x)
            wcss.append(kmeans.inertia_)
        return wcss.index(min(wcss))

    def fit(self, parameter: dict):
        n = self.best_n()
        self.kmeans = KMeans(n_clusters=n, init='k-means++', random_state=42)
        train_x, test_x = train_test_split(self.dataset.dataframe, test_size=0.2, shuffle=False)
        train_y = train_x.pop('Diabetes_binary')
        test_y = test_x.pop('Diabetes_binary')
        sc_X = StandardScaler()
        train_x = sc_X.fit_transform(train_x)
        test_x = sc_X.transform(test_x)
        sc_y = StandardScaler()
        y_train = sc_y.fit_transform(train_y)

        self.kmeans.fit(train_x, train_y)
        preds = self.kmeans.predict(test_x)
        self.acc = self.kmeans.score(test_x, test_y)

        return classification_report(test_y, preds, output_dict=True)

    def load_data(self, dataset: StructDataset):
        self.dataset = dataset

    def get_prediction(self, data):
        test = pd.DataFrame([data['data']])
        ret = dict()
        if self.kmeans.predict(test)[0] == 0:
            ret['prediction'] = "false"
        else:
            ret['prediction'] = "true"
        ret['precision'] = self.acc
        return ret

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass
