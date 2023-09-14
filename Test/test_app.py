import pytest
import os
from pathlib import Path
import sys
sys.path.append([str(Path(os.getcwd()).parent), str(Path(os.getcwd()))])
from flask_app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict(client):
    # Sample input data for testing
    input_data = {
        "feature1": 17,
        "feature2": 17700,
        # Add more input features as needed
    }

    # Send a POST request to the /predict route with the sample input data
    response = client.post('/predict', json=input_data)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse the response JSON
    response_data = json.loads(response.data)

    # Check if the response contains the "predictions" key
    assert "predictions" in response_data

    # You can add more specific assertions here based on your app's behavior
    # For example, check if the "predictions" value matches your expected output

    # Example assertion (modify as needed)
    assert response_data["predictions"] in ["not likely to purchase", "highly likely to purchase"]

    # You can add more test cases with different input data and expected outputs as needed