# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.flight import Flight  # noqa: E501
from swagger_server.models.flight_prediction import FlightPrediction  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFlightsController(BaseTestCase):
    """FlightsController integration test stubs"""

    def test_get_flight_by_number(self):
        """Test case for get_flight_by_number

        Obtain flight data by flight number
        """
        response = self.client.open(
            '/flights/{flight-number}'.format(flight_number=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_flight_forecast(self):
        """Test case for get_flight_forecast

        Obtain a forecast for a future flight
        """
        query_string = [('flight_date', '2013-10-20'),
                        ('airline_code', 'airline_code_example'),
                        ('origin_airport_id', 56),
                        ('dest_airport_id', 56),
                        ('departure_time', 56),
                        ('arrival_time', 56)]
        response = self.client.open(
            '/flights/forecast',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_flights_statistics(self):
        """Test case for get_flights_statistics

        Obtain statistics regarding flights
        """
        query_string = [('limit', 56),
                        ('airline_code', 'airline_code_example'),
                        ('origin_airport_id', 56),
                        ('dest_airport_id', 56),
                        ('start_date', 56),
                        ('end_date', 56)]
        response = self.client.open(
            '/flights/statistics',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
