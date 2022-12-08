from torch.utils.data import Dataset, DataLoader
import pandas as pd
import os
import config


def get_dataset_from_file(path):
    path = os.path.join(config.DATA_PATH, path)
    if 'data_type' == 'form':  # TODO: 增加数据集种类
        return StructDataset(path)

    return StructDataset(path)


class StructDataset(Dataset):
    def __init__(self, path):
        self.data = pd.read_csv(path, dtype=int)

    def __getitem__(self, index):
        return self.data.iloc[index]

    def __len__(self):
        return len(self.data)

    @property
    def train_data(self):
        return None

    @property
    def dataframe(self):
        return self.data
