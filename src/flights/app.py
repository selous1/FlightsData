from google.cloud import bigquery
from google.oauth2 import service_account
from flask import Flask, request, abort
from flask_restful import reqparse

# BigQuery client setup
credentials = service_account.Credentials.from_service_account_file("key.json")
client = bigquery.Client(credentials=credentials)

app = Flask(__name__)

param_to_column = {
    "airline-code": ("Operating_Airline", "="), 
    "origin-airport-id": ("OriginAirportID", "="), 
    "dest-airport-id": ("DestAirportID", "="),
    "start-date": ("FlightDate", ">="),
    "end-date": ("FlightDate", "<="),
}

@app.route("/flights/statistics")
def get_flight_statistics():
    args = request.args
    
    if not args:
        return "Where args", 404

    query_elems = ["SELECT * FROM cn54392dataset.flight_table"]
    where_and = "WHERE"

    for param in param_to_column.keys():
        if param in args:
            param_val = args[param] if args[param].isnumeric() else f'"{args[param]}"'
            column_val, arithmetic_val = param_to_column[param]
            query_elems.append(f"{where_and} {column_val} {arithmetic_val} {param_val}")
            where_and = "AND"
    

    query = " ".join(query_elems)

    query_job = client.query(query)

    result = query_job.result().to_dataframe()

    total_flights = len(result.index)
    cancellation_per = result["Cancelled"].value_counts(normalize=True).get(True, 0) * 100
    diversion_per = result["Diverted"].value_counts(normalize=True).get(True, 0) * 100
    max_dep_delay = result["DepDelayMinutes"].max()
    average_dep_delay = result["DepDelayMinutes"].mean()
    max_arr_delay = result["ArrDelayMinutes"].max()
    average_arr_delay = result["ArrDelayMinutes"].mean()
    
    print(query)

    return {
        "total_flights": total_flights,
        "cancellation_percentage": cancellation_per,
        "diversion_percentage": diversion_per,
        "max_dep_delay": max_dep_delay,
        "average_dep_delay": average_dep_delay,
        "max_arr_delay": max_arr_delay,
        "average_arr_delay": average_arr_delay
    }


flight_get_params = {
    "flight-number": ("Flight_Number_Operating_Airline", "="),
    "origin-airport-id": ("OriginAirportID", "="),
    "dest-airport-id": ("DestAirportID", "="),
    "flight-date": ("FlightDate", "="),
    "airline-code": ("Operating_Airline", "="), 
}

@app.route("/flights")
def get_flight():
    args = request.args

    # Check if all params are present in query
    if all(key in args for key in flight_get_params.keys()):

        query_elems = ["SELECT * FROM cn54392dataset.flight_table"]
        where_and = "WHERE"

        for param in flight_get_params.keys():
            param_val = args[param] if args[param].isnumeric() else f'"{args[param]}"'
            column_val, arithmetic_val = flight_get_params[param]
            query_elems.append(f"{where_and} {column_val} {arithmetic_val} {param_val}")
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
    
    abort(400, "Missing query parameters")

if __name__ == "__main__":
    app.run(debug=True)