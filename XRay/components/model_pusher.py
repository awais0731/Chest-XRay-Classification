
from XRay.entity.config_entity import ModelPusherConfig
from XRay.entity.artifact_entity import ModelTrainerArtifact
from XRay.cloud_storage.operation import LocalOperation
from XRay.logger import logging
from XRay.exception import XRayException
from XRay.entity.artifact_entity import ModelPusherArtifact
import os,sys
import shutil

# class ModelPusher:

#     def __init__(self,model_pusher_config: ModelPusherConfig, model_trainer_artifact:ModelTrainerArtifact):

#         self.model_pusher_config = model_pusher_config
#         self.model_trainer_artifact = model_trainer_artifact


#     def initiate_model_pusher(self):
#         try:
#             logging.info("pushing the model to save_model dir")
#             trained_model_path = self.model_trainer_artifact.trained_model_path

#             saved_model_path = self.model_pusher_config.saved_model_path

#             os.makedirs(os.path.dirname(saved_model_path),exist_ok=True)

#             shutil.copy(src=trained_model_path, dst=saved_model_path)

#             logging.info("model pussing successfuly")
            
#         except Exception as e:
#             raise e


class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig):
        self.model_pusher_config = model_pusher_config

    
    def build_and_push_bento_image(self):
        logging.info("Entered build_and_push_bento_image method of ModelPusher class")

        try:
            logging.info("Building the bento from bentofile.yaml")

            os.system("bentoml build")

            os.system(f"bentoml containerize {self.model_pusher_config.bentoml_service_name}:latest -t {self.model_pusher_config.bentoml_service_name}_local:latest")

            # logging.info("Built the bento from bentofile.yaml")

            # logging.info("Creating docker image for bento")


            # os.system(
            #     f"bentoml containerize {self.model_pusher_config.bentoml_service_name}:latest -t 136566696263.dkr.ecr.us-east-1.amazonaws.com/{self.model_pusher_config.bentoml_ecr_image}:latest"
            # )

            # logging.info("Created docker image for bento")

            # logging.info("Logging into ECR")

            # os.system(
            #     "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 136566696263.dkr.ecr.us-east-1.amazonaws.com"
            # )

            # logging.info("Logged into ECR")

            # logging.info("Pushing bento image to ECR")
            

            # os.system(
            #     f"docker push 136566696263.dkr.ecr.us-east-1.amazonaws.com/{self.model_pusher_config.bentoml_ecr_image}:latest"
            # )

            # logging.info("Pushed bento image to ECR")

            logging.info(
                "Exited build_and_push_bento_image method of ModelPusher class"
            )

        except Exception as e:
            raise XRayException(e, sys)
        

    
    def initiate_model_pusher(self) -> ModelPusherArtifact:
        
        logging.info("Entered initiate_model_pusher method of ModelPusher class")

        try:
            self.build_and_push_bento_image()

            model_pusher_artifact = ModelPusherArtifact(
                bentoml_model_name=self.model_pusher_config.bentoml_model_name,
                bentoml_service_name=self.model_pusher_config.bentoml_service_name,
            )

            logging.info("Exited the initiate_model_pusher method of ModelPusher class")

            return model_pusher_artifact

        except Exception as e:
            raise XRayException(e, sys)
