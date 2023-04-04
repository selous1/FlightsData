from google.cloud import bigquery
from google.oauth2 import service_account
from flask import Flask, request, abort

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


if __name__ == "__main__":
    app.run(debug=True)