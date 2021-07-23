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


class AgentConnectionWithServicesAgent(object):
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
        "agent_services": "list[AgentConnectionWithServicesAgentAgentServices]",
        "agent_type": "PlatformAgentTypeLocal",
        "agent_id": "float",
    }

    attribute_map = {
        "agent_services": "agent_services",
        "agent_type": "agent_type",
        "agent_id": "agent_id",
    }

    def __init__(
        self, agent_services=None, agent_type=None, agent_id=None
    ):  # noqa: E501
        """AgentConnectionWithServicesAgent - a model defined in Swagger"""  # noqa: E501
        self._agent_services = None
        self._agent_type = None
        self._agent_id = None
        self.discriminator = None
        self.agent_services = agent_services
        self.agent_type = agent_type
        self.agent_id = agent_id

    @property
    def agent_services(self):
        """Gets the agent_services of this AgentConnectionWithServicesAgent.  # noqa: E501


        :return: The agent_services of this AgentConnectionWithServicesAgent.  # noqa: E501
        :rtype: list[AgentConnectionWithServicesAgentAgentServices]
        """
        return self._agent_services

    @agent_services.setter
    def agent_services(self, agent_services):
        """Sets the agent_services of this AgentConnectionWithServicesAgent.


        :param agent_services: The agent_services of this AgentConnectionWithServicesAgent.  # noqa: E501
        :type: list[AgentConnectionWithServicesAgentAgentServices]
        """
        if agent_services is None:
            raise ValueError(
                "Invalid value for `agent_services`, must not be `None`"
            )  # noqa: E501

        self._agent_services = agent_services

    @property
    def agent_type(self):
        """Gets the agent_type of this AgentConnectionWithServicesAgent.  # noqa: E501


        :return: The agent_type of this AgentConnectionWithServicesAgent.  # noqa: E501
        :rtype: PlatformAgentTypeLocal
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this AgentConnectionWithServicesAgent.


        :param agent_type: The agent_type of this AgentConnectionWithServicesAgent.  # noqa: E501
        :type: PlatformAgentTypeLocal
        """
        if agent_type is None:
            raise ValueError(
                "Invalid value for `agent_type`, must not be `None`"
            )  # noqa: E501

        self._agent_type = agent_type

    @property
    def agent_id(self):
        """Gets the agent_id of this AgentConnectionWithServicesAgent.  # noqa: E501


        :return: The agent_id of this AgentConnectionWithServicesAgent.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AgentConnectionWithServicesAgent.


        :param agent_id: The agent_id of this AgentConnectionWithServicesAgent.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

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
        if issubclass(AgentConnectionWithServicesAgent, dict):
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
        if not isinstance(other, AgentConnectionWithServicesAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other