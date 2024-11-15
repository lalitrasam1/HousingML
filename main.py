from src.HOUSINGML.utils.logger import logging
from src.HOUSINGML.utils.exception import CustomException
import sys
from src.HOUSINGML.pipeline.stage01_dataIngestion import dataingestionpipeline
from src.HOUSINGML.pipeline.stage02_datatransformation import datatransformationpipeline
from src.HOUSINGML.pipeline.stage03_modelTraining import modeltrainingpipeline
from src.HOUSINGML.pipeline.stage04_ModelEvaluation import modelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = dataingestionpipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.error(str(CustomException(e, sys)))
        raise CustomException(e, sys)

STAGE_NAME = "Data Transformation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_transformation = datatransformationpipeline()
   data_transformation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.error(str(CustomException(e, sys)))
        raise CustomException(e, sys)

STAGE_NAME = "Model Training stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   ModelTrainer = modeltrainingpipeline()
   ModelTrainer.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.error(str(CustomException(e, sys)))
        raise CustomException(e, sys)

STAGE_NAME = "Model Evaluation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   ModelEvaluation = modelEvaluationPipeline()
   ModelEvaluation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.error(str(CustomException(e, sys)))
        raise CustomException(e, sys)