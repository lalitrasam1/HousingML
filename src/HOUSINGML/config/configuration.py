from dataclasses import dataclass
from src.HOUSINGML.utils.common import read_Config
from pathlib import Path

Config=read_Config()

@dataclass
class dataIngestionConfig:
    root_path : Path =Config.Dataingestion.root_path
    file_path : str = Config.Dataingestion.file_path
    row_data_path : Path = Config.Dataingestion.row_data_path
    train_data_path : Path= Config.Dataingestion.train_data_path
    test_data_path : Path = Config.Dataingestion.test_data_path

@dataclass
class dataTransformationConfig:
    preprocessor: Path = Config.DataTransformation.preprocessor_path

@dataclass
class getmodelconfig:
    model_path: Path = Config.Modeltrainer.model_path
    preprocessor: Path = Config.Modeltrainer.preprocessor_path
    train_data_path : Path= Config.Modeltrainer.train_data_path

@dataclass
class getmodelEvaluationConfig:
    model_path: Path = Config.ModelEvaluation.model_path
    preprocessor: Path = Config.ModelEvaluation.preprocessor_path
    test_data_path : Path = Config.ModelEvaluation.test_data_path