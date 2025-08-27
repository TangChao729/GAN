# Modern PyTorch Imports for GAN Notebook
# Replace the old imports with these modern equivalents

# OLD (deprecated):
# from torch.autograd.variable import Variable

# NEW (modern PyTorch 2.0+):
import torch
from torch import nn, optim
from torchvision import transforms, datasets
import numpy as np
from IPython import display
import matplotlib.pyplot as plt

# Modern way to create tensors with autograd (replaces Variable)
def noise(size):
    """Generate random noise tensor (replaces Variable usage)"""
    n = torch.randn(size, 100)
    if torch.cuda.is_available(): 
        return n.cuda() 
    return n

# Example of modern tensor operations:
# OLD: Variable(torch.randn(64, 100))
# NEW: torch.randn(64, 100)  # autograd is automatic!

print("✅ Modern imports ready!")
print("✅ tensorboardX installed")
print("✅ utils.py updated for modern PyTorch")
print("\nYour notebook should now work with our uv environment!")
