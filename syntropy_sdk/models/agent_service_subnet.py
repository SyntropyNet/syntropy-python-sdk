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


class AgentServiceSubnet(object):
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
        "agent_service_subnet_id": "int",
        "agent_service_subnet_ip": "str",
        "agent_service_subnet_is_active": "bool",
        "agent_service_subnet_is_user_enabled": "bool",
        "agent_service_subnet_is_enabled_by_default": "bool",
    }

    attribute_map = {
        "agent_service_subnet_id": "agent_service_subnet_id",
        "agent_service_subnet_ip": "agent_service_subnet_ip",
        "agent_service_subnet_is_active": "agent_service_subnet_is_active",
        "agent_service_subnet_is_user_enabled": "agent_service_subnet_is_user_enabled",
        "agent_service_subnet_is_enabled_by_default": "agent_service_subnet_is_enabled_by_default",
    }

    def __init__(
        self,
        agent_service_subnet_id=None,
        agent_service_subnet_ip=None,
        agent_service_subnet_is_active=None,
        agent_service_subnet_is_user_enabled=None,
        agent_service_subnet_is_enabled_by_default=None,
    ):  # noqa: E501
        """AgentServiceSubnet - a model defined in Swagger"""  # noqa: E501
        self._agent_service_subnet_id = None
        self._agent_service_subnet_ip = None
        self._agent_service_subnet_is_active = None
        self._agent_service_subnet_is_user_enabled = None
        self._agent_service_subnet_is_enabled_by_default = None
        self.discriminator = None
        self.agent_service_subnet_id = agent_service_subnet_id
        self.agent_service_subnet_ip = agent_service_subnet_ip
        self.agent_service_subnet_is_active = agent_service_subnet_is_active
        self.agent_service_subnet_is_user_enabled = agent_service_subnet_is_user_enabled
        self.agent_service_subnet_is_enabled_by_default = (
            agent_service_subnet_is_enabled_by_default
        )

    @property
    def agent_service_subnet_id(self):
        """Gets the agent_service_subnet_id of this AgentServiceSubnet.  # noqa: E501


        :return: The agent_service_subnet_id of this AgentServiceSubnet.  # noqa: E501
        :rtype: int
        """
        return self._agent_service_subnet_id

    @agent_service_subnet_id.setter
    def agent_service_subnet_id(self, agent_service_subnet_id):
        """Sets the agent_service_subnet_id of this AgentServiceSubnet.


        :param agent_service_subnet_id: The agent_service_subnet_id of this AgentServiceSubnet.  # noqa: E501
        :type: int
        """
        if agent_service_subnet_id is None:
            raise ValueError(
                "Invalid value for `agent_service_subnet_id`, must not be `None`"
            )  # noqa: E501

        self._agent_service_subnet_id = agent_service_subnet_id

    @property
    def agent_service_subnet_ip(self):
        """Gets the agent_service_subnet_ip of this AgentServiceSubnet.  # noqa: E501


        :return: The agent_service_subnet_ip of this AgentServiceSubnet.  # noqa: E501
        :rtype: str
        """
        return self._agent_service_subnet_ip

    @agent_service_subnet_ip.setter
    def agent_service_subnet_ip(self, agent_service_subnet_ip):
        """Sets the agent_service_subnet_ip of this AgentServiceSubnet.


        :param agent_service_subnet_ip: The agent_service_subnet_ip of this AgentServiceSubnet.  # noqa: E501
        :type: str
        """
        if agent_service_subnet_ip is None:
            raise ValueError(
                "Invalid value for `agent_service_subnet_ip`, must not be `None`"
            )  # noqa: E501

        self._agent_service_subnet_ip = agent_service_subnet_ip

    @property
    def agent_service_subnet_is_active(self):
        """Gets the agent_service_subnet_is_active of this AgentServiceSubnet.  # noqa: E501


        :return: The agent_service_subnet_is_active of this AgentServiceSubnet.  # noqa: E501
        :rtype: bool
        """
        return self._agent_service_subnet_is_active

    @agent_service_subnet_is_active.setter
    def agent_service_subnet_is_active(self, agent_service_subnet_is_active):
        """Sets the agent_service_subnet_is_active of this AgentServiceSubnet.


        :param agent_service_subnet_is_active: The agent_service_subnet_is_active of this AgentServiceSubnet.  # noqa: E501
        :type: bool
        """
        if agent_service_subnet_is_active is None:
            raise ValueError(
                "Invalid value for `agent_service_subnet_is_active`, must not be `None`"
            )  # noqa: E501

        self._agent_service_subnet_is_active = agent_service_subnet_is_active

    @property
    def agent_service_subnet_is_user_enabled(self):
        """Gets the agent_service_subnet_is_user_enabled of this AgentServiceSubnet.  # noqa: E501


        :return: The agent_service_subnet_is_user_enabled of this AgentServiceSubnet.  # noqa: E501
        :rtype: bool
        """
        return self._agent_service_subnet_is_user_enabled

    @agent_service_subnet_is_user_enabled.setter
    def agent_service_subnet_is_user_enabled(
        self, agent_service_subnet_is_user_enabled
    ):
        """Sets the agent_service_subnet_is_user_enabled of this AgentServiceSubnet.


        :param agent_service_subnet_is_user_enabled: The agent_service_subnet_is_user_enabled of this AgentServiceSubnet.  # noqa: E501
        :type: bool
        """
        if agent_service_subnet_is_user_enabled is None:
            raise ValueError(
                "Invalid value for `agent_service_subnet_is_user_enabled`, must not be `None`"
            )  # noqa: E501

        self._agent_service_subnet_is_user_enabled = (
            agent_service_subnet_is_user_enabled
        )

    @property
    def agent_service_subnet_is_enabled_by_default(self):
        """Gets the agent_service_subnet_is_enabled_by_default of this AgentServiceSubnet.  # noqa: E501


        :return: The agent_service_subnet_is_enabled_by_default of this AgentServiceSubnet.  # noqa: E501
        :rtype: bool
        """
        return self._agent_service_subnet_is_enabled_by_default

    @agent_service_subnet_is_enabled_by_default.setter
    def agent_service_subnet_is_enabled_by_default(
        self, agent_service_subnet_is_enabled_by_default
    ):
        """Sets the agent_service_subnet_is_enabled_by_default of this AgentServiceSubnet.


        :param agent_service_subnet_is_enabled_by_default: The agent_service_subnet_is_enabled_by_default of this AgentServiceSubnet.  # noqa: E501
        :type: bool
        """
        if agent_service_subnet_is_enabled_by_default is None:
            raise ValueError(
                "Invalid value for `agent_service_subnet_is_enabled_by_default`, must not be `None`"
            )  # noqa: E501

        self._agent_service_subnet_is_enabled_by_default = (
            agent_service_subnet_is_enabled_by_default
        )

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
        if issubclass(AgentServiceSubnet, dict):
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
        if not isinstance(other, AgentServiceSubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
