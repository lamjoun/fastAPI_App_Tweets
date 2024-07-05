import sys
import json
import requests
from typing import Dict


def get_input_data(tweet_text: str) -> Dict[str, str]:
    """Get the input data for the test based on the provided tweet text."""
    return {"text": tweet_text}


def main() -> None:
    """Main function to test the sentiment prediction endpoint."""
    if len(sys.argv) < 2:
        print('Usage: python mon_script.py "je suis un tweet"')
        sys.exit(1)

    tweet_text = sys.argv[1]
    url = "http://localhost:8000/predict"
    input_data = get_input_data(tweet_text)

    response = requests.post(
        url, json=input_data, headers={"Content-Type": "application/json"}
    )
    # print("response.text= ", response.text)

    # Check the sentiment response
    try:
        response_data = response.json()
        sentiment = response_data.get("sentiment", "Unknown")
        print(f"The sentiment of the tweet is: {sentiment}")
    except json.JSONDecodeError:
        print("Failed to parse response JSON.")
        print("response.text= ", response.text)


if __name__ == "__main__":
    main()
