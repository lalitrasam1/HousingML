from src.HOUSINGML.utils.exception import CustomException
from src.HOUSINGML.utils.logger import logging
import yaml
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import sys
import os
import pandas as pd
from src.HOUSINGML.constants.constants import Config_File_path

def read_Config(Path_to_Yaml=Config_File_path):
    try:
        with open(Path_to_Yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info("YAML file loaded: "+str(Path_to_Yaml))
            content=ConfigBox(content)
            return content
    except Exception as e:
        logging.error(str(CustomException(error_message=e, error_detail=sys)))
        raise CustomException(error_message=e, error_detail=sys)
    
def save_object(filePath, obj):
    try:
        os.makedirs(os.path.dirname(filePath),exist_ok=True)
        pd.to_pickle(obj=obj,filepath_or_buffer=filePath)
    except Exception as e:
        logging.error(str(CustomException(error_message=e, error_detail=sys)))
        raise CustomException(error_message=e, error_detail=sys)
    

def load_object(filepath):
    obj=pd.read_pickle(filepath)
    return obj