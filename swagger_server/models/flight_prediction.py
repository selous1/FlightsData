# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FlightPrediction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cancelling_probability: float=None, diverting_probability: float=None, expected_delay: int=None):  # noqa: E501
        """FlightPrediction - a model defined in Swagger

        :param cancelling_probability: The cancelling_probability of this FlightPrediction.  # noqa: E501
        :type cancelling_probability: float
        :param diverting_probability: The diverting_probability of this FlightPrediction.  # noqa: E501
        :type diverting_probability: float
        :param expected_delay: The expected_delay of this FlightPrediction.  # noqa: E501
        :type expected_delay: int
        """
        self.swagger_types = {
            'cancelling_probability': float,
            'diverting_probability': float,
            'expected_delay': int
        }

        self.attribute_map = {
            'cancelling_probability': 'cancellingProbability',
            'diverting_probability': 'divertingProbability',
            'expected_delay': 'expectedDelay'
        }
        self._cancelling_probability = cancelling_probability
        self._diverting_probability = diverting_probability
        self._expected_delay = expected_delay

    @classmethod
    def from_dict(cls, dikt) -> 'FlightPrediction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlightPrediction of this FlightPrediction.  # noqa: E501
        :rtype: FlightPrediction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cancelling_probability(self) -> float:
        """Gets the cancelling_probability of this FlightPrediction.


        :return: The cancelling_probability of this FlightPrediction.
        :rtype: float
        """
        return self._cancelling_probability

    @cancelling_probability.setter
    def cancelling_probability(self, cancelling_probability: float):
        """Sets the cancelling_probability of this FlightPrediction.


        :param cancelling_probability: The cancelling_probability of this FlightPrediction.
        :type cancelling_probability: float
        """

        self._cancelling_probability = cancelling_probability

    @property
    def diverting_probability(self) -> float:
        """Gets the diverting_probability of this FlightPrediction.


        :return: The diverting_probability of this FlightPrediction.
        :rtype: float
        """
        return self._diverting_probability

    @diverting_probability.setter
    def diverting_probability(self, diverting_probability: float):
        """Sets the diverting_probability of this FlightPrediction.


        :param diverting_probability: The diverting_probability of this FlightPrediction.
        :type diverting_probability: float
        """

        self._diverting_probability = diverting_probability

    @property
    def expected_delay(self) -> int:
        """Gets the expected_delay of this FlightPrediction.


        :return: The expected_delay of this FlightPrediction.
        :rtype: int
        """
        return self._expected_delay

    @expected_delay.setter
    def expected_delay(self, expected_delay: int):
        """Sets the expected_delay of this FlightPrediction.


        :param expected_delay: The expected_delay of this FlightPrediction.
        :type expected_delay: int
        """

        self._expected_delay = expected_delay
