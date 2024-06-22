import pandas as pd
import json
import requests

# Load the dataset (example)
# Assuming X is your dataset that contains the code snippets to be tested
X = ["def add(a, b):\n    return a + b"]  # Example data, replace with actual data loading

# Convert dataset to JSON format
json_data = json.dumps({"code": X[0]})  # Sending one code snippet at a time for simplicity

# Define the Flask server URL
url = "http://127.0.0.1:5000"

# Send the request to the Flask server
response = requests.post(url, json=json_data)

# Print the response from the server
print(response.json())
