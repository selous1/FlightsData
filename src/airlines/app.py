from google.cloud import bigquery
from google.oauth2 import service_account
from flask import Flask, request, abort
from prometheus_client import Counter, generate_latest
import glob
import json
import os
import grpc
import GRPC.GRPC_pb2
import GRPC.GRPC_pb2_grpc


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

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = GRPC.GRPC_pb2.numberFlightsStub(channel)
        response = stub.getNumberFlights(
            GRPC.GRPC_pb2.numberFlightsRequest(airlineCode=airline_code))

    number_of_flights = response.numberFlights

    return {
        "name": result["Airline"],
        "code": result["Operating_Airline"],
        "iata": result["IATA_Code_Marketing_Airline"]
    }


@app.route("/metrics", methods=["GET"])
def metrics():
    return generate_latest()


if __name__ == "__main__":
    app.run(debug=True)
