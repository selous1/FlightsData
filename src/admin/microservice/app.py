import json, os, connexion, re
from flask import Flask, request, jsonify
from google.cloud import bigquery
from flight import Flight  # noqa: E501

# BigQuery client setup
credentials = service_account.Credentials.from_service_account_file("cnproject-381016-a92327017fa2.json")
client = bigquery.Client(credentials=credentials)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():  # noqa: E501
    response = app.response_class(
        response="OK",
        status=200,
    )
    return response

@app.route("/admin/flights", methods=['POST'])
def post_flight():  # noqa: E501
    """Add a new flight

    The admin can add a new flight and its information # noqa: E501

    :param body: Add a new flight
    :type body: dict | bytes

    :rtype: List[Flight]
    """

    body = request.json
    #if connexion.request.is_json:
    #    body = Flight.from_dict(connexion.request.get_json())  # noqa: E501

    flightDict = flatten_dict(body)
    #Columns = 'FlightDate,Flight_Number_Operating_Airline,AirTime,Cancelled,Diverted,Tail_Number,Airline,OriginAirportID,OriginAirportSeqID,DepTime,DepDelayMinutes,DestAirportID,DestAirportSeqID,ArrTime,ArrDelayMinutes'
    
    ColumnsTranslation ={
        'flightDate':'FlightDate',
        'Airline':'Flight_Number_Operating_Airline',
        'flightDuration':'AirTime',
        'cancelled':'Cancelled',
        'diverted':'Diverted',
        'tailNumber':'Tail_Number',
        'airlineCode':'Airline',
        'departure_actual':'DepTime',
        'departure_airportId':'OriginAirportID',
        'departure_delay':'DepDelay',
        'departure_scheduled':'CRSDepTime',
        'arrival_actual':'ArrTime',
        'arrival_airportId':'DestAirportID',
        'arrival_delay':'ArrDelay',
        'arrival_scheduled':'CRSElapsedTime',
        'flightNumber':'Flight_Number_Operating_Airline'
    }

    # Create Set part of the query
    Columns = []
    values = []
    for (col,val) in list(zip(flightDict.keys(),flightDict.values())):
        if re.search("\d{4}-\d{2}-\d{2}",str(val)):
            Columns.append("FlightDate,")
            values.append(f"CAST('{val}' AS Date),")
        elif represents_int(val):
            Columns.append(f"{ColumnsTranslation[col]},")
            values.append(f"{val},")
        else:
            Columns.append(f"{ColumnsTranslation[col]},")
            values.append(f"'{val}',")

    #Values = f"CAST('{values[0]}' AS Date),{values[1]},{values[2]},{values[3]},{values[4]},'{values[5]}','{values[6]}',{values[7]},{values[8]},{values[9]},{values[10]},{values[11]},{values[12]},{values[13]},{values[14]}"
    query = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('cnproject-381016.cn54392dataset.flight_table', ''.join(Columns)[:-1], ''.join(values)[:-1])

    print(query)
    results = client.query(query)

    response = app.response_class(
        response=json.dumps(body),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/admin/flights/<flight_number>", methods=['DELETE'])
def delete_flight(flight_number):  # noqa: E501
    """Delete an existing flight

    The admin can delete an existing flight by its flight number # noqa: E501

    :param flight_number: Number of the flight to delete
    :type flight_number: int

    :rtype: None
    """

    query = f"DELETE FROM cnproject-381016.cn54392dataset.flight_table WHERE Flight_Number_Operating_Airline = {flight_number};"

    results = client.query(query)

    resp = jsonify(success=True)

    return resp

@app.route("/admin/flights/<flight_number>", methods=['PUT'])
def put_flight(flight_number):  # noqa: E501
    """Update an existing flight

    The admin can update an existing flight&#x27;s information by its flight number # noqa: E501

    :param body: Update an existing flight
    :type body: dict | bytes
    :param flight_number: Number of the flight to update
    :type flight_number: int

    :rtype: List[Flight]
    """
    body = request.json

    #if connexion.request.is_json:
    #    body = Flight.from_dict(connexion.request.get_json())  # noqa: E501

    # Turn body to dict of values and list of columns
    flightDict = flatten_dict(body)
    ColumnsTranslation ={
        'flightDate':'FlightDate',
        'Airline':'Flight_Number_Operating_Airline',
        'flightDuration':'AirTime',
        'cancelled':'Cancelled',
        'diverted':'Diverted',
        'tailNumber':'Tail_Number',
        'airlineCode':'Airline',
        'departure_actual':'DepTime',
        'departure_airportId':'OriginAirportID',
        'departure_delay':'DepDelay',
        'departure_scheduled':'CRSDepTime',
        'arrival_actual':'ArrTime',
        'arrival_airportId':'DestAirportID',
        'arrival_delay':'ArrDelay',
        'arrival_scheduled':'CRSElapsedTime',
        'flightNumber':'Flight_Number_Operating_Airline'
    }

    # Create Set part of the query
    start = ""
    for (col,val) in list(zip(flightDict.keys(),flightDict.values())):
        if re.search("\d{4}-\d{2}-\d{2}",str(val)):
            start += f"FlightDate = CAST('{val}' AS Date),"
        elif represents_int(val):
            start += f"{ColumnsTranslation[col]} = {val},"
        else:
            start += f"{ColumnsTranslation[col]} = '{val}',"

    # Combine the entire query
    query = f"UPDATE cnproject-381016.cn54392dataset.flight_table SET {start[:-1]} WHERE Flight_Number_Operating_Airline = {flight_number}; "

    results = client.query(query)
    print(query)

    response = app.response_class(
        response=json.dumps(flightDict, sort_keys=True, default=str),
        status=200,
        mimetype='application/json'
    )
    
    return response



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