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


class TsoaPartialHostGroupObject_(object):
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
    swagger_types = {"host_group_name": "str"}

    attribute_map = {"host_group_name": "host_group_name"}

    def __init__(self, host_group_name=None):  # noqa: E501
        """TsoaPartialHostGroupObject_ - a model defined in Swagger"""  # noqa: E501
        self._host_group_name = None
        self.discriminator = None
        if host_group_name is not None:
            self.host_group_name = host_group_name

    @property
    def host_group_name(self):
        """Gets the host_group_name of this TsoaPartialHostGroupObject_.  # noqa: E501


        :return: The host_group_name of this TsoaPartialHostGroupObject_.  # noqa: E501
        :rtype: str
        """
        return self._host_group_name

    @host_group_name.setter
    def host_group_name(self, host_group_name):
        """Sets the host_group_name of this TsoaPartialHostGroupObject_.


        :param host_group_name: The host_group_name of this TsoaPartialHostGroupObject_.  # noqa: E501
        :type: str
        """

        self._host_group_name = host_group_name

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
        if issubclass(TsoaPartialHostGroupObject_, dict):
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
        if not isinstance(other, TsoaPartialHostGroupObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
