from src.HOUSINGML.utils.logger import logging
from src.HOUSINGML.utils.exception import CustomException
from src.HOUSINGML.config.configuration import getmodelEvaluationConfig
from src.HOUSINGML.utils.common import load_object
import os
import sys
import pandas as pd
from sklearn.metrics import r2_score

class ModelEvaluation:
    def __init__(self):
        self.ModelEvaluationConfig=getmodelEvaluationConfig()

    def Initiate_ModelEvaluation(self):
        try:
            logging.info("Model Evaluation started")
            test_set=pd.read_csv(self.ModelEvaluationConfig.test_data_path)
            X_test=test_set.drop('median_house_value', axis=1)
            y_test=test_set['median_house_value']
            preprocessor=load_object(self.ModelEvaluationConfig.preprocessor)
            model=load_object(self.ModelEvaluationConfig.model_path)
            X_test=preprocessor.transform(X_test)
            X_test=pd.DataFrame(X_test)
            y_pred=model.predict(X_test)
            logging.info(r2_score(y_test,y_pred))
            print(r2_score(y_test,y_pred))

        except Exception as e:
            logging.error(str(CustomException(error_message=e, error_detail=sys)))
            raise CustomException(error_message=e, error_detail=sys)
        

if __name__=="__main__":
    process= ModelEvaluation()
    process.Initiate_ModelEvaluation()



