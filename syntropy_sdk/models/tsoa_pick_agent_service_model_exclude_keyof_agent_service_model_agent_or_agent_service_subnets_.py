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


class TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_(
    object
):
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
        "agent_id": "float",
        "agent_service_id": "float",
        "agent_service_name": "str",
        "agent_service_type": "AgentServiceTypes",
        "agent_service_networks": "list[str]",
        "agent_service_tcp_ports": "list[float]",
        "agent_service_udp_ports": "list[float]",
        "agent_service_is_active": "bool",
        "agent_service_is_enabled_by_default": "bool",
        "agent_service_is_active_modified_at": "datetime",
        "agent_service_created_at": "datetime",
        "agent_service_updated_at": "datetime",
    }

    attribute_map = {
        "agent_id": "agent_id",
        "agent_service_id": "agent_service_id",
        "agent_service_name": "agent_service_name",
        "agent_service_type": "agent_service_type",
        "agent_service_networks": "agent_service_networks",
        "agent_service_tcp_ports": "agent_service_tcp_ports",
        "agent_service_udp_ports": "agent_service_udp_ports",
        "agent_service_is_active": "agent_service_is_active",
        "agent_service_is_enabled_by_default": "agent_service_is_enabled_by_default",
        "agent_service_is_active_modified_at": "agent_service_is_active_modified_at",
        "agent_service_created_at": "agent_service_created_at",
        "agent_service_updated_at": "agent_service_updated_at",
    }

    def __init__(
        self,
        agent_id=None,
        agent_service_id=None,
        agent_service_name=None,
        agent_service_type=None,
        agent_service_networks=None,
        agent_service_tcp_ports=None,
        agent_service_udp_ports=None,
        agent_service_is_active=None,
        agent_service_is_enabled_by_default=None,
        agent_service_is_active_modified_at=None,
        agent_service_created_at=None,
        agent_service_updated_at=None,
    ):  # noqa: E501
        """TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_ - a model defined in Swagger"""  # noqa: E501
        self._agent_id = None
        self._agent_service_id = None
        self._agent_service_name = None
        self._agent_service_type = None
        self._agent_service_networks = None
        self._agent_service_tcp_ports = None
        self._agent_service_udp_ports = None
        self._agent_service_is_active = None
        self._agent_service_is_enabled_by_default = None
        self._agent_service_is_active_modified_at = None
        self._agent_service_created_at = None
        self._agent_service_updated_at = None
        self.discriminator = None
        self.agent_id = agent_id
        self.agent_service_id = agent_service_id
        self.agent_service_name = agent_service_name
        self.agent_service_type = agent_service_type
        self.agent_service_networks = agent_service_networks
        self.agent_service_tcp_ports = agent_service_tcp_ports
        self.agent_service_udp_ports = agent_service_udp_ports
        self.agent_service_is_active = agent_service_is_active
        self.agent_service_is_enabled_by_default = agent_service_is_enabled_by_default
        if agent_service_is_active_modified_at is not None:
            self.agent_service_is_active_modified_at = (
                agent_service_is_active_modified_at
            )
        self.agent_service_created_at = agent_service_created_at
        self.agent_service_updated_at = agent_service_updated_at

    @property
    def agent_id(self):
        """Gets the agent_id of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_id of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_id: The agent_id of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def agent_service_id(self):
        """Gets the agent_service_id of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_id of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: float
        """
        return self._agent_service_id

    @agent_service_id.setter
    def agent_service_id(self, agent_service_id):
        """Sets the agent_service_id of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_id: The agent_service_id of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: float
        """
        if agent_service_id is None:
            raise ValueError(
                "Invalid value for `agent_service_id`, must not be `None`"
            )  # noqa: E501

        self._agent_service_id = agent_service_id

    @property
    def agent_service_name(self):
        """Gets the agent_service_name of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_name of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: str
        """
        return self._agent_service_name

    @agent_service_name.setter
    def agent_service_name(self, agent_service_name):
        """Sets the agent_service_name of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_name: The agent_service_name of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: str
        """
        if agent_service_name is None:
            raise ValueError(
                "Invalid value for `agent_service_name`, must not be `None`"
            )  # noqa: E501

        self._agent_service_name = agent_service_name

    @property
    def agent_service_type(self):
        """Gets the agent_service_type of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_type of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: AgentServiceTypes
        """
        return self._agent_service_type

    @agent_service_type.setter
    def agent_service_type(self, agent_service_type):
        """Sets the agent_service_type of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_type: The agent_service_type of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: AgentServiceTypes
        """
        if agent_service_type is None:
            raise ValueError(
                "Invalid value for `agent_service_type`, must not be `None`"
            )  # noqa: E501

        self._agent_service_type = agent_service_type

    @property
    def agent_service_networks(self):
        """Gets the agent_service_networks of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_networks of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_service_networks

    @agent_service_networks.setter
    def agent_service_networks(self, agent_service_networks):
        """Sets the agent_service_networks of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_networks: The agent_service_networks of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: list[str]
        """
        if agent_service_networks is None:
            raise ValueError(
                "Invalid value for `agent_service_networks`, must not be `None`"
            )  # noqa: E501

        self._agent_service_networks = agent_service_networks

    @property
    def agent_service_tcp_ports(self):
        """Gets the agent_service_tcp_ports of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_tcp_ports of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: list[float]
        """
        return self._agent_service_tcp_ports

    @agent_service_tcp_ports.setter
    def agent_service_tcp_ports(self, agent_service_tcp_ports):
        """Sets the agent_service_tcp_ports of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_tcp_ports: The agent_service_tcp_ports of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: list[float]
        """
        if agent_service_tcp_ports is None:
            raise ValueError(
                "Invalid value for `agent_service_tcp_ports`, must not be `None`"
            )  # noqa: E501

        self._agent_service_tcp_ports = agent_service_tcp_ports

    @property
    def agent_service_udp_ports(self):
        """Gets the agent_service_udp_ports of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_udp_ports of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: list[float]
        """
        return self._agent_service_udp_ports

    @agent_service_udp_ports.setter
    def agent_service_udp_ports(self, agent_service_udp_ports):
        """Sets the agent_service_udp_ports of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_udp_ports: The agent_service_udp_ports of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: list[float]
        """
        if agent_service_udp_ports is None:
            raise ValueError(
                "Invalid value for `agent_service_udp_ports`, must not be `None`"
            )  # noqa: E501

        self._agent_service_udp_ports = agent_service_udp_ports

    @property
    def agent_service_is_active(self):
        """Gets the agent_service_is_active of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_is_active of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: bool
        """
        return self._agent_service_is_active

    @agent_service_is_active.setter
    def agent_service_is_active(self, agent_service_is_active):
        """Sets the agent_service_is_active of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_is_active: The agent_service_is_active of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: bool
        """
        if agent_service_is_active is None:
            raise ValueError(
                "Invalid value for `agent_service_is_active`, must not be `None`"
            )  # noqa: E501

        self._agent_service_is_active = agent_service_is_active

    @property
    def agent_service_is_enabled_by_default(self):
        """Gets the agent_service_is_enabled_by_default of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_is_enabled_by_default of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: bool
        """
        return self._agent_service_is_enabled_by_default

    @agent_service_is_enabled_by_default.setter
    def agent_service_is_enabled_by_default(self, agent_service_is_enabled_by_default):
        """Sets the agent_service_is_enabled_by_default of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_is_enabled_by_default: The agent_service_is_enabled_by_default of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: bool
        """
        if agent_service_is_enabled_by_default is None:
            raise ValueError(
                "Invalid value for `agent_service_is_enabled_by_default`, must not be `None`"
            )  # noqa: E501

        self._agent_service_is_enabled_by_default = agent_service_is_enabled_by_default

    @property
    def agent_service_is_active_modified_at(self):
        """Gets the agent_service_is_active_modified_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_is_active_modified_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_service_is_active_modified_at

    @agent_service_is_active_modified_at.setter
    def agent_service_is_active_modified_at(self, agent_service_is_active_modified_at):
        """Sets the agent_service_is_active_modified_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_is_active_modified_at: The agent_service_is_active_modified_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: datetime
        """

        self._agent_service_is_active_modified_at = agent_service_is_active_modified_at

    @property
    def agent_service_created_at(self):
        """Gets the agent_service_created_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_created_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_service_created_at

    @agent_service_created_at.setter
    def agent_service_created_at(self, agent_service_created_at):
        """Sets the agent_service_created_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_created_at: The agent_service_created_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: datetime
        """
        if agent_service_created_at is None:
            raise ValueError(
                "Invalid value for `agent_service_created_at`, must not be `None`"
            )  # noqa: E501

        self._agent_service_created_at = agent_service_created_at

    @property
    def agent_service_updated_at(self):
        """Gets the agent_service_updated_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501


        :return: The agent_service_updated_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_service_updated_at

    @agent_service_updated_at.setter
    def agent_service_updated_at(self, agent_service_updated_at):
        """Sets the agent_service_updated_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.


        :param agent_service_updated_at: The agent_service_updated_at of this TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_.  # noqa: E501
        :type: datetime
        """
        if agent_service_updated_at is None:
            raise ValueError(
                "Invalid value for `agent_service_updated_at`, must not be `None`"
            )  # noqa: E501

        self._agent_service_updated_at = agent_service_updated_at

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
        if issubclass(
            TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_,
            dict,
        ):
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
        if not isinstance(
            other,
            TsoaPickAgentServiceModelExcludeKeyofAgentServiceModelAgentOrAgentServiceSubnets_,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
