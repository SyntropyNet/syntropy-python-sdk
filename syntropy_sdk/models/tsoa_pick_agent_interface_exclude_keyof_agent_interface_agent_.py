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


class TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_(object):
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
        "user_id": "float",
        "agent_interface_id": "float",
        "agent_id": "float",
        "agent_interface_is_configured": "bool",
        "agent_interface_link_tag": "LinkTag",
        "agent_interface_name": "str",
        "agent_interface_public_key": "str",
        "agent_interface_endpoint_ipv4": "str",
        "agent_interface_endpoint_port": "float",
        "agent_interface_internal_ipv4": "str",
        "agent_interface_created_at": "datetime",
        "agent_interface_updated_at": "datetime",
    }

    attribute_map = {
        "user_id": "user_id",
        "agent_interface_id": "agent_interface_id",
        "agent_id": "agent_id",
        "agent_interface_is_configured": "agent_interface_is_configured",
        "agent_interface_link_tag": "agent_interface_link_tag",
        "agent_interface_name": "agent_interface_name",
        "agent_interface_public_key": "agent_interface_public_key",
        "agent_interface_endpoint_ipv4": "agent_interface_endpoint_ipv4",
        "agent_interface_endpoint_port": "agent_interface_endpoint_port",
        "agent_interface_internal_ipv4": "agent_interface_internal_ipv4",
        "agent_interface_created_at": "agent_interface_created_at",
        "agent_interface_updated_at": "agent_interface_updated_at",
    }

    def __init__(
        self,
        user_id=None,
        agent_interface_id=None,
        agent_id=None,
        agent_interface_is_configured=None,
        agent_interface_link_tag=None,
        agent_interface_name=None,
        agent_interface_public_key=None,
        agent_interface_endpoint_ipv4=None,
        agent_interface_endpoint_port=None,
        agent_interface_internal_ipv4=None,
        agent_interface_created_at=None,
        agent_interface_updated_at=None,
    ):  # noqa: E501
        """TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_ - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._agent_interface_id = None
        self._agent_id = None
        self._agent_interface_is_configured = None
        self._agent_interface_link_tag = None
        self._agent_interface_name = None
        self._agent_interface_public_key = None
        self._agent_interface_endpoint_ipv4 = None
        self._agent_interface_endpoint_port = None
        self._agent_interface_internal_ipv4 = None
        self._agent_interface_created_at = None
        self._agent_interface_updated_at = None
        self.discriminator = None
        self.user_id = user_id
        self.agent_interface_id = agent_interface_id
        self.agent_id = agent_id
        self.agent_interface_is_configured = agent_interface_is_configured
        self.agent_interface_link_tag = agent_interface_link_tag
        self.agent_interface_name = agent_interface_name
        self.agent_interface_public_key = agent_interface_public_key
        if agent_interface_endpoint_ipv4 is not None:
            self.agent_interface_endpoint_ipv4 = agent_interface_endpoint_ipv4
        if agent_interface_endpoint_port is not None:
            self.agent_interface_endpoint_port = agent_interface_endpoint_port
        self.agent_interface_internal_ipv4 = agent_interface_internal_ipv4
        self.agent_interface_created_at = agent_interface_created_at
        self.agent_interface_updated_at = agent_interface_updated_at

    @property
    def user_id(self):
        """Gets the user_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The user_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param user_id: The user_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: float
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def agent_interface_id(self):
        """Gets the agent_interface_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: float
        """
        return self._agent_interface_id

    @agent_interface_id.setter
    def agent_interface_id(self, agent_interface_id):
        """Sets the agent_interface_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_id: The agent_interface_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: float
        """
        if agent_interface_id is None:
            raise ValueError(
                "Invalid value for `agent_interface_id`, must not be `None`"
            )  # noqa: E501

        self._agent_interface_id = agent_interface_id

    @property
    def agent_id(self):
        """Gets the agent_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_id: The agent_id of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def agent_interface_is_configured(self):
        """Gets the agent_interface_is_configured of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_is_configured of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: bool
        """
        return self._agent_interface_is_configured

    @agent_interface_is_configured.setter
    def agent_interface_is_configured(self, agent_interface_is_configured):
        """Sets the agent_interface_is_configured of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_is_configured: The agent_interface_is_configured of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: bool
        """
        if agent_interface_is_configured is None:
            raise ValueError(
                "Invalid value for `agent_interface_is_configured`, must not be `None`"
            )  # noqa: E501

        self._agent_interface_is_configured = agent_interface_is_configured

    @property
    def agent_interface_link_tag(self):
        """Gets the agent_interface_link_tag of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_link_tag of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: LinkTag
        """
        return self._agent_interface_link_tag

    @agent_interface_link_tag.setter
    def agent_interface_link_tag(self, agent_interface_link_tag):
        """Sets the agent_interface_link_tag of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_link_tag: The agent_interface_link_tag of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: LinkTag
        """
        if agent_interface_link_tag is None:
            raise ValueError(
                "Invalid value for `agent_interface_link_tag`, must not be `None`"
            )  # noqa: E501

        self._agent_interface_link_tag = agent_interface_link_tag

    @property
    def agent_interface_name(self):
        """Gets the agent_interface_name of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_name of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: str
        """
        return self._agent_interface_name

    @agent_interface_name.setter
    def agent_interface_name(self, agent_interface_name):
        """Sets the agent_interface_name of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_name: The agent_interface_name of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: str
        """
        if agent_interface_name is None:
            raise ValueError(
                "Invalid value for `agent_interface_name`, must not be `None`"
            )  # noqa: E501

        self._agent_interface_name = agent_interface_name

    @property
    def agent_interface_public_key(self):
        """Gets the agent_interface_public_key of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_public_key of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: str
        """
        return self._agent_interface_public_key

    @agent_interface_public_key.setter
    def agent_interface_public_key(self, agent_interface_public_key):
        """Sets the agent_interface_public_key of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_public_key: The agent_interface_public_key of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: str
        """
        if agent_interface_public_key is None:
            raise ValueError(
                "Invalid value for `agent_interface_public_key`, must not be `None`"
            )  # noqa: E501

        self._agent_interface_public_key = agent_interface_public_key

    @property
    def agent_interface_endpoint_ipv4(self):
        """Gets the agent_interface_endpoint_ipv4 of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_endpoint_ipv4 of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: str
        """
        return self._agent_interface_endpoint_ipv4

    @agent_interface_endpoint_ipv4.setter
    def agent_interface_endpoint_ipv4(self, agent_interface_endpoint_ipv4):
        """Sets the agent_interface_endpoint_ipv4 of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_endpoint_ipv4: The agent_interface_endpoint_ipv4 of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: str
        """

        self._agent_interface_endpoint_ipv4 = agent_interface_endpoint_ipv4

    @property
    def agent_interface_endpoint_port(self):
        """Gets the agent_interface_endpoint_port of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_endpoint_port of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: float
        """
        return self._agent_interface_endpoint_port

    @agent_interface_endpoint_port.setter
    def agent_interface_endpoint_port(self, agent_interface_endpoint_port):
        """Sets the agent_interface_endpoint_port of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_endpoint_port: The agent_interface_endpoint_port of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: float
        """

        self._agent_interface_endpoint_port = agent_interface_endpoint_port

    @property
    def agent_interface_internal_ipv4(self):
        """Gets the agent_interface_internal_ipv4 of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_internal_ipv4 of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: str
        """
        return self._agent_interface_internal_ipv4

    @agent_interface_internal_ipv4.setter
    def agent_interface_internal_ipv4(self, agent_interface_internal_ipv4):
        """Sets the agent_interface_internal_ipv4 of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_internal_ipv4: The agent_interface_internal_ipv4 of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: str
        """
        if agent_interface_internal_ipv4 is None:
            raise ValueError(
                "Invalid value for `agent_interface_internal_ipv4`, must not be `None`"
            )  # noqa: E501

        self._agent_interface_internal_ipv4 = agent_interface_internal_ipv4

    @property
    def agent_interface_created_at(self):
        """Gets the agent_interface_created_at of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_created_at of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_interface_created_at

    @agent_interface_created_at.setter
    def agent_interface_created_at(self, agent_interface_created_at):
        """Sets the agent_interface_created_at of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_created_at: The agent_interface_created_at of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: datetime
        """
        if agent_interface_created_at is None:
            raise ValueError(
                "Invalid value for `agent_interface_created_at`, must not be `None`"
            )  # noqa: E501

        self._agent_interface_created_at = agent_interface_created_at

    @property
    def agent_interface_updated_at(self):
        """Gets the agent_interface_updated_at of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501


        :return: The agent_interface_updated_at of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_interface_updated_at

    @agent_interface_updated_at.setter
    def agent_interface_updated_at(self, agent_interface_updated_at):
        """Sets the agent_interface_updated_at of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.


        :param agent_interface_updated_at: The agent_interface_updated_at of this TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_.  # noqa: E501
        :type: datetime
        """
        if agent_interface_updated_at is None:
            raise ValueError(
                "Invalid value for `agent_interface_updated_at`, must not be `None`"
            )  # noqa: E501

        self._agent_interface_updated_at = agent_interface_updated_at

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
        if issubclass(TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_, dict):
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
            other, TsoaPickAgentInterfaceExcludeKeyofAgentInterfaceAgent_
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
