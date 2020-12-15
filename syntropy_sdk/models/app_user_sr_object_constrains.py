# coding: utf-8

"""
    syntropy-controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AppUserSrObjectConstrains(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "latency_max": "float",
        "jitter_max": "float",
        "price_max": "float",
        "bandwidth_min": "float",
    }

    attribute_map = {
        "latency_max": "latency_max",
        "jitter_max": "jitter_max",
        "price_max": "price_max",
        "bandwidth_min": "bandwidth_min",
    }

    def __init__(
        self, latency_max=None, jitter_max=None, price_max=None, bandwidth_min=None
    ):  # noqa: E501
        """AppUserSrObjectConstrains - a model defined in Swagger"""  # noqa: E501
        self._latency_max = None
        self._jitter_max = None
        self._price_max = None
        self._bandwidth_min = None
        self.discriminator = None
        if latency_max is not None:
            self.latency_max = latency_max
        if jitter_max is not None:
            self.jitter_max = jitter_max
        if price_max is not None:
            self.price_max = price_max
        if bandwidth_min is not None:
            self.bandwidth_min = bandwidth_min

    @property
    def latency_max(self):
        """Gets the latency_max of this AppUserSrObjectConstrains.  # noqa: E501


        :return: The latency_max of this AppUserSrObjectConstrains.  # noqa: E501
        :rtype: float
        """
        return self._latency_max

    @latency_max.setter
    def latency_max(self, latency_max):
        """Sets the latency_max of this AppUserSrObjectConstrains.


        :param latency_max: The latency_max of this AppUserSrObjectConstrains.  # noqa: E501
        :type: float
        """

        self._latency_max = latency_max

    @property
    def jitter_max(self):
        """Gets the jitter_max of this AppUserSrObjectConstrains.  # noqa: E501


        :return: The jitter_max of this AppUserSrObjectConstrains.  # noqa: E501
        :rtype: float
        """
        return self._jitter_max

    @jitter_max.setter
    def jitter_max(self, jitter_max):
        """Sets the jitter_max of this AppUserSrObjectConstrains.


        :param jitter_max: The jitter_max of this AppUserSrObjectConstrains.  # noqa: E501
        :type: float
        """

        self._jitter_max = jitter_max

    @property
    def price_max(self):
        """Gets the price_max of this AppUserSrObjectConstrains.  # noqa: E501


        :return: The price_max of this AppUserSrObjectConstrains.  # noqa: E501
        :rtype: float
        """
        return self._price_max

    @price_max.setter
    def price_max(self, price_max):
        """Sets the price_max of this AppUserSrObjectConstrains.


        :param price_max: The price_max of this AppUserSrObjectConstrains.  # noqa: E501
        :type: float
        """

        self._price_max = price_max

    @property
    def bandwidth_min(self):
        """Gets the bandwidth_min of this AppUserSrObjectConstrains.  # noqa: E501


        :return: The bandwidth_min of this AppUserSrObjectConstrains.  # noqa: E501
        :rtype: float
        """
        return self._bandwidth_min

    @bandwidth_min.setter
    def bandwidth_min(self, bandwidth_min):
        """Sets the bandwidth_min of this AppUserSrObjectConstrains.


        :param bandwidth_min: The bandwidth_min of this AppUserSrObjectConstrains.  # noqa: E501
        :type: float
        """

        self._bandwidth_min = bandwidth_min

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(AppUserSrObjectConstrains, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppUserSrObjectConstrains):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
