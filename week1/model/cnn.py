from typing  import Any, Dict

CONV_DIM = 16
FC_DIM = 18

class CNN():
    def __init__(self, data_config: Dict[str,Any], args) -> None:

        pass

    @staticmethod
    def add_to_argparse(parser):
        parser.add_argument("--conv_dim", type=int, default=CONV_DIM)
        parser.add_argument("--fc_dim", type=int, default=FC_DIM)
        pass