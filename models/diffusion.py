import pandas as pd
import torch
import numpy as np
import matplotlib.pyplot as plt
from .model import Model
from torch_utils import StructDataset
from sklearn.datasets import make_s_curve
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


class Diffusion(Model):
    def __init__(self):
        self.s_curve = None
        self.data = None
        self.dataset = None
        self.num_steps = 100
        self.betas = torch.linspace(-6, 6, self.num_steps)
        self.betas = torch.sigmoid(self.betas) * (0.5e-2 - 1e-5) + 1e-5

        # 维度应该相同
        self.alphas = 1 - self.betas
        self.alpha_prod = torch.cumprod(self.alphas, 0)
        self.alpha_prod_p = torch.cat([torch.tensor([1]).float(), self.alpha_prod[:-1]], 0)
        self.alphas_bar_sqrt = torch.sqrt(self.alpha_prod)
        self.one_minus_alphas_bar_sqrt = torch.sqrt(1 - self.alpha_prod)
        self.one_minus_alphas_bar_log = torch.log(1 - self.alpha_prod)
        print('all shape:', self.betas.shape)

    # 确定扩散过程任意时刻采样值
    def q_x(self, x_0, t):
        noise = torch.randn_like(x_0)  # 从正态分布生成随机噪声
        alpha_t = self.alphas_bar_sqrt[t]
        alpha_1_m_t = self.one_minus_alphas_bar_sqrt[t]
        return alpha_t * x_0 + alpha_1_m_t * noise

    def show_add_noise_effect(self, num_shows=20):
        fig, axs = plt.subplots(2, 10, figsize=(28, 3))
        plt.rc('text', color='blue')
        for i in range(num_shows):
            j = i
            k = i % 10
            q_i = self.q_x(self.dataset, torch.tensor([i * self.num_steps // num_shows]))
            axs[j, k].scatter(q_i[:, 0], q_i[:, 1], color='red', edgecolor='white')
            axs[j, k].set_axis_off()
            axs[j, k].set_title(str(i * self.num_steps // num_shows))

    def fit(self, parameter: dict):
        return

    def load_data(self, dataset: StructDataset):
        self.s_curve, _ = make_s_curve(10 ** 4, noise=0.1)
        self.s_curve = self.s_curve[:, [0, 2]] / 10.0

        print("shape: ", np.shape(self.s_curve))

        self.data = self.s_curve.T

        fig, ax = plt.subplots()
        ax.scatter(*self.data, color="red", edgecolor='white')
        ax.axis('off')
        plt.show()

        self.dataset = torch.Tensor(self.s_curve).float()
        pass

    def get_prediction(self, data):
        return

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass


