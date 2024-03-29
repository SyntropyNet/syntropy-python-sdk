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


class V1AgentFilter(object):
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
        "agent_id": "list[IdNumber]",
        "agent_provider_id": "list[IdNumber]",
        "agent_tag_id": "list[IdNumber]",
        "agent_type": "list[AgentType]",
        "agent_version": "list[str]",
        "agent_tag_name": "list[str]",
        "agent_status": "list[AgentFilterAgentStatus]",
        "agent_location_country": "list[str]",
        "agent_modified_at_from": "datetime",
        "agent_modified_at_to": "datetime",
        "agent_name": "str",
    }

    attribute_map = {
        "agent_id": "agent_id",
        "agent_provider_id": "agent_provider_id",
        "agent_tag_id": "agent_tag_id",
        "agent_type": "agent_type",
        "agent_version": "agent_version",
        "agent_tag_name": "agent_tag_name",
        "agent_status": "agent_status",
        "agent_location_country": "agent_location_country",
        "agent_modified_at_from": "agent_modified_at_from",
        "agent_modified_at_to": "agent_modified_at_to",
        "agent_name": "agent_name",
    }

    def __init__(
        self,
        agent_id=None,
        agent_provider_id=None,
        agent_tag_id=None,
        agent_type=None,
        agent_version=None,
        agent_tag_name=None,
        agent_status=None,
        agent_location_country=None,
        agent_modified_at_from=None,
        agent_modified_at_to=None,
        agent_name=None,
    ):  # noqa: E501
        """V1AgentFilter - a model defined in Swagger"""  # noqa: E501
        self._agent_id = None
        self._agent_provider_id = None
        self._agent_tag_id = None
        self._agent_type = None
        self._agent_version = None
        self._agent_tag_name = None
        self._agent_status = None
        self._agent_location_country = None
        self._agent_modified_at_from = None
        self._agent_modified_at_to = None
        self._agent_name = None
        self.discriminator = None
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_provider_id is not None:
            self.agent_provider_id = agent_provider_id
        if agent_tag_id is not None:
            self.agent_tag_id = agent_tag_id
        if agent_type is not None:
            self.agent_type = agent_type
        if agent_version is not None:
            self.agent_version = agent_version
        if agent_tag_name is not None:
            self.agent_tag_name = agent_tag_name
        if agent_status is not None:
            self.agent_status = agent_status
        if agent_location_country is not None:
            self.agent_location_country = agent_location_country
        if agent_modified_at_from is not None:
            self.agent_modified_at_from = agent_modified_at_from
        if agent_modified_at_to is not None:
            self.agent_modified_at_to = agent_modified_at_to
        if agent_name is not None:
            self.agent_name = agent_name

    @property
    def agent_id(self):
        """Gets the agent_id of this V1AgentFilter.  # noqa: E501


        :return: The agent_id of this V1AgentFilter.  # noqa: E501
        :rtype: list[IdNumber]
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this V1AgentFilter.


        :param agent_id: The agent_id of this V1AgentFilter.  # noqa: E501
        :type: list[IdNumber]
        """

        self._agent_id = agent_id

    @property
    def agent_provider_id(self):
        """Gets the agent_provider_id of this V1AgentFilter.  # noqa: E501


        :return: The agent_provider_id of this V1AgentFilter.  # noqa: E501
        :rtype: list[IdNumber]
        """
        return self._agent_provider_id

    @agent_provider_id.setter
    def agent_provider_id(self, agent_provider_id):
        """Sets the agent_provider_id of this V1AgentFilter.


        :param agent_provider_id: The agent_provider_id of this V1AgentFilter.  # noqa: E501
        :type: list[IdNumber]
        """

        self._agent_provider_id = agent_provider_id

    @property
    def agent_tag_id(self):
        """Gets the agent_tag_id of this V1AgentFilter.  # noqa: E501


        :return: The agent_tag_id of this V1AgentFilter.  # noqa: E501
        :rtype: list[IdNumber]
        """
        return self._agent_tag_id

    @agent_tag_id.setter
    def agent_tag_id(self, agent_tag_id):
        """Sets the agent_tag_id of this V1AgentFilter.


        :param agent_tag_id: The agent_tag_id of this V1AgentFilter.  # noqa: E501
        :type: list[IdNumber]
        """

        self._agent_tag_id = agent_tag_id

    @property
    def agent_type(self):
        """Gets the agent_type of this V1AgentFilter.  # noqa: E501


        :return: The agent_type of this V1AgentFilter.  # noqa: E501
        :rtype: list[AgentType]
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this V1AgentFilter.


        :param agent_type: The agent_type of this V1AgentFilter.  # noqa: E501
        :type: list[AgentType]
        """

        self._agent_type = agent_type

    @property
    def agent_version(self):
        """Gets the agent_version of this V1AgentFilter.  # noqa: E501


        :return: The agent_version of this V1AgentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this V1AgentFilter.


        :param agent_version: The agent_version of this V1AgentFilter.  # noqa: E501
        :type: list[str]
        """

        self._agent_version = agent_version

    @property
    def agent_tag_name(self):
        """Gets the agent_tag_name of this V1AgentFilter.  # noqa: E501


        :return: The agent_tag_name of this V1AgentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_tag_name

    @agent_tag_name.setter
    def agent_tag_name(self, agent_tag_name):
        """Sets the agent_tag_name of this V1AgentFilter.


        :param agent_tag_name: The agent_tag_name of this V1AgentFilter.  # noqa: E501
        :type: list[str]
        """

        self._agent_tag_name = agent_tag_name

    @property
    def agent_status(self):
        """Gets the agent_status of this V1AgentFilter.  # noqa: E501


        :return: The agent_status of this V1AgentFilter.  # noqa: E501
        :rtype: list[AgentFilterAgentStatus]
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this V1AgentFilter.


        :param agent_status: The agent_status of this V1AgentFilter.  # noqa: E501
        :type: list[AgentFilterAgentStatus]
        """

        self._agent_status = agent_status

    @property
    def agent_location_country(self):
        """Gets the agent_location_country of this V1AgentFilter.  # noqa: E501


        :return: The agent_location_country of this V1AgentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_location_country

    @agent_location_country.setter
    def agent_location_country(self, agent_location_country):
        """Sets the agent_location_country of this V1AgentFilter.


        :param agent_location_country: The agent_location_country of this V1AgentFilter.  # noqa: E501
        :type: list[str]
        """

        self._agent_location_country = agent_location_country

    @property
    def agent_modified_at_from(self):
        """Gets the agent_modified_at_from of this V1AgentFilter.  # noqa: E501


        :return: The agent_modified_at_from of this V1AgentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_modified_at_from

    @agent_modified_at_from.setter
    def agent_modified_at_from(self, agent_modified_at_from):
        """Sets the agent_modified_at_from of this V1AgentFilter.


        :param agent_modified_at_from: The agent_modified_at_from of this V1AgentFilter.  # noqa: E501
        :type: datetime
        """

        self._agent_modified_at_from = agent_modified_at_from

    @property
    def agent_modified_at_to(self):
        """Gets the agent_modified_at_to of this V1AgentFilter.  # noqa: E501


        :return: The agent_modified_at_to of this V1AgentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_modified_at_to

    @agent_modified_at_to.setter
    def agent_modified_at_to(self, agent_modified_at_to):
        """Sets the agent_modified_at_to of this V1AgentFilter.


        :param agent_modified_at_to: The agent_modified_at_to of this V1AgentFilter.  # noqa: E501
        :type: datetime
        """

        self._agent_modified_at_to = agent_modified_at_to

    @property
    def agent_name(self):
        """Gets the agent_name of this V1AgentFilter.  # noqa: E501


        :return: The agent_name of this V1AgentFilter.  # noqa: E501
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this V1AgentFilter.


        :param agent_name: The agent_name of this V1AgentFilter.  # noqa: E501
        :type: str
        """

        self._agent_name = agent_name

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
        if issubclass(V1AgentFilter, dict):
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
        if not isinstance(other, V1AgentFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
