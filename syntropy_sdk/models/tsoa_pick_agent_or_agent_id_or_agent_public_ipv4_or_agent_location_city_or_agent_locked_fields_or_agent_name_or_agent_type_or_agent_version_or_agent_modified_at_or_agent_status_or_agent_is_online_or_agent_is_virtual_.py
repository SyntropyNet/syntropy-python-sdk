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


class TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_(
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
        "agent_public_ipv4": "str",
        "agent_location_city": "str",
        "agent_name": "str",
        "agent_status": "PlatformAgentStatus",
        "agent_version": "str",
        "agent_is_online": "bool",
        "agent_locked_fields": "AgentLockedFields",
        "agent_modified_at": "datetime",
        "agent_is_virtual": "bool",
        "agent_type": "PlatformAgentTypeLocal",
    }

    attribute_map = {
        "agent_id": "agent_id",
        "agent_public_ipv4": "agent_public_ipv4",
        "agent_location_city": "agent_location_city",
        "agent_name": "agent_name",
        "agent_status": "agent_status",
        "agent_version": "agent_version",
        "agent_is_online": "agent_is_online",
        "agent_locked_fields": "agent_locked_fields",
        "agent_modified_at": "agent_modified_at",
        "agent_is_virtual": "agent_is_virtual",
        "agent_type": "agent_type",
    }

    def __init__(
        self,
        agent_id=None,
        agent_public_ipv4=None,
        agent_location_city=None,
        agent_name=None,
        agent_status=None,
        agent_version=None,
        agent_is_online=None,
        agent_locked_fields=None,
        agent_modified_at=None,
        agent_is_virtual=None,
        agent_type=None,
    ):  # noqa: E501
        """TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_ - a model defined in Swagger"""  # noqa: E501
        self._agent_id = None
        self._agent_public_ipv4 = None
        self._agent_location_city = None
        self._agent_name = None
        self._agent_status = None
        self._agent_version = None
        self._agent_is_online = None
        self._agent_locked_fields = None
        self._agent_modified_at = None
        self._agent_is_virtual = None
        self._agent_type = None
        self.discriminator = None
        self.agent_id = agent_id
        self.agent_public_ipv4 = agent_public_ipv4
        if agent_location_city is not None:
            self.agent_location_city = agent_location_city
        self.agent_name = agent_name
        if agent_status is not None:
            self.agent_status = agent_status
        if agent_version is not None:
            self.agent_version = agent_version
        if agent_is_online is not None:
            self.agent_is_online = agent_is_online
        if agent_locked_fields is not None:
            self.agent_locked_fields = agent_locked_fields
        if agent_modified_at is not None:
            self.agent_modified_at = agent_modified_at
        self.agent_is_virtual = agent_is_virtual
        if agent_type is not None:
            self.agent_type = agent_type

    @property
    def agent_id(self):
        """Gets the agent_id of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_id of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_id: The agent_id of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def agent_public_ipv4(self):
        """Gets the agent_public_ipv4 of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_public_ipv4 of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: str
        """
        return self._agent_public_ipv4

    @agent_public_ipv4.setter
    def agent_public_ipv4(self, agent_public_ipv4):
        """Sets the agent_public_ipv4 of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_public_ipv4: The agent_public_ipv4 of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: str
        """
        if agent_public_ipv4 is None:
            raise ValueError(
                "Invalid value for `agent_public_ipv4`, must not be `None`"
            )  # noqa: E501

        self._agent_public_ipv4 = agent_public_ipv4

    @property
    def agent_location_city(self):
        """Gets the agent_location_city of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_location_city of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: str
        """
        return self._agent_location_city

    @agent_location_city.setter
    def agent_location_city(self, agent_location_city):
        """Sets the agent_location_city of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_location_city: The agent_location_city of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: str
        """

        self._agent_location_city = agent_location_city

    @property
    def agent_name(self):
        """Gets the agent_name of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_name of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_name: The agent_name of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: str
        """
        if agent_name is None:
            raise ValueError(
                "Invalid value for `agent_name`, must not be `None`"
            )  # noqa: E501

        self._agent_name = agent_name

    @property
    def agent_status(self):
        """Gets the agent_status of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_status of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: PlatformAgentStatus
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_status: The agent_status of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: PlatformAgentStatus
        """

        self._agent_status = agent_status

    @property
    def agent_version(self):
        """Gets the agent_version of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_version of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_version: The agent_version of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: str
        """

        self._agent_version = agent_version

    @property
    def agent_is_online(self):
        """Gets the agent_is_online of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_is_online of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: bool
        """
        return self._agent_is_online

    @agent_is_online.setter
    def agent_is_online(self, agent_is_online):
        """Sets the agent_is_online of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_is_online: The agent_is_online of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: bool
        """

        self._agent_is_online = agent_is_online

    @property
    def agent_locked_fields(self):
        """Gets the agent_locked_fields of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_locked_fields of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: AgentLockedFields
        """
        return self._agent_locked_fields

    @agent_locked_fields.setter
    def agent_locked_fields(self, agent_locked_fields):
        """Sets the agent_locked_fields of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_locked_fields: The agent_locked_fields of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: AgentLockedFields
        """

        self._agent_locked_fields = agent_locked_fields

    @property
    def agent_modified_at(self):
        """Gets the agent_modified_at of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_modified_at of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_modified_at

    @agent_modified_at.setter
    def agent_modified_at(self, agent_modified_at):
        """Sets the agent_modified_at of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_modified_at: The agent_modified_at of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: datetime
        """

        self._agent_modified_at = agent_modified_at

    @property
    def agent_is_virtual(self):
        """Gets the agent_is_virtual of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_is_virtual of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: bool
        """
        return self._agent_is_virtual

    @agent_is_virtual.setter
    def agent_is_virtual(self, agent_is_virtual):
        """Sets the agent_is_virtual of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_is_virtual: The agent_is_virtual of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: bool
        """
        if agent_is_virtual is None:
            raise ValueError(
                "Invalid value for `agent_is_virtual`, must not be `None`"
            )  # noqa: E501

        self._agent_is_virtual = agent_is_virtual

    @property
    def agent_type(self):
        """Gets the agent_type of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501


        :return: The agent_type of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :rtype: PlatformAgentTypeLocal
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.


        :param agent_type: The agent_type of this TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_.  # noqa: E501
        :type: PlatformAgentTypeLocal
        """

        self._agent_type = agent_type

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
            TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_,
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
            TsoaPickAgentOrAgentIdOrAgentPublicIpv4OrAgentLocationCityOrAgentLockedFieldsOrAgentNameOrAgentTypeOrAgentVersionOrAgentModifiedAtOrAgentStatusOrAgentIsOnlineOrAgentIsVirtual_,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other