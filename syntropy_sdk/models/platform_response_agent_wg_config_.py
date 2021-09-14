# coding: utf-8

"""
    syntropy-controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PlatformResponseAgentWgConfig_(object):
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
        "data": "AgentWgConfig",
        "errors": "list[PlatformResponseErrorItem]",
    }

    attribute_map = {"data": "data", "errors": "errors"}

    def __init__(self, data=None, errors=None):  # noqa: E501
        """PlatformResponseAgentWgConfig_ - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._errors = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if errors is not None:
            self.errors = errors

    @property
    def data(self):
        """Gets the data of this PlatformResponseAgentWgConfig_.  # noqa: E501


        :return: The data of this PlatformResponseAgentWgConfig_.  # noqa: E501
        :rtype: AgentWgConfig
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PlatformResponseAgentWgConfig_.


        :param data: The data of this PlatformResponseAgentWgConfig_.  # noqa: E501
        :type: AgentWgConfig
        """

        self._data = data

    @property
    def errors(self):
        """Gets the errors of this PlatformResponseAgentWgConfig_.  # noqa: E501


        :return: The errors of this PlatformResponseAgentWgConfig_.  # noqa: E501
        :rtype: list[PlatformResponseErrorItem]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this PlatformResponseAgentWgConfig_.


        :param errors: The errors of this PlatformResponseAgentWgConfig_.  # noqa: E501
        :type: list[PlatformResponseErrorItem]
        """

        self._errors = errors

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
        if issubclass(PlatformResponseAgentWgConfig_, dict):
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
        if not isinstance(other, PlatformResponseAgentWgConfig_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
