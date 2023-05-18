import json, os, connexion, re, glob
from flask import Flask, request, jsonify
from google.cloud import bigquery
from google.oauth2 import service_account
from json import loads, dumps
from decimal import *

# BigQuery client setup
json_string = os.environ.get('API_TOKEN')
json_file = json.loads(json_string)
credentials = service_account.Credentials.from_service_account_info(json_file)
client = bigquery.Client(credentials=credentials)
table_name = os.environ.get("TABLE_NAME")

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    response = app.response_class(
        response="OK",
        status=200,
    )
    return response

where_params = {
    "origin_airport_id": ("OriginAirportID", "="), 
    "dest_airport_id": ("DestAirportID", "="),
    "start-date": ("FlightDate", ">="),
    "end-date": ("FlightDate", "<="),
}

@app.route("/airlines/rank", methods=['GET'])
def get_airlines_rank():

    # Get args
    args = request.args

    if not args:
        return "Where args", 404
    
    # Start query
    query_elems = [f"""
        SELECT Airline as airline,
        Operating_Airline as airline_code,
        COUNT(Airline) as num_flights, 
        COUNT(CASE WHEN Cancelled THEN 1 END) as num_cancelled, 
        COUNT(CASE WHEN Diverted THEN 1 END) as num_diverted,
        CAST(COUNT(CASE WHEN Cancelled THEN 1 END) AS DECIMAL) / COUNT(Airline) as ratio_cancelled,
        CAST(COUNT(CASE WHEN Diverted THEN 1 END) AS DECIMAL) / COUNT(Airline) as ratio_diverted,
        
        FROM {table_name}"""]
    
    # Check for where params
    where_and = "WHERE"
    for param in where_params.keys():
        if param in args:
            param_val = args[param] if args[param].isnumeric() else f'"{args[param]}"'
            column_val, arithmetic_val = where_params[param]
            query_elems.append(f"{where_and} {column_val} {arithmetic_val} {param_val}")
            where_and = "AND"

    # Finish query
    query_elems.append("GROUP BY Airline, Operating_Airline")
    if "limit" in args:
        limit = args["limit"]
        query_elems.append(f"LIMIT {limit}")

    # Setup and execute query
    query = " ".join(query_elems)
    query_job = client.query(query)
    df = query_job.result().to_dataframe()

    # Rank
    cancellation_weight = int(args["cancellation_weight"]) / 100
    diversion_weight = int(args["diversion_weight"]) / 100

    ranking = []
    for index, row in df.iterrows():
        ratio_cancelled = row["ratio_cancelled"]
        ratio_diverted = row["ratio_cancelled"]

        rank = (1-ratio_cancelled) * Decimal(cancellation_weight) + (1-ratio_diverted) * Decimal(diversion_weight)
        ranking.append(rank)

    df["ranking"] = ranking

    sorted_df = df.sort_values(by=['ranking'], ascending=False)

    # Add ranking number
    ranking_index = []
    for index, row in df.iterrows():
        ranking_index.append(index+1)

    sorted_df["ranking_index"] = ranking_index

    # If we only want one airline
    if "airline_code" in args:
        sorted_df = sorted_df.loc[df["airline_code"] == args["airline_code"]]

    result = sorted_df.to_json(orient="records")
    parsed = loads(result)
    #json = dumps(parsed, indent=4)

    parsed.sort(key=lambda x: x["ranking_index"])
    return parsed


def flatten_dict(dd, separator='_', prefix=''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }

def represents_int(s):
        try: 
            int(s)
        except ValueError:
            return False
        else:
            return True

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')