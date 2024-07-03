import os
import json
from typing import Any, Dict

from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

from src.model_loader import ModelLoader
from src.text_preprocessing import TextPreprocessor


class Tweet(BaseModel):
    """
    Pydantic model to validate the input for tweet sentiment prediction.

    Attributes:
        text (str): The text of the tweet to be analyzed.
    """

    text: str = Field(..., max_length=280)


# Paths to the model and tokenizer files
tokenizer_file = "model_files/tokenizer.pickle"
model_file = "model_files/model.keras"

# Check if the model file exists (GitHub Action case)
if not os.path.isfile(model_file):
    model_file = "tmp/model_files/model7.keras"

# Create instances of necessary classes
preprocessor = TextPreprocessor()
model_loader = ModelLoader(model_file, tokenizer_file)

# Create the FastAPI app
app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> Dict[str, str]:
    """
    Root endpoint returning a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"Hello": "World.....!!!!"}


@app.post("/predict")
async def prediction(input_parameters: Tweet) -> Dict[str, Any]:
    """
    Endpoint for predicting the sentiment of a given tweet text.

    Args:
        input_parameters (Tweet): The input parameters containing
        the tweet text.

    Returns:
        dict: A dictionary containing the predicted sentiment
        and score.
    """
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    sentiment_result = model_loader.predict_sentiment(
        input_dictionary["text"], preprocessor
    )
    return {"sentiment": sentiment_result["sentiment"]}
