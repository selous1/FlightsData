import connexion
import six

from swagger_server.models.flight import Flight  # noqa: E501
from swagger_server import util
from google.cloud import storage


def delete_flight(flight_number):  # noqa: E501
    """Delete an existing flight

    The admin can delete an existing flight by its flight number # noqa: E501

    :param flight_number: Number of the flight to delete
    :type flight_number: int

    :rtype: None
    """
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
    return 'do some magic!'
