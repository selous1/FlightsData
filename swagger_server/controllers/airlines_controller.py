import connexion
import six

from swagger_server.models.airline import Airline  # noqa: E501
from swagger_server.models.airline_rank import AirlineRank  # noqa: E501
from swagger_server import util
from google.cloud import bigquery
import os


def get_airline_by_code(airline_code):  # noqa: E501
    """Obtain airline data by airline code

    Obtain airline data given an airline code # noqa: E501

    :param airline_code: Unique carrier code of the airline to return
    :type airline_code: str

    :rtype: Airline
    """
    return 'do some magic!'


def get_airline_ranks(limit=None, cancellation_weight=None, diversion_weight=None, delay_weight=None, 
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

    table_name = "cnproject-381016.cn54392dataset.flight_table";

    query = f"SELECT * FROM {table_name}"

    query_job = client.query(query)

    for row in query_job:
        print(row)

    print("oi")

    # rank

    # return
    
    return 'do some magic!'
