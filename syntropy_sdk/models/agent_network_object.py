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


class AgentNetworkObject(object):
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
        "agent_network_id_external": "str",
        "agent_network_name": "str",
        "agent_network_subnet": "str",
    }

    attribute_map = {
        "agent_id": "agent_id",
        "agent_network_id_external": "agent_network_id_external",
        "agent_network_name": "agent_network_name",
        "agent_network_subnet": "agent_network_subnet",
    }

    def __init__(
        self,
        agent_id=None,
        agent_network_id_external=None,
        agent_network_name=None,
        agent_network_subnet=None,
    ):  # noqa: E501
        """AgentNetworkObject - a model defined in Swagger"""  # noqa: E501
        self._agent_id = None
        self._agent_network_id_external = None
        self._agent_network_name = None
        self._agent_network_subnet = None
        self.discriminator = None
        self.agent_id = agent_id
        if agent_network_id_external is not None:
            self.agent_network_id_external = agent_network_id_external
        if agent_network_name is not None:
            self.agent_network_name = agent_network_name
        self.agent_network_subnet = agent_network_subnet

    @property
    def agent_id(self):
        """Gets the agent_id of this AgentNetworkObject.  # noqa: E501


        :return: The agent_id of this AgentNetworkObject.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AgentNetworkObject.


        :param agent_id: The agent_id of this AgentNetworkObject.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def agent_network_id_external(self):
        """Gets the agent_network_id_external of this AgentNetworkObject.  # noqa: E501


        :return: The agent_network_id_external of this AgentNetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._agent_network_id_external

    @agent_network_id_external.setter
    def agent_network_id_external(self, agent_network_id_external):
        """Sets the agent_network_id_external of this AgentNetworkObject.


        :param agent_network_id_external: The agent_network_id_external of this AgentNetworkObject.  # noqa: E501
        :type: str
        """

        self._agent_network_id_external = agent_network_id_external

    @property
    def agent_network_name(self):
        """Gets the agent_network_name of this AgentNetworkObject.  # noqa: E501


        :return: The agent_network_name of this AgentNetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._agent_network_name

    @agent_network_name.setter
    def agent_network_name(self, agent_network_name):
        """Sets the agent_network_name of this AgentNetworkObject.


        :param agent_network_name: The agent_network_name of this AgentNetworkObject.  # noqa: E501
        :type: str
        """

        self._agent_network_name = agent_network_name

    @property
    def agent_network_subnet(self):
        """Gets the agent_network_subnet of this AgentNetworkObject.  # noqa: E501


        :return: The agent_network_subnet of this AgentNetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._agent_network_subnet

    @agent_network_subnet.setter
    def agent_network_subnet(self, agent_network_subnet):
        """Sets the agent_network_subnet of this AgentNetworkObject.


        :param agent_network_subnet: The agent_network_subnet of this AgentNetworkObject.  # noqa: E501
        :type: str
        """
        if agent_network_subnet is None:
            raise ValueError(
                "Invalid value for `agent_network_subnet`, must not be `None`"
            )  # noqa: E501

        self._agent_network_subnet = agent_network_subnet

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
        if issubclass(AgentNetworkObject, dict):
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
        if not isinstance(other, AgentNetworkObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
