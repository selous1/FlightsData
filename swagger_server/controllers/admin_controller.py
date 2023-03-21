import connexion
import six

from swagger_server.models.flight import Flight  # noqa: E501
from swagger_server import util
from google.cloud import bigquery
import os


def delete_flight(flight_number):  # noqa: E501
    """Delete an existing flight

    The admin can delete an existing flight by its flight number # noqa: E501

    :param flight_number: Number of the flight to delete
    :type flight_number: int

    :rtype: None
    """
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cnproject-381016-a92327017fa2.json"
    client = bigquery.Client()

    query = f"DELETE FROM cnproject-381016.cn54392dataset.flight_table WHERE Flight_Number_Operating_Airline = {flight_number};"

    results = client.query(query)

    return 'do some magic!'


def post_flight(body):  # noqa: E501
    """Add a new flight

    The admin can add a new flight and its information # noqa: E501

    :param body: Add a new flight
    :type body: dict | bytes

    :rtype: List[Flight]
    """
    if connexion.request.is_json:
        body = Flight.from_dict(connexion.request.get_json())  # noqa: E501

    def flatten_dict(dd, separator='_', prefix=''):
        return { prefix + separator + k if prefix else k : v
                 for kk, vv in dd.items()
                 for k, v in flatten_dict(vv, separator, kk).items()
                 } if isinstance(dd, dict) else { prefix : dd }


    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cnproject-381016-a92327017fa2.json"
    client = bigquery.Client()

    flightDict = flatten_dict(body.to_dict())
    Columns = 'FlightDate,Flight_Number_Operating_Airline,AirTime,Cancelled,Diverted,Tail_Number,Airline,OriginAirportID,OriginAirportSeqID,DepTime,DepDelayMinutes,DestAirportID,DestAirportSeqID,ArrTime,ArrDelayMinutes'
    values = list(flightDict.values())

    Values = f"CAST('{values[0]}' AS Date),{values[1]},{values[2]},{values[3]},{values[4]},'{values[5]}','{values[6]}',{values[7]},{values[8]},{values[9]},{values[10]},{values[11]},{values[12]},{values[13]},{values[14]}"
    query = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('cnproject-381016.cn54392dataset.flight_table', Columns, Values)

    results = client.query(query)

    return 'do some magic!'


def put_flight(body, flight_number):  # noqa: E501
    """Update an existing flight

    The admin can update an existing flight&#x27;s information by its flight number # noqa: E501

    :param body: Update an existing flight
    :type body: dict | bytes
    :param flight_number: Number of the flight to update
    :type flight_number: int

    :rtype: List[Flight]
    """
    if connexion.request.is_json:
        body = Flight.from_dict(connexion.request.get_json())  # noqa: E501



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

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cnproject-381016-a92327017fa2.json"
    client = bigquery.Client()


    # Turn body to dict of values and list of columns
    flightDict = flatten_dict(body.to_dict())
    Columns = ["Flight_Number_Operating_Airline","AirTime","Cancelled","Diverted","Tail_Number","Airline","OriginAirportID","OriginAirportSeqID","DepTime","DepDelayMinutes","DestAirportID","DestAirportSeqID","ArrTime","ArrDelayMinutes"]
    values = list(flightDict.values())

    # Create Set part of the query
    start = f"FlightDate = CAST('{values[0]}' AS Date), "
    for val,col in zip(values[1:],Columns):
        if represents_int(val):
            start = start + f"{col} = {val}, "
        else:
            start = start + f"{col} = '{val}', "

    # Combine the entire query
    query = f"UPDATE cnproject-381016.cn54392dataset.flight_table SET {start[:-2]} WHERE Flight_Number_Operating_Airline = {flight_number}; "

    results = client.query(query)
    
    return 'do some magic!'
