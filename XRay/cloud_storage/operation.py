import os
import sys
from XRay.exception import XRayException
import shutil


class LocalOperation:

    def syn_from_local(self, src_folder:str, dest_folder:str ):

        try:
            
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            for item in os.listdir(src_folder):
                src_item = os.path.join(src_folder, item)
                dest_item = os.path.join(dest_folder, item)

                if os.path.isdir(src_item):
                    shutil.copytree(src_item, dest_item, dirs_exist_ok=True)

                else:
                    shutil.copy2(src_item, dest_item)

        except Exception as e:
            raise XRayException(e, sys)
