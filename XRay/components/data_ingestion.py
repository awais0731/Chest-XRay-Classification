from XRay.entity.config_entity import DataIngestionConfig
from XRay.entity.artifact_entity import DataIngestionArtifact
from XRay.cloud_storage.operation import LocalOperation
from XRay.logger import logging
from XRay.exception import XRayException
import sys

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

        self.local = LocalOperation()

    def get_data_from_local(self) -> None:
        try:
            logging.info("Entered the get_data_from_local method of Data ingestion class")

            self.local.syn_from_local(
                src_folder=r"D:\DataSets\xray data",
                dest_folder=self.data_ingestion_config.data_path
            )

            logging.info("Exited the get_data_from_s3 method of Data ingestion class")

        except Exception as e:
            raise XRayException(e, sys)
        

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the initiate_data_ingestion method of Data ingestion class")

        try:
            self.get_data_from_local()

            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                train_file_path = self.data_ingestion_config.train_data_path,
                test_file_path = self.data_ingestion_config.test_data_path
            )

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")

            return data_ingestion_artifact

        except Exception as e:
            raise XRayException(e, sys)