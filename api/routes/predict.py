import sys
from fastapi import APIRouter
from api.schemas.prediction_input import PredictionInput
from api.services.model_service import get_prediction

from src.exception import CustomException
from src.logger import logging

router = APIRouter()

@router.post("/")
async def predict_score(input_data: PredictionInput):
    """
    Predict the score based on the input data.
    """
    try:
        logging.info("Received input data for prediction")
        # Convert input data to a dictionary
        input_dict = input_data.dict()
        
        # Get prediction from the service
        prediction = get_prediction(input_dict)
        
        logging.info(f"Prediction result: {prediction}")
        
        return {"prediction": prediction}
    except Exception as e:
        logging.error(f"Error occurred during prediction: {str(e)}")
        raise CustomException(e, sys)