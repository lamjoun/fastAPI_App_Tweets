import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences


class ModelLoader:
    """
    A class to load a TensorFlow model and tokenizer for sentiment analysis,
    and predict sentiment based on input text.

    Attributes:
        model_path (str): File path to the saved Keras model.
        tokenizer_path (str): File path to the saved tokenizer.
        model (tf.keras.Model): Loaded Keras model.
        tokenizer (object): Loaded tokenizer object.
    """

    def __init__(self, model_path: str, tokenizer_path: str):
        """
        Initializes the ModelLoader instance with model and tokenizer paths.

        Args:
            model_path (str): File path to the saved Keras model.
            tokenizer_path (str): File path to the saved tokenizer.
        """
        self.model_path = model_path
        self.tokenizer_path = tokenizer_path
        self.model = self._load_model()
        self.tokenizer = self._load_tokenizer()

    def _load_model(self) -> tf.keras.Model:
        """
        Loads the Keras model from the specified path.

        Returns:
            tf.keras.Model: Loaded Keras model.
        """
        return tf.keras.models.load_model(self.model_path)

    def _load_tokenizer(self):
        """
        Loads the tokenizer from the specified path.

        Returns:
            object: Loaded tokenizer object.
        """
        with open(self.tokenizer_path, "rb") as handle:
            try:
                tokenizer = pickle.load(handle)
            except ModuleNotFoundError as e:
                if "keras.src.preprocessing" in str(e):
                    import keras

                    keras.utils.get_custom_objects()
                    with open(self.tokenizer_path, "rb") as handle:
                        tokenizer = pickle.load(handle)
                else:
                    raise e
        return tokenizer

    # preprocessor: Callable[[str], str]
    def predict_sentiment(self, text: str, preprocessor) -> dict:
        """
        Predicts sentiment (Positive/Negative) and sentiment score
        for the input text.

        Args:
            text (str): Input text to predict sentiment.
            preprocessor (Callable[[str], str]): Preprocessing function
            for text.

        Returns:
            dict: Dictionary containing predicted sentiment
            ("Positive" or "Negative") and sentiment score.
        """
        processed_text = preprocessor.preprocess(text)
        sequence = self.tokenizer.texts_to_sequences([processed_text])
        padded_sequence = pad_sequences(sequence, maxlen=30)
        score = self.model.predict(padded_sequence, verbose=0)[0][0]
        sentiment = "Positive" if score > 0.5 else "Negative"
        return {"sentiment": sentiment, "score": score}
