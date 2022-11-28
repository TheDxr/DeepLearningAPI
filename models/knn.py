from .model import Model
from torch_utils import StructDataset
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


# TODO
class KNN(Model):
    def __init__(self):
        self.dataset = None
        # self.knn = neighbors.KNeighborsClassifier(n_neighbors=self.best_k)
        self.acc = float()

    def best_k(self):
        train_x, test_x = train_test_split(self.dataset.dataframe, test_size=0.2, shuffle=False)
        train_y = train_x.pop('Diabetes_binary')
        test_y = test_x.pop('Diabetes_binary')
        weight = [1] * len(train_y)
        for i in range(0, len(train_y)):
            if train_y[i] == 1:
                weight[i] = 1  # 权重调整
        k_range = range(1, 31)  # 设置循环次数
        k_error = []
        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            # cv参数决定数据集划分比例，这里是按照5:1划分训练集和测试集
            scores = cross_val_score(knn, train_x, train_y, cv=6, scoring='accuracy')
            k_error.append(1 - scores.mean())

        return k_error.index(min(k_error))

    def fit(self, parameter: dict):
        best = self.best_k()
        self.knn = KNeighborsClassifier(n_neighbors=best)
        train_x, test_x = train_test_split(self.dataset.dataframe, test_size=0.2, shuffle=False)
        train_y = train_x.pop('Diabetes_binary')
        test_y = test_x.pop('Diabetes_binary')
        weight = [1] * len(train_y)
        for i in range(0, len(train_y)):
            if train_y[i] == 1:
                weight[i] = 1  # 权重调整
        # 训练
        self.knn.fit(train_x, train_y)
        preds = self.knn.predict(train_x)
        self.acc = self.knn.score(train_x, train_y)

        return classification_report(train_y, preds, output_dict=True)

    def load_data(self, dataset: StructDataset):
        self.dataset = dataset

    def get_prediction(self, data):
        return

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass
