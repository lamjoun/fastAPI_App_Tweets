from src.text_preprocessing import TextPreprocessor

def test_preprocess() -> None:
    """
    Test the preprocess method of the TextPreprocessor class.

    This function creates an instance of TextPreprocessor, processes a sample text,
    and asserts that the processed text matches the expected output.

    Raises:
        AssertionError: If the processed text does not match the expected output.
    """
    preprocessor = TextPreprocessor()
    text = "yeeeees freaking!!$$$$$ handsome @@@@@@@ wait till new moon night museum 2!"
    result = preprocessor.preprocess(text)
    print(result)
    expected_text="yeeeees freaking handsome wait till new moon night museum 2"
    assert result == expected_text, f"Expected {expected_text}, but got {result}"

if __name__ == "__main__":
    test_preprocess()
