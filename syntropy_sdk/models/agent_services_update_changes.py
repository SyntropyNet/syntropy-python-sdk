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


class AgentServicesUpdateChanges(object):
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
    swagger_types = {"agent_service_subnet_id": "IdNumber", "is_enabled": "bool"}

    attribute_map = {
        "agent_service_subnet_id": "agent_service_subnet_id",
        "is_enabled": "is_enabled",
    }

    def __init__(self, agent_service_subnet_id=None, is_enabled=None):  # noqa: E501
        """AgentServicesUpdateChanges - a model defined in Swagger"""  # noqa: E501
        self._agent_service_subnet_id = None
        self._is_enabled = None
        self.discriminator = None
        if agent_service_subnet_id is not None:
            self.agent_service_subnet_id = agent_service_subnet_id
        if is_enabled is not None:
            self.is_enabled = is_enabled

    @property
    def agent_service_subnet_id(self):
        """Gets the agent_service_subnet_id of this AgentServicesUpdateChanges.  # noqa: E501


        :return: The agent_service_subnet_id of this AgentServicesUpdateChanges.  # noqa: E501
        :rtype: IdNumber
        """
        return self._agent_service_subnet_id

    @agent_service_subnet_id.setter
    def agent_service_subnet_id(self, agent_service_subnet_id):
        """Sets the agent_service_subnet_id of this AgentServicesUpdateChanges.


        :param agent_service_subnet_id: The agent_service_subnet_id of this AgentServicesUpdateChanges.  # noqa: E501
        :type: IdNumber
        """

        self._agent_service_subnet_id = agent_service_subnet_id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this AgentServicesUpdateChanges.  # noqa: E501


        :return: The is_enabled of this AgentServicesUpdateChanges.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this AgentServicesUpdateChanges.


        :param is_enabled: The is_enabled of this AgentServicesUpdateChanges.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

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
        if issubclass(AgentServicesUpdateChanges, dict):
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
        if not isinstance(other, AgentServicesUpdateChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other