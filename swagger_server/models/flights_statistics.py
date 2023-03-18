# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FlightsStatistics(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, total_flights: int=None, average_delay: float=None, max_delay: int=None, cancellation_percentage: float=None, diversion_percentage: float=None):  # noqa: E501
        """FlightsStatistics - a model defined in Swagger

        :param total_flights: The total_flights of this FlightsStatistics.  # noqa: E501
        :type total_flights: int
        :param average_delay: The average_delay of this FlightsStatistics.  # noqa: E501
        :type average_delay: float
        :param max_delay: The max_delay of this FlightsStatistics.  # noqa: E501
        :type max_delay: int
        :param cancellation_percentage: The cancellation_percentage of this FlightsStatistics.  # noqa: E501
        :type cancellation_percentage: float
        :param diversion_percentage: The diversion_percentage of this FlightsStatistics.  # noqa: E501
        :type diversion_percentage: float
        """
        self.swagger_types = {
            'total_flights': int,
            'average_delay': float,
            'max_delay': int,
            'cancellation_percentage': float,
            'diversion_percentage': float
        }

        self.attribute_map = {
            'total_flights': 'total_flights',
            'average_delay': 'average_delay',
            'max_delay': 'max_delay',
            'cancellation_percentage': 'cancellation_percentage',
            'diversion_percentage': 'diversion_percentage'
        }
        self._total_flights = total_flights
        self._average_delay = average_delay
        self._max_delay = max_delay
        self._cancellation_percentage = cancellation_percentage
        self._diversion_percentage = diversion_percentage

    @classmethod
    def from_dict(cls, dikt) -> 'FlightsStatistics':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlightsStatistics of this FlightsStatistics.  # noqa: E501
        :rtype: FlightsStatistics
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total_flights(self) -> int:
        """Gets the total_flights of this FlightsStatistics.


        :return: The total_flights of this FlightsStatistics.
        :rtype: int
        """
        return self._total_flights

    @total_flights.setter
    def total_flights(self, total_flights: int):
        """Sets the total_flights of this FlightsStatistics.


        :param total_flights: The total_flights of this FlightsStatistics.
        :type total_flights: int
        """

        self._total_flights = total_flights

    @property
    def average_delay(self) -> float:
        """Gets the average_delay of this FlightsStatistics.


        :return: The average_delay of this FlightsStatistics.
        :rtype: float
        """
        return self._average_delay

    @average_delay.setter
    def average_delay(self, average_delay: float):
        """Sets the average_delay of this FlightsStatistics.


        :param average_delay: The average_delay of this FlightsStatistics.
        :type average_delay: float
        """

        self._average_delay = average_delay

    @property
    def max_delay(self) -> int:
        """Gets the max_delay of this FlightsStatistics.


        :return: The max_delay of this FlightsStatistics.
        :rtype: int
        """
        return self._max_delay

    @max_delay.setter
    def max_delay(self, max_delay: int):
        """Sets the max_delay of this FlightsStatistics.


        :param max_delay: The max_delay of this FlightsStatistics.
        :type max_delay: int
        """

        self._max_delay = max_delay

    @property
    def cancellation_percentage(self) -> float:
        """Gets the cancellation_percentage of this FlightsStatistics.


        :return: The cancellation_percentage of this FlightsStatistics.
        :rtype: float
        """
        return self._cancellation_percentage

    @cancellation_percentage.setter
    def cancellation_percentage(self, cancellation_percentage: float):
        """Sets the cancellation_percentage of this FlightsStatistics.


        :param cancellation_percentage: The cancellation_percentage of this FlightsStatistics.
        :type cancellation_percentage: float
        """

        self._cancellation_percentage = cancellation_percentage

    @property
    def diversion_percentage(self) -> float:
        """Gets the diversion_percentage of this FlightsStatistics.


        :return: The diversion_percentage of this FlightsStatistics.
        :rtype: float
        """
        return self._diversion_percentage

    @diversion_percentage.setter
    def diversion_percentage(self, diversion_percentage: float):
        """Sets the diversion_percentage of this FlightsStatistics.


        :param diversion_percentage: The diversion_percentage of this FlightsStatistics.
        :type diversion_percentage: float
        """

        self._diversion_percentage = diversion_percentage
