import connexion
import six

from swagger_server.models.airline import Airline  # noqa: E501
from swagger_server.models.airline_rank import AirlineRank  # noqa: E501
from swagger_server import util
from google.cloud import bigquery
from collections import Counter
from decimal import Decimal
import os, json


def get_airline_by_code(airline_code):  # noqa: E501
    """Obtain airline data by airline code

    Obtain airline data given an airline code # noqa: E501

    :param airline_code: Unique carrier code of the airline to return
    :type airline_code: str

    :rtype: Airline
    """
    return 'do some magic!'

# TODO: All parameters below diversion weight need to be clarified
def get_airline_ranks(limit=None, cancellation_weight=0, diversion_weight=0, delay_weight=0, 
                      airline_code=None, origin_airport_id=None, dest_airport_id=None, start_date=None, end_date=None):  # noqa: E501
    """Obtain airline ranks

    Obtain airline ranks, given weights and specifications for calculating it # noqa: E501

    :param limit: Limit the number of results
    :type limit: int
    :param cancellation_weight: Weight of cancellations in calculating the airline rank
    :type cancellation_weight: int
    :param diversion_weight: Weight of diversions in calculating the airline rank
    :type diversion_weight: int
    :param delay_weight: Weight of delays in calculating the airline rank
    :type delay_weight: int
    :param airline_code: Rank the given airline
    :type airline_code: str
    :param origin_airport_id: Rank airlines using flight data from this origin airport
    :type origin_airport_id: int
    :param dest_airport_id: Rank airlines using flight data from this destination airport
    :type dest_airport_id: int
    :param start_date: Rank airlines using flight data after the given date
    :type start_date: int
    :param end_date: Rank airlines using flight data before the given date
    :type end_date: int

    :rtype: List[AirlineRank]
    """

    # get data from bigquery (bucket)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cnproject-381016-a92327017fa2.json"
    client = bigquery.Client()

    table_name = "cnproject-381016.cn54392dataset.flight_table"

    # Airlines to list of dictionaries
    # airline, num_flights, num_cancelled, num_diverted, ratio_cancelled, ratio_diverted
    query_airlines = f"""SELECT Airline as airline,
                         Operating_Airline as airline_code,
                         COUNT(Airline) as num_flights, 
                         COUNT(CASE WHEN Cancelled THEN 1 END) as num_cancelled, 
                         COUNT(CASE WHEN Diverted THEN 1 END) as num_diverted,
                         CAST(COUNT(CASE WHEN Cancelled THEN 1 END) AS DECIMAL) / COUNT(Airline) as ratio_cancelled,
                         CAST(COUNT(CASE WHEN Diverted THEN 1 END) AS DECIMAL) / COUNT(Airline) as ratio_diverted,
       
                         FROM {table_name} 
                         GROUP BY Airline, Operating_Airline"""

    query_job = client.query(query_airlines)
    airlines_dicts = [dict(row) for row in query_job]

    # rank

    cancellation_weight = cancellation_weight / 100
    diversion_weight = diversion_weight / 100

    for airline in airlines_dicts:
        ratio_cancelled = airline["ratio_cancelled"]
        ratio_diverted = airline["ratio_diverted"]

        airline["ranking_index"] = (1-ratio_cancelled) * Decimal(cancellation_weight) + (1-ratio_diverted) * Decimal(diversion_weight)

    sorted_airlines = __sort_by__(airlines_dicts, "ranking_index", True, limit)

    if airline_code != None:
        return __get_ranking__(sorted_airlines, airline_code)


    """ for airline in new_list:
        print(str(airline["airline"]) + " " + str(airline["ratio_cancelled"]) 
              + " " + str(airline["ratio_diverted"]) + " " + str(airline["ranking_index"])) """

    return sorted_airlines

def __find_by__(dict_list, key, value):
    return next(item for item in dict_list if item[key] == value)

def __sort_by__(dict_list, key, in_reverse, limit=None):
    list = sorted(dict_list, key=lambda d: d[key], reverse=in_reverse)
    if limit != None: 
        list = list[0:limit]
    return list

def __get_ranking__(dict_list, airline_code):
    return next((index+1 for (index, d) in enumerate(dict_list) if d["airline_code"] == airline_code), "No airline matching that code")