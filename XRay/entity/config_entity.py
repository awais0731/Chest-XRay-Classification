import os
from dataclasses import dataclass
from XRay.constant.training_pipeline import *


@dataclass
class DataIngestionConfig:
    
    def __init__(self):
        self.data_folder:str = Data_FOLDER
        self.artifact_dir:str = os.path.join(ARTIFACT_DIR, TIMESTAMP)

        self.data_path:str = os.path.join(self.artifact_dir, "data_ingestion", self.data_folder)

        self.train_data_path:str = os.path.join(self.data_path, "train")
        self.test_data_path:str = os.path.join(self.data_path, "test")