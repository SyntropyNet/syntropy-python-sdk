# coding: utf-8

"""
    syntropy-auth-service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AuthErrorResponseV1Errors(object):
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
    swagger_types = {"message": "str", "_property": "str", "name": "str"}

    attribute_map = {"message": "message", "_property": "property", "name": "name"}

    def __init__(self, message=None, _property=None, name=None):  # noqa: E501
        """AuthErrorResponseV1Errors - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self.__property = None
        self._name = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if _property is not None:
            self._property = _property
        if name is not None:
            self.name = name

    @property
    def message(self):
        """Gets the message of this AuthErrorResponseV1Errors.  # noqa: E501


        :return: The message of this AuthErrorResponseV1Errors.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AuthErrorResponseV1Errors.


        :param message: The message of this AuthErrorResponseV1Errors.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def _property(self):
        """Gets the _property of this AuthErrorResponseV1Errors.  # noqa: E501


        :return: The _property of this AuthErrorResponseV1Errors.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this AuthErrorResponseV1Errors.


        :param _property: The _property of this AuthErrorResponseV1Errors.  # noqa: E501
        :type: str
        """

        self.__property = _property

    @property
    def name(self):
        """Gets the name of this AuthErrorResponseV1Errors.  # noqa: E501


        :return: The name of this AuthErrorResponseV1Errors.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthErrorResponseV1Errors.


        :param name: The name of this AuthErrorResponseV1Errors.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(AuthErrorResponseV1Errors, dict):
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
        if not isinstance(other, AuthErrorResponseV1Errors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
