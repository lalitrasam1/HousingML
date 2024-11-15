from src.HOUSINGML.components.data_ingestion import dataIngestion
from src.HOUSINGML.utils.logger import logging

class dataingestionpipeline:
    def __init__(self):
        pass
    def main(self):
        logging.info("Data ingestion pipeline")
        process=dataIngestion()
        trainpath, testPath = process.Initiate_data_ingestion()