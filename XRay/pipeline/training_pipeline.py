from XRay.entity.config_entity import DataIngestionConfig
from XRay.entity.artifact_entity import DataIngestionArtifact
from XRay.components.data_ingestion import DataIngestion
from XRay.logger import logging
from XRay.exception import XRayException
import os, sys

class TrainPipeline:

    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()

    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")

        try:
            logging.info("Getting the data from local bucket")

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train_set and test_set from s3")

            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact
        except Exception as e:
            raise XRayException(e, sys)
        


    
    def run_pipeline(self) -> None:
        data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()