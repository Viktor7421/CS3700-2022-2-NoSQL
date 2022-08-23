import argparse
import importlib
# import pandas as pd
# import numpy as np
# import torch

# from model import cnn

def _import_class(module_and_class_name: str):
    """ model.cnn  -  model.mlp"""
    module_name, class_name = module_and_class_name.rsplit(".",1)
    # print(module_name,class_name)
    module = importlib.import_module(module_name)
    print(module)


def main():
    print(_import_class("model.cnn"))

if __name__ == '__main__':
    main()