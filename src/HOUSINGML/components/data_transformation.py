from pathlib import Path
import os
import sys
from src.HOUSINGML.utils.logger import logging
from src.HOUSINGML.utils.exception import CustomException
from src.HOUSINGML.config.configuration import dataTransformationConfig
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.HOUSINGML.utils.common import save_object


class data_transformation:
    def __init__(self):
        self.datatransformationConfig=dataTransformationConfig()
    
    def get_data_transformation_object(self):
        '''This will give us preprocessor object
        '''
        try:
            numerical_columns=["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms",
                               "population", "households"]
            catagorical_columns=['ocean_proximity']

            os.makedirs(os.path.dirname(self.datatransformationConfig.preprocessor),exist_ok=True)
            logging.info("Numerical Features: "+str.join(",",numerical_columns))
            logging.info("catagorical Features: "+str.join(",",catagorical_columns))

            num_pipeline=Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scalar",MinMaxScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("encoder", OneHotEncoder(drop='first'))
                ]
            )
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline,catagorical_columns)
                ]
            )
            save_object(self.datatransformationConfig.preprocessor, preprocessor)
            logging.info("preprocessor saved at location: "+self.datatransformationConfig.preprocessor)
            return preprocessor            

        except Exception as e:
            logging.error(str(CustomException(error_message=e, error_detail=sys)))
            raise CustomException(error_message=e, error_detail=sys)


'''if __name__=="__main__":
    process=data_transformation()
    process.get_data_transformation_object()'''