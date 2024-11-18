from src.HOUSINGML.components.predict import ModelPrediction
from src.HOUSINGML.utils.logger import logging

class ModelPredictionpipeline:
    def __init__(self):
        pass
    def main(self, test_set):
        logging.info("Data prediction pipeline")
        process=ModelPrediction()
        return process.Initiate_ModelPrediction(test_set=test_set)
    