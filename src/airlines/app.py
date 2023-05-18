from google.cloud import bigquery
from google.oauth2 import service_account
from flask import Flask, request, abort
import glob,json,os

# BigQuery client setup
json_string = os.environ.get('API_TOKEN')
json_file = json.loads(json_string)
credentials = service_account.Credentials.from_service_account_info(json_file)
client = bigquery.Client(credentials=credentials)
table_name = os.environ.get("TABLE_NAME")

# Flask setup
app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    response = app.response_class(
        response="OK",
        status=200,
    )
    return response

@app.route("/airlines/<airline_code>")
def get_airline(airline_code, methods=["GET"]):

    query = f"""
        SELECT * FROM {table_name}
        WHERE Operating_Airline = "{airline_code}"
        LIMIT 1
    """

    query_job = client.query(query)

    result = query_job.result().to_dataframe().iloc[0].to_dict()

    return {
        "name": result["Airline"],
        "code": result["Operating_Airline"],
        "iata": result["IATA_Code_Marketing_Airline"]
    }

@app.route("/", methods=["GET"])
def health_check():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)