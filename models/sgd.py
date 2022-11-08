import pandas as pd

from .model import Model
from torch_utils import StructDataset
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


class SGD(Model):
    def __init__(self):
        pass

    def fit(self, parameter: dict):
        return

    def load_data(self, dataset: StructDataset):
        pass

    def get_prediction(self, data):
        return

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass
