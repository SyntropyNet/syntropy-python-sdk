# coding: utf-8

"""
    Syntropy network API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@syntropynet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class V1SdnPaths(object):
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
        "sdn3": "list[IdNumber]",
        "sdn2": "list[IdNumber]",
        "sdn1": "list[IdNumber]",
    }

    attribute_map = {"sdn3": "SDN3", "sdn2": "SDN2", "sdn1": "SDN1"}

    def __init__(self, sdn3=None, sdn2=None, sdn1=None):  # noqa: E501
        """V1SdnPaths - a model defined in Swagger"""  # noqa: E501
        self._sdn3 = None
        self._sdn2 = None
        self._sdn1 = None
        self.discriminator = None
        if sdn3 is not None:
            self.sdn3 = sdn3
        if sdn2 is not None:
            self.sdn2 = sdn2
        if sdn1 is not None:
            self.sdn1 = sdn1

    @property
    def sdn3(self):
        """Gets the sdn3 of this V1SdnPaths.  # noqa: E501


        :return: The sdn3 of this V1SdnPaths.  # noqa: E501
        :rtype: list[IdNumber]
        """
        return self._sdn3

    @sdn3.setter
    def sdn3(self, sdn3):
        """Sets the sdn3 of this V1SdnPaths.


        :param sdn3: The sdn3 of this V1SdnPaths.  # noqa: E501
        :type: list[IdNumber]
        """

        self._sdn3 = sdn3

    @property
    def sdn2(self):
        """Gets the sdn2 of this V1SdnPaths.  # noqa: E501


        :return: The sdn2 of this V1SdnPaths.  # noqa: E501
        :rtype: list[IdNumber]
        """
        return self._sdn2

    @sdn2.setter
    def sdn2(self, sdn2):
        """Sets the sdn2 of this V1SdnPaths.


        :param sdn2: The sdn2 of this V1SdnPaths.  # noqa: E501
        :type: list[IdNumber]
        """

        self._sdn2 = sdn2

    @property
    def sdn1(self):
        """Gets the sdn1 of this V1SdnPaths.  # noqa: E501


        :return: The sdn1 of this V1SdnPaths.  # noqa: E501
        :rtype: list[IdNumber]
        """
        return self._sdn1

    @sdn1.setter
    def sdn1(self, sdn1):
        """Sets the sdn1 of this V1SdnPaths.


        :param sdn1: The sdn1 of this V1SdnPaths.  # noqa: E501
        :type: list[IdNumber]
        """

        self._sdn1 = sdn1

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
        if issubclass(V1SdnPaths, dict):
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
        if not isinstance(other, V1SdnPaths):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other