import sys
import json
import requests

test_positive_sentiment = True

try:
    print(sys.argv[1])
    test_positive_sentiment = False 
except Exception as e:
    pass
    

url = 'http://localhost:8000/predict'

input_data_test = {
    "text": "it's a loveling%%!!!!!"
}

if test_positive_sentiment:
    input_data_test = {"text": "holla"}
else:
    input_data_test = {"text": "nooo danny kicked adam totally going win"}

input_json = json.dumps(input_data_test)
response = requests.post(url, data=input_json)
print("response.text= ",response.text)
positive_sentiment = '{' + "\"sentiment\":\"Positive\"}"
negative_sentiment = '{' + "\"sentiment\":\"Negative\"}"

if test_positive_sentiment:
    assert positive_sentiment == str(response.text)
else: 
    assert negative_sentiment == str(response.text)  