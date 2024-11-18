from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import BytesIO
from src.HOUSINGML.pipeline.stage05_ModelPrediction import ModelPredictionpipeline
from src.HOUSINGML.utils.logger import logging
app = FastAPI()

@app.post("/get_price/")
async def get_price(file: UploadFile = File(...)):
    # Read the uploaded file
    contents = await file.read()
    # Convert bytes to a DataFrame
    df = pd.read_csv(BytesIO(contents))
    df.astype
    # For demonstration, we print the DataFrame
    print(df)
    prediction= ModelPredictionpipeline()
    y_pred=prediction.main(test_set=df)
    logging.info(y_pred)
    return (str(y_pred))


# Run the app
# Run with: uvicorn script_name:app --reload
