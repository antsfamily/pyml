# Copyright (c) 2016-2018, Zhi Liu.  All rights reserved.
from __future__ import absolute_import

# from .version import __version__

# __all__ = ['__version__']

from . import math
from .math.rand import randperm

from . import nn
from .nn.activations import linear, sigmoid, tanh, softplus, softsign, elu, relu, relu6, selu, crelu, leaky_relu
