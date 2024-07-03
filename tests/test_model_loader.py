import os
from src.model_loader import ModelLoader
from src.text_preprocessing import TextPreprocessor


def test_predict_sentiment() -> None:
    """
    Test function for predicting sentiment using ModelLoader.

    Raises:
        AssertionError: If the predicted result does not contain 'sentiment' or 'score'.
    """
    tokenizer_file = "model_files/tokenizer.pickle"
    model_file = "model_files/model.keras"
    # Check if the file exists : gitHubAction case
    if not os.path.isfile(model_file):
        model_file = "_local_model_files/model.keras"
    #
    model_loader = ModelLoader(model_file, tokenizer_file)
    #
    preprocessor = TextPreprocessor()
    text = "This is a test tweet!"
    result = model_loader.predict_sentiment(text, preprocessor)
    assert "sentiment" in result, f"Expected 'sentiment' in result but got: {result}"
    assert "score" in result, f"Expected 'score' in result but got: {result}"


if __name__ == "__main__":
    test_predict_sentiment()
