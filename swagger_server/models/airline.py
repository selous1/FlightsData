# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Airline(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, code: str=None, iata: str=None, icao: str=None):  # noqa: E501
        """Airline - a model defined in Swagger

        :param name: The name of this Airline.  # noqa: E501
        :type name: str
        :param code: The code of this Airline.  # noqa: E501
        :type code: str
        :param iata: The iata of this Airline.  # noqa: E501
        :type iata: str
        :param icao: The icao of this Airline.  # noqa: E501
        :type icao: str
        """
        self.swagger_types = {
            'name': str,
            'code': str,
            'iata': str,
            'icao': str
        }

        self.attribute_map = {
            'name': 'name',
            'code': 'code',
            'iata': 'iata',
            'icao': 'icao'
        }
        self._name = name
        self._code = code
        self._iata = iata
        self._icao = icao

    @classmethod
    def from_dict(cls, dikt) -> 'Airline':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Airline of this Airline.  # noqa: E501
        :rtype: Airline
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Airline.


        :return: The name of this Airline.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Airline.


        :param name: The name of this Airline.
        :type name: str
        """

        self._name = name

    @property
    def code(self) -> str:
        """Gets the code of this Airline.


        :return: The code of this Airline.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this Airline.


        :param code: The code of this Airline.
        :type code: str
        """

        self._code = code

    @property
    def iata(self) -> str:
        """Gets the iata of this Airline.


        :return: The iata of this Airline.
        :rtype: str
        """
        return self._iata

    @iata.setter
    def iata(self, iata: str):
        """Sets the iata of this Airline.


        :param iata: The iata of this Airline.
        :type iata: str
        """

        self._iata = iata

    @property
    def icao(self) -> str:
        """Gets the icao of this Airline.


        :return: The icao of this Airline.
        :rtype: str
        """
        return self._icao

    @icao.setter
    def icao(self, icao: str):
        """Sets the icao of this Airline.


        :param icao: The icao of this Airline.
        :type icao: str
        """

        self._icao = icao