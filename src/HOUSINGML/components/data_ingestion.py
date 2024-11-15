from pathlib import Path
from src.HOUSINGML.utils.logger import logging
from src.HOUSINGML.utils.exception import CustomException
from src.HOUSINGML.config.configuration import dataIngestionConfig
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import sys

class dataIngestion:
    def __init__(self):
        self.dataIngestionConfig=dataIngestionConfig()

    def Initiate_data_ingestion(self):
        try:
            logging.info("Data ingestion started")
            df=pd.read_csv(self.dataIngestionConfig.file_path)
            print(df.head())
            logging.info("Data loaded")
            os.makedirs(self.dataIngestionConfig.root_path, exist_ok=True)
            os.makedirs(os.path.dirname(self.dataIngestionConfig.row_data_path), exist_ok=True)
            df.to_csv(self.dataIngestionConfig.row_data_path, index=False, header=True)
            logging.info("Train test split started")
            train_set, test_set=train_test_split(df, test_size=0.2, random_state= 42)
            train_set=pd.DataFrame(train_set)
            train_set.to_csv(self.dataIngestionConfig.train_data_path, index=False, header=True)
            test_set=pd.DataFrame(test_set)
            test_set.to_csv(self.dataIngestionConfig.test_data_path, index=False, header=True)
            logging.info("Train test split completed")
            logging.info("Train path: "+self.dataIngestionConfig.train_data_path)
            logging.info("Test path: "+self.dataIngestionConfig.test_data_path)
            return(
                self.dataIngestionConfig.train_data_path,
                self.dataIngestionConfig.test_data_path
            )
        except Exception as e:
            logging.error(str(CustomException(e, sys)))
            raise CustomException(e, sys)

'''if __name__=="__main__":
    process=dataIngestion()
    trainpath, testPath = process.Initiate_data_ingestion()'''
    