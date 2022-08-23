
BATCH_SIZE=100

class BaseDataModule():
    def __init__(args,self) -> None:
        self.batch_size = args.get("batch_size",BATCH_SIZE)
        pass

    def prepare_data():
        pass
    def split_data():
        pass 