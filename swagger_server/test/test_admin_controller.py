# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.flight import Flight  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminController(BaseTestCase):
    """AdminController integration test stubs"""

    def test_delete_flight(self):
        """Test case for delete_flight

        Delete an existing flight
        """
        response = self.client.open(
            '/admin/flights/{flight-number}'.format(flight_number=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_flight(self):
        """Test case for post_flight

        Add a new flight
        """
        body = Flight()
        response = self.client.open(
            '/admin/flights',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_flight(self):
        """Test case for put_flight

        Update an existing flight
        """
        body = Flight()
        response = self.client.open(
            '/admin/flights/{flight-number}'.format(flight_number=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
