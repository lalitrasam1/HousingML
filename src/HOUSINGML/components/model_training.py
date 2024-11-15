from pathlib import Path
import os
import sys
import pandas as pd
from src.HOUSINGML.utils.logger import logging
from src.HOUSINGML.utils.exception import CustomException
from src.HOUSINGML.config.configuration import getmodelconfig
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.HOUSINGML.utils.common import read_Config, save_object, load_object
from src.HOUSINGML.constants.constants import Params_File_path

class model_trainer:
    def __init__(self):
        self.modelconfig = getmodelconfig()

    def initiate_model_training(self):
        try:
            logging.info("Initiate model training started")
            train_set=pd.read_csv(self.modelconfig.train_data_path)
            X_train=train_set.drop('median_house_value', axis=1)
            y_train=train_set['median_house_value']
            logging.info("Initiate data transformation")
            preprocessor=load_object(self.modelconfig.preprocessor)
            X_train=preprocessor.fit_transform(X_train)
            X_train=pd.DataFrame(X_train)
            XGB=XGBRegressor()
            params=read_Config(Path_to_Yaml=Params_File_path)
            param_grid = { 
                          'n_estimators': params.XGB_parameters.n_estimators, 
                          'learning_rate': params.XGB_parameters.learning_rate, 
                          'max_depth': params.XGB_parameters.max_depth, 
                          'subsample': params.XGB_parameters.subsample, 
                          'colsample_bytree': params.XGB_parameters.colsample_bytree
                          }
            grid_search = GridSearchCV(estimator=XGB, 
                                       param_grid=param_grid, 
                                       cv=5, 
                                       scoring='r2', 
                                       n_jobs=-1, 
                                       verbose=2)
            grid_search.fit(X_train, y_train)
            print("Best Parameters:", grid_search.best_params_) 
            print("Best Score:", grid_search.best_score_)
            best_model = grid_search.best_estimator_
            os.makedirs(os.path.dirname(self.modelconfig.model_path),exist_ok=True)
            save_object(self.modelconfig.model_path, best_model)
            save_object(self.modelconfig.preprocessor, preprocessor)
            logging.info(self.modelconfig.model_path)
            return best_model

        
        except Exception as e:
            logging.error(str(CustomException(error_message=e, error_detail=sys)))
            raise CustomException(error_message=e, error_detail=sys)
        
if __name__=="__main__":
    process=model_trainer()
    process.initiate_model_training()