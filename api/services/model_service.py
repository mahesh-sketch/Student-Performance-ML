import sys
import pandas as pd

from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from api.schemas.prediction_input import PredictionInput

from src.exception import CustomException
from src.logger import logging


def get_prediction(input_data: dict) -> float:
    try:
        data = CustomData(
            gender=input_data["gender"],
            race_ethnicity=input_data["race_ethnicity"],
            parental_level_of_education=input_data["parental_level_of_education"],
            lunch=input_data["lunch"],
            test_preparation_course=input_data["test_preparation_course"],
            reading_score=input_data["reading_score"],
            writing_score=input_data["writing_score"],
        )

        df = data.get_data_as_data_frame()
        model_pipeline = PredictPipeline()
        prediction = model_pipeline.predict(df)

        return float(prediction[0])
    except Exception as e:
        logging.error(f"Error in get_prediction: {e}")
        raise CustomException(e,sys)