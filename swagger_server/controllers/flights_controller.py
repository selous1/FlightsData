import connexion
import six

from swagger_server.models.flight import Flight  # noqa: E501
from swagger_server.models.flight_prediction import FlightPrediction  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def get_flight_by_number(flight_number):  # noqa: E501
    """Obtain flight data by flight number

    Obtain flight data given a flight number # noqa: E501

    :param flight_number: Number of the flight to return
    :type flight_number: int

    :rtype: Flight
    """
    return 'do some magic!'


def get_flight_forecast(flight_date, airline_code, origin_airport_id, dest_airport_id, departure_time, arrival_time):  # noqa: E501
    """Obtain a forecast for a future flight

    Obtain predictions for a future flight, given a date and other details # noqa: E501

    :param flight_date: Date for future flight
    :type flight_date: str
    :param airline_code: Airline for future flight
    :type airline_code: str
    :param origin_airport_id: Origin airport for future flight
    :type origin_airport_id: int
    :param dest_airport_id: Destination airport for future flight
    :type dest_airport_id: int
    :param departure_time: Departure time for future flight
    :type departure_time: int
    :param arrival_time: Arrival time for future flight
    :type arrival_time: int

    :rtype: FlightPrediction
    """
    flight_date = util.deserialize_date(flight_date)
    return 'do some magic!'


def get_flights_statistics(limit=None, airline_code=None, origin_airport_id=None, dest_airport_id=None, start_date=None, end_date=None):  # noqa: E501
    """Obtain statistics regarding flights

    Obtain flight statistics, given certain criteria. # noqa: E501

    :param limit: Limit the number of results
    :type limit: int
    :param airline_code: Filter results by airlines
    :type airline_code: str
    :param origin_airport_id: Filter results by the origin airport
    :type origin_airport_id: int
    :param dest_airport_id: Filter results by the destination airport
    :type dest_airport_id: int
    :param start_date: Filter results with a flight date after the given date
    :type start_date: int
    :param end_date: Filter results with a flight date before the given date
    :type end_date: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'
