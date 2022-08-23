import argparse
import pandas as pd
import importlib
import numpy as np
# import torch

def _import_class(str):
    module = importlib.import_module("/model/cnn",)
