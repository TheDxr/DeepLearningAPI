from models.sgd import SGD
from models.diffusion import Diffusion
import config
import torch

# model = Diffusion()
# model.load_data(None)
# model.show_add_noise_effect()

a = torch.randn([3, 3])

print(a)
print(a[:-1, 2])
