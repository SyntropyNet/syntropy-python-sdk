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


class V1NetworkAgent(object):
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
        "agent_id": "int",
        "agent_is_online": "bool",
        "agent_name": "str",
        "agent_type": "AgentType",
        "agent_version": "str",
        "agent_device_id": "str",
        "agent_location_city": "str",
        "agent_provider_id": "int",
        "agent_public_ipv4": "str",
        "agent_status": "AgentStatus",
        "agent_tags": "list[AgentTag]",
    }

    attribute_map = {
        "agent_id": "agent_id",
        "agent_is_online": "agent_is_online",
        "agent_name": "agent_name",
        "agent_type": "agent_type",
        "agent_version": "agent_version",
        "agent_device_id": "agent_device_id",
        "agent_location_city": "agent_location_city",
        "agent_provider_id": "agent_provider_id",
        "agent_public_ipv4": "agent_public_ipv4",
        "agent_status": "agent_status",
        "agent_tags": "agent_tags",
    }

    def __init__(
        self,
        agent_id=None,
        agent_is_online=None,
        agent_name=None,
        agent_type=None,
        agent_version=None,
        agent_device_id=None,
        agent_location_city=None,
        agent_provider_id=None,
        agent_public_ipv4=None,
        agent_status=None,
        agent_tags=None,
    ):  # noqa: E501
        """V1NetworkAgent - a model defined in Swagger"""  # noqa: E501
        self._agent_id = None
        self._agent_is_online = None
        self._agent_name = None
        self._agent_type = None
        self._agent_version = None
        self._agent_device_id = None
        self._agent_location_city = None
        self._agent_provider_id = None
        self._agent_public_ipv4 = None
        self._agent_status = None
        self._agent_tags = None
        self.discriminator = None
        self.agent_id = agent_id
        self.agent_is_online = agent_is_online
        self.agent_name = agent_name
        self.agent_type = agent_type
        self.agent_version = agent_version
        self.agent_device_id = agent_device_id
        self.agent_location_city = agent_location_city
        self.agent_provider_id = agent_provider_id
        self.agent_public_ipv4 = agent_public_ipv4
        self.agent_status = agent_status
        self.agent_tags = agent_tags

    @property
    def agent_id(self):
        """Gets the agent_id of this V1NetworkAgent.  # noqa: E501


        :return: The agent_id of this V1NetworkAgent.  # noqa: E501
        :rtype: int
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this V1NetworkAgent.


        :param agent_id: The agent_id of this V1NetworkAgent.  # noqa: E501
        :type: int
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def agent_is_online(self):
        """Gets the agent_is_online of this V1NetworkAgent.  # noqa: E501


        :return: The agent_is_online of this V1NetworkAgent.  # noqa: E501
        :rtype: bool
        """
        return self._agent_is_online

    @agent_is_online.setter
    def agent_is_online(self, agent_is_online):
        """Sets the agent_is_online of this V1NetworkAgent.


        :param agent_is_online: The agent_is_online of this V1NetworkAgent.  # noqa: E501
        :type: bool
        """
        if agent_is_online is None:
            raise ValueError(
                "Invalid value for `agent_is_online`, must not be `None`"
            )  # noqa: E501

        self._agent_is_online = agent_is_online

    @property
    def agent_name(self):
        """Gets the agent_name of this V1NetworkAgent.  # noqa: E501


        :return: The agent_name of this V1NetworkAgent.  # noqa: E501
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this V1NetworkAgent.


        :param agent_name: The agent_name of this V1NetworkAgent.  # noqa: E501
        :type: str
        """
        if agent_name is None:
            raise ValueError(
                "Invalid value for `agent_name`, must not be `None`"
            )  # noqa: E501

        self._agent_name = agent_name

    @property
    def agent_type(self):
        """Gets the agent_type of this V1NetworkAgent.  # noqa: E501


        :return: The agent_type of this V1NetworkAgent.  # noqa: E501
        :rtype: AgentType
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this V1NetworkAgent.


        :param agent_type: The agent_type of this V1NetworkAgent.  # noqa: E501
        :type: AgentType
        """
        if agent_type is None:
            raise ValueError(
                "Invalid value for `agent_type`, must not be `None`"
            )  # noqa: E501

        self._agent_type = agent_type

    @property
    def agent_version(self):
        """Gets the agent_version of this V1NetworkAgent.  # noqa: E501


        :return: The agent_version of this V1NetworkAgent.  # noqa: E501
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this V1NetworkAgent.


        :param agent_version: The agent_version of this V1NetworkAgent.  # noqa: E501
        :type: str
        """
        if agent_version is None:
            raise ValueError(
                "Invalid value for `agent_version`, must not be `None`"
            )  # noqa: E501

        self._agent_version = agent_version

    @property
    def agent_device_id(self):
        """Gets the agent_device_id of this V1NetworkAgent.  # noqa: E501


        :return: The agent_device_id of this V1NetworkAgent.  # noqa: E501
        :rtype: str
        """
        return self._agent_device_id

    @agent_device_id.setter
    def agent_device_id(self, agent_device_id):
        """Sets the agent_device_id of this V1NetworkAgent.


        :param agent_device_id: The agent_device_id of this V1NetworkAgent.  # noqa: E501
        :type: str
        """
        if agent_device_id is None:
            raise ValueError(
                "Invalid value for `agent_device_id`, must not be `None`"
            )  # noqa: E501

        self._agent_device_id = agent_device_id

    @property
    def agent_location_city(self):
        """Gets the agent_location_city of this V1NetworkAgent.  # noqa: E501


        :return: The agent_location_city of this V1NetworkAgent.  # noqa: E501
        :rtype: str
        """
        return self._agent_location_city

    @agent_location_city.setter
    def agent_location_city(self, agent_location_city):
        """Sets the agent_location_city of this V1NetworkAgent.


        :param agent_location_city: The agent_location_city of this V1NetworkAgent.  # noqa: E501
        :type: str
        """
        if agent_location_city is None:
            raise ValueError(
                "Invalid value for `agent_location_city`, must not be `None`"
            )  # noqa: E501

        self._agent_location_city = agent_location_city

    @property
    def agent_provider_id(self):
        """Gets the agent_provider_id of this V1NetworkAgent.  # noqa: E501


        :return: The agent_provider_id of this V1NetworkAgent.  # noqa: E501
        :rtype: int
        """
        return self._agent_provider_id

    @agent_provider_id.setter
    def agent_provider_id(self, agent_provider_id):
        """Sets the agent_provider_id of this V1NetworkAgent.


        :param agent_provider_id: The agent_provider_id of this V1NetworkAgent.  # noqa: E501
        :type: int
        """
        if agent_provider_id is None:
            raise ValueError(
                "Invalid value for `agent_provider_id`, must not be `None`"
            )  # noqa: E501

        self._agent_provider_id = agent_provider_id

    @property
    def agent_public_ipv4(self):
        """Gets the agent_public_ipv4 of this V1NetworkAgent.  # noqa: E501


        :return: The agent_public_ipv4 of this V1NetworkAgent.  # noqa: E501
        :rtype: str
        """
        return self._agent_public_ipv4

    @agent_public_ipv4.setter
    def agent_public_ipv4(self, agent_public_ipv4):
        """Sets the agent_public_ipv4 of this V1NetworkAgent.


        :param agent_public_ipv4: The agent_public_ipv4 of this V1NetworkAgent.  # noqa: E501
        :type: str
        """
        if agent_public_ipv4 is None:
            raise ValueError(
                "Invalid value for `agent_public_ipv4`, must not be `None`"
            )  # noqa: E501

        self._agent_public_ipv4 = agent_public_ipv4

    @property
    def agent_status(self):
        """Gets the agent_status of this V1NetworkAgent.  # noqa: E501


        :return: The agent_status of this V1NetworkAgent.  # noqa: E501
        :rtype: AgentStatus
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this V1NetworkAgent.


        :param agent_status: The agent_status of this V1NetworkAgent.  # noqa: E501
        :type: AgentStatus
        """
        if agent_status is None:
            raise ValueError(
                "Invalid value for `agent_status`, must not be `None`"
            )  # noqa: E501

        self._agent_status = agent_status

    @property
    def agent_tags(self):
        """Gets the agent_tags of this V1NetworkAgent.  # noqa: E501


        :return: The agent_tags of this V1NetworkAgent.  # noqa: E501
        :rtype: list[AgentTag]
        """
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, agent_tags):
        """Sets the agent_tags of this V1NetworkAgent.


        :param agent_tags: The agent_tags of this V1NetworkAgent.  # noqa: E501
        :type: list[AgentTag]
        """
        if agent_tags is None:
            raise ValueError(
                "Invalid value for `agent_tags`, must not be `None`"
            )  # noqa: E501

        self._agent_tags = agent_tags

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
        if issubclass(V1NetworkAgent, dict):
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
        if not isinstance(other, V1NetworkAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other