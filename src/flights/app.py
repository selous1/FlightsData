from google.cloud import bigquery
from google.oauth2 import service_account
from flask import Flask, request, abort
from concurrent import futures
import glob
import json
import os
import grpc
from GRPC.GRPC_pb2 import *
from GRPC.GRPC_pb2_grpc import *
import threading

# BigQuery client setup
json_string = os.environ.get('API_TOKEN')
json_file = json.loads(json_string)
credentials = service_account.Credentials.from_service_account_info(json_file)
client = bigquery.Client(credentials=credentials)
table_name = os.environ.get("TABLE_NAME")

# Flask setup
app = Flask(__name__)


# Flight Statistics

flight_statistics_get_params = {
    "airline-code": ("Operating_Airline", "="),
    "origin-airport-id": ("OriginAirportID", "="),
    "dest-airport-id": ("DestAirportID", "="),
    "start-date": ("FlightDate", ">="),
    "end-date": ("FlightDate", "<="),
}


@app.route("/", methods=['GET'])
def root():
    response = app.response_class(
        response="OK",
        status=200,
    )
    return response


@app.route("/flights/statistics", methods=["GET"])
def get_flight_statistics():
    args = request.args

    # Args must have at least one VALID element
    if not args or not any(key in args for key in flight_statistics_get_params.keys()):
        abort(400, "Insert at least one valid query parameter")

    query_elems = [f"SELECT * FROM {table_name}"]
    where_and = "WHERE"

    for param in flight_statistics_get_params.keys():
        if param in args:
            param_val = args[param] if args[param].isnumeric(
            ) else f'"{args[param]}"'
            column_val, arithmetic_val = flight_statistics_get_params[param]
            query_elems.append(
                f"{where_and} {column_val} {arithmetic_val} {param_val}")
            where_and = "AND"

    query = " ".join(query_elems)

    query_job = client.query(query)

    result = query_job.result().to_dataframe()

    total_flights = len(result.index)
    cancellation_per = result["Cancelled"].value_counts(
        normalize=True).get(True, 0) * 100
    diversion_per = result["Diverted"].value_counts(
        normalize=True).get(True, 0) * 100
    max_dep_delay = result["DepDelayMinutes"].max()
    average_dep_delay = result["DepDelayMinutes"].mean()
    max_arr_delay = result["ArrDelayMinutes"].max()
    average_arr_delay = result["ArrDelayMinutes"].mean()

    return {
        "total_flights": total_flights,
        "cancellation_percentage": cancellation_per,
        "diversion_percentage": diversion_per,
        "max_dep_delay": max_dep_delay,
        "average_dep_delay": average_dep_delay,
        "max_arr_delay": max_arr_delay,
        "average_arr_delay": average_arr_delay
    }

# Flight Getter


flight_get_params = {
    "flight-number": ("Flight_Number_Operating_Airline", "="),
    "origin-airport-id": ("OriginAirportID", "="),
    "dest-airport-id": ("DestAirportID", "="),
    "flight-date": ("FlightDate", "="),
    "airline-code": ("Operating_Airline", "="),
}


@app.route("/flights", methods=["GET"])
def get_flight():
    args = request.args

    # Check if all params are present in query
    if not all(key in args for key in flight_get_params.keys()):
        abort(400, "Missing query parameters")

    query_elems = [f"SELECT * FROM {table_name}"]
    where_and = "WHERE"

    for param in flight_get_params.keys():
        param_val = args[param] if args[param].isnumeric(
        ) else f'"{args[param]}"'
        column_val, arithmetic_val = flight_get_params[param]
        query_elems.append(
            f"{where_and} {column_val} {arithmetic_val} {param_val}")
        where_and = "AND"

    query = " ".join(query_elems)

    query_job = client.query(query)

    result = query_job.result().to_dataframe().iloc[0].to_dict()

    return {
        "flightDate": result["FlightDate"],
        "flightNumber": result["Flight_Number_Operating_Airline"],
        "flightDuration": result["ActualElapsedTime"],
        "cancelled": result["Cancelled"],
        "diverted": result["Diverted"],
        "tailNumber": result["Tail_Number"],
        "airlineCode": result["Operating_Airline"],
        "departure": {
            "airportId": result["DestAirportID"],
            "scheduled": result["CRSArrTime"],
            "actual": result["ArrTime"],
            "delay": result["ArrDelay"]
        },
        "arrival": {
            "airportId": result["OriginAirportID"],
            "scheduled": result["CRSDepTime"],
            "actual": result["DepTime"],
            "delay": result["DepDelay"]
        },
    }

class flightNumberService(numberFlightsServicer):

    def get_flight(self, request, context):

        airline_code = request.airlineCode

        query = f"SELECT COUNT(*) AS row_count FROM {table_name} WHERE Operating_Airline = {airline_code}"

        query_job = client.query(query)

        result = query_job.result()

        return result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_numberFlightsServicer_to_server(flightNumberService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    grpc_server_thread = threading.Thread(target=serve)
    grpc_server_thread.start()
    app.run(port=5000, debug=True)
