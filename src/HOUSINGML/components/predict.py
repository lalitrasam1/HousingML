from src.HOUSINGML.utils.logger import logging
from src.HOUSINGML.utils.exception import CustomException
from src.HOUSINGML.config.configuration import getmodelPredictionConfig
from src.HOUSINGML.utils.common import load_object
import os
import sys
import pandas as pd

class ModelPrediction:
    def __init__(self):
        self.ModelPrediction=getmodelPredictionConfig()

    def Initiate_ModelPrediction(self, test_set):
        try:
            logging.info("Model prediction started")
            preprocessor=load_object(self.ModelPrediction.preprocessor)
            model=load_object(self.ModelPrediction.model_path)
            logging.info(test_set)
            test_set=pd.DataFrame(test_set)
            test_set=preprocessor.transform(test_set)
            test_set=pd.DataFrame(test_set)
            y_pred=model.predict(test_set)
            return y_pred[0]

        except Exception as e:
            logging.error(str(CustomException(error_message=e, error_detail=sys)))
            raise CustomException(error_message=e, error_detail=sys)
        
'''if __name__=="__main__":
    process=ModelPrediction()
    process.Initiate_ModelPrediction()'''
