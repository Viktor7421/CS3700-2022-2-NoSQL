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
    class_ = getattr(module,class_name)
    # print(class_)
    return class_
    


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_class", type=str, default="CNN")
    # parser.add_argument("--data_class", type=str, default="MNIST")

    temp_args, _ = parser.parse_known_args()
    
    print(_)
    # print(temp_args.model_class)

    model_class = _import_class(f"model.{temp_args.model_class}")

    model_group = parser.add_argument_group("Model Args")
    

    # model = model_class(model_group)
    model_class.add_to_argparse(model_group)




if __name__ == '__main__':
    main()