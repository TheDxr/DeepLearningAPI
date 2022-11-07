from abc import abstractmethod, ABCMeta

from torch.utils.data import Dataset


class Model(metaclass=ABCMeta):

    @abstractmethod
    def get_prediction(self, data) -> dict:
        pass

    @abstractmethod
    def fit(self, parameter: dict) -> dict:
        pass

    @abstractmethod
    def load_data(self, dataset: Dataset):
        pass

    @abstractmethod
    def save_model(self, path):
        pass

    @abstractmethod
    def load_model(self, path):
        pass
