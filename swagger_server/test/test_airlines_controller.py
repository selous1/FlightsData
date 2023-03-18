# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.airline import Airline  # noqa: E501
from swagger_server.models.airline_rank import AirlineRank  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAirlinesController(BaseTestCase):
    """AirlinesController integration test stubs"""

    def test_get_airline_by_code(self):
        """Test case for get_airline_by_code

        Obtain airline data by airline code
        """
        response = self.client.open(
            '/airlines/{airline-code}'.format(airline_code='airline_code_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_airline_ranks(self):
        """Test case for get_airline_ranks

        Obtain airline ranks
        """
        query_string = [('limit', 56),
                        ('cancellation_weight', 100),
                        ('diversion_weight', 100),
                        ('delay_weight', 100),
                        ('airline_code', 'airline_code_example'),
                        ('origin_airport_id', 56),
                        ('dest_airport_id', 56),
                        ('start_date', 56),
                        ('end_date', 56)]
        response = self.client.open(
            '/airlines/rank',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
