from src.HOUSINGML.utils.logger import logging
from src.HOUSINGML.utils.exception import CustomException
import sys
from src.HOUSINGML.pipeline.stage01_dataIngestion import dataingestionpipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = dataingestionpipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.error(str(CustomException(e, sys)))
        raise CustomException(e, sys)

