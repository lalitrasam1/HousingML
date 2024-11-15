from src.HOUSINGML.components.model_evaluation import ModelEvaluation
from src.HOUSINGML.utils.logger import logging

class modelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        logging.info("Model Evaluation pipeline started")
        process= ModelEvaluation()
        process.Initiate_ModelEvaluation()