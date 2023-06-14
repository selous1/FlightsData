import pytest
from unittest.mock import MagicMock
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_airline(client):
    # Mock the BigQuery client and its query result
    mock_query_result = {
        "Airline": "Test Airline",
        "Operating_Airline": "TEST",
    }
    mock_query_job = MagicMock()
    mock_query_job.result().to_dataframe().iloc[0].to_dict.return_value = mock_query_result
    mock_client = MagicMock()
    mock_client.query.return_value = mock_query_job
    app.config['client'] = mock_client

    # Mock the gRPC client and its response
    mock_stub = MagicMock()
    mock_stub.getNumberFlights.return_value.numberFlights = 10
    app.config['stub'] = mock_stub

    response = client.get('/airlines/TEST')

    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Test Airline'
    assert data['code'] == 'TEST'
    assert data['number_of_flights'] == 10

def test_metrics(client):
    response = client.get('/metrics')
    assert response.status_code == 200