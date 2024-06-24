import torch
import torch.nn as nn


class Softmax(nn.Module):
    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x/torch.sum(exp_x)


class SoftMaxStable(nn.Module):
    def forward(self, x):
        x = x - torch.max(x)
        exp_x = torch.exp(x)
        return exp_x/torch.sum(exp_x)


if __name__ == '__main__':
    softmax = Softmax()
    softmax_stable = SoftMaxStable()
    x = torch.tensor([1, 2, 3])
    print(softmax(x))
    print(softmax_stable(x))
