from google.cloud import bigquery
from google.oauth2 import service_account
from flask import Flask, request, abort

# BigQuery client setup
credentials = service_account.Credentials.from_service_account_file("key.json")
client = bigquery.Client(credentials=credentials)

# Flask setup
app = Flask(__name__)

@app.route("/airlines/<airline_code>")
def get_airline(airline_code, methods=["GET"]):
    query = f"""
        SELECT * FROM cn54392dataset.flight_table
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