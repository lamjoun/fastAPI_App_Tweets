import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from typing import Set

nltk.download('stopwords')

class TextPreprocessor:
    """
    A class to preprocess text data, including cleaning, tokenizing, 
    removing stop words, and optional stemming.

    Attributes:
        stop_words (Set[str]): A set of English stopwords.
        stemmer (SnowballStemmer): An instance of the SnowballStemmer for English.
        text_cleaning_re (str): A regular expression pattern for text cleaning.
    """

    def __init__(self):
        """
        Initializes the TextPreprocessor with stopwords, a stemmer, 
        and a text cleaning regex pattern.
        """
        self.stop_words: Set[str] = set(stopwords.words('english'))
        self.stemmer: SnowballStemmer = SnowballStemmer('english')
        self.text_cleaning_re: str = r"@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

    def preprocess(self, text: str, stem: bool = False) -> str:
        """
        Preprocesses the input text by cleaning, tokenizing, removing stopwords, 
        and optionally applying stemming.

        Args:
            text (str): The input text to be preprocessed.
            stem (bool): A flag indicating whether to apply stemming.

        Returns:
            str: The preprocessed text.
        """
        # Clean the text
        cleaned_text = re.sub(self.text_cleaning_re, ' ', text.lower()).strip()
        
        # Tokenize and remove stopwords, apply stemming if specified
        tokens = [
            self.stemmer.stem(token) if stem else token
            for token in cleaned_text.split() if token not in self.stop_words
        ]
        
        # Join tokens back into a single string
        return " ".join(tokens)
