from src.HOUSINGML.components.data_ingestion import dataIngestion

class dataingestionpipeline:
    def __init__(self):
        pass
    def main(self):
        process=dataIngestion()
        trainpath, testPath = process.Initiate_data_ingestion()