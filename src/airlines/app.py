import json, os, grpc, pytest
from google.cloud import bigquery
from google.oauth2 import service_account
from flask import Flask, request, abort
from prometheus_client import Counter, generate_latest, Summary
import GRPC_pb2
import GRPC_pb2_grpc
from kubernetes import client, config
import kubernetes
from unittest.mock import MagicMock

# test webhook

# BigQuery client setup
json_string = os.environ.get('API_TOKEN')
json_file = json.loads(json_string)
credentials = service_account.Credentials.from_service_account_info(json_file)
client = bigquery.Client(credentials=credentials)
table_name = os.environ.get("TABLE_NAME")

# Flask setup
app = Flask(__name__)

# Monitoring variables
request_counter = Counter('airlines_requests_total',
                          'Total number of requests received in the airlines microservice')
request_time = Summary('airlines_processing_seconds',
                          'Time spent processing request')

@request_time.time()
@app.route("/airlines/<airline_code>")
def get_airline(airline_code, methods=["GET"]):
    request_counter.inc()

    query = f"""
        SELECT * FROM {table_name}
        WHERE Operating_Airline = "{airline_code}"
        LIMIT 1
    """

    query_job = client.query(query)

    result = query_job.result().to_dataframe().iloc[0].to_dict()

    config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()
    service = v1.read_namespaced_service('flight-s', "default")
    ip = service.spec.cluster_ip
    with grpc.insecure_channel(f'{ip}:50051') as channel:
        stub = GRPC_pb2_grpc.numberFlightsStub(channel)
        response = stub.getNumberFlights(GRPC_pb2.numberFlightsRequest(airlineCode=airline_code))
    number_of_flights = response.numberFlights

    return {
        "name": result["Airline"],
        "code": result["Operating_Airline"],
        #"iata_code": result["IATA_Code_Marketing_Airline"],
        "number_of_flights": number_of_flights
    }


@app.route("/metrics", methods=["GET"])
def metrics():
    return generate_latest()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")