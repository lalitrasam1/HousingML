from src.HOUSINGML.components.model_training import model_trainer
from src.HOUSINGML.utils.logger import logging

class modeltrainingpipeline:
    def __init__(self):
        pass
    def main(self):
        logging.info("Model Training pipeline started")
        process=model_trainer()
        process.initiate_model_training()