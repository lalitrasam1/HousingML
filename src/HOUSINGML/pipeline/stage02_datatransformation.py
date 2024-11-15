from src.HOUSINGML.components.data_transformation import data_transformation
from src.HOUSINGML.utils.logger import logging

class datatransformationpipeline:
    def __init__(self):
        pass
    def main(self):
        logging.info("Data transformation pipeline started")
        process=data_transformation()
        process.get_data_transformation_object()