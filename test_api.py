import sys
import json
import requests
from typing import Dict

def get_input_data(test_positive_sentiment: bool) -> Dict[str, str]:
    """
    Get the input data for the test based on the sentiment type.

    Args:
        test_positive_sentiment (bool): Flag to determine the type of sentiment to test.

    Returns:
        Dict[str, str]: The input data for the test.
    """
    if test_positive_sentiment:
        return {"text": "holla"}
    else:
        return {"text": "nooo danny kicked adam totally going win"}

def main() -> None:
    """
    Main function to test the sentiment prediction endpoint.

    Determines the type of sentiment to test, sends the input data to the prediction endpoint,
    and asserts the response matches the expected sentiment.

    Raises:
        AssertionError: If the response does not match the expected sentiment.
    """
    test_positive_sentiment = True

    try:
        print(sys.argv[1])
        test_positive_sentiment = False
    except IndexError:
        pass

    url = 'http://localhost:8000/predict'
    input_data_test = get_input_data(test_positive_sentiment)
    
    input_json = json.dumps(input_data_test)
    response = requests.post(url, data=input_json)
    print("response.text= ", response.text)
    
    positive_sentiment = '{"sentiment":"Positive"}'
    negative_sentiment = '{"sentiment":"Negative"}'
    
    if test_positive_sentiment:
        assert positive_sentiment == response.text
    else:
        assert negative_sentiment == response.text

if __name__ == "__main__":
    main()
