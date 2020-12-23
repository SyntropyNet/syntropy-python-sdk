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


class TsoaPartialNetworkObject_(object):
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
        "organization_id": "float",
        "user_id": "float",
        "agent_gateway_id": "float",
        "network_key": "str",
        "network_type": "NetworkType",
        "network_name": "str",
        "network_disable_sdn_connections": "bool",
        "network_metadata": "NetworkMetadata",
    }

    attribute_map = {
        "organization_id": "organization_id",
        "user_id": "user_id",
        "agent_gateway_id": "agent_gateway_id",
        "network_key": "network_key",
        "network_type": "network_type",
        "network_name": "network_name",
        "network_disable_sdn_connections": "network_disable_sdn_connections",
        "network_metadata": "network_metadata",
    }

    def __init__(
        self,
        organization_id=None,
        user_id=None,
        agent_gateway_id=None,
        network_key=None,
        network_type=None,
        network_name=None,
        network_disable_sdn_connections=None,
        network_metadata=None,
    ):  # noqa: E501
        """TsoaPartialNetworkObject_ - a model defined in Swagger"""  # noqa: E501
        self._organization_id = None
        self._user_id = None
        self._agent_gateway_id = None
        self._network_key = None
        self._network_type = None
        self._network_name = None
        self._network_disable_sdn_connections = None
        self._network_metadata = None
        self.discriminator = None
        if organization_id is not None:
            self.organization_id = organization_id
        if user_id is not None:
            self.user_id = user_id
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        if network_key is not None:
            self.network_key = network_key
        if network_type is not None:
            self.network_type = network_type
        if network_name is not None:
            self.network_name = network_name
        if network_disable_sdn_connections is not None:
            self.network_disable_sdn_connections = network_disable_sdn_connections
        if network_metadata is not None:
            self.network_metadata = network_metadata

    @property
    def organization_id(self):
        """Gets the organization_id of this TsoaPartialNetworkObject_.  # noqa: E501


        :return: The organization_id of this TsoaPartialNetworkObject_.  # noqa: E501
        :rtype: float
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this TsoaPartialNetworkObject_.


        :param organization_id: The organization_id of this TsoaPartialNetworkObject_.  # noqa: E501
        :type: float
        """

        self._organization_id = organization_id

    @property
    def user_id(self):
        """Gets the user_id of this TsoaPartialNetworkObject_.  # noqa: E501


        :return: The user_id of this TsoaPartialNetworkObject_.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TsoaPartialNetworkObject_.


        :param user_id: The user_id of this TsoaPartialNetworkObject_.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def agent_gateway_id(self):
        """Gets the agent_gateway_id of this TsoaPartialNetworkObject_.  # noqa: E501


        :return: The agent_gateway_id of this TsoaPartialNetworkObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        """Sets the agent_gateway_id of this TsoaPartialNetworkObject_.


        :param agent_gateway_id: The agent_gateway_id of this TsoaPartialNetworkObject_.  # noqa: E501
        :type: float
        """

        self._agent_gateway_id = agent_gateway_id

    @property
    def network_key(self):
        """Gets the network_key of this TsoaPartialNetworkObject_.  # noqa: E501


        :return: The network_key of this TsoaPartialNetworkObject_.  # noqa: E501
        :rtype: str
        """
        return self._network_key

    @network_key.setter
    def network_key(self, network_key):
        """Sets the network_key of this TsoaPartialNetworkObject_.


        :param network_key: The network_key of this TsoaPartialNetworkObject_.  # noqa: E501
        :type: str
        """

        self._network_key = network_key

    @property
    def network_type(self):
        """Gets the network_type of this TsoaPartialNetworkObject_.  # noqa: E501


        :return: The network_type of this TsoaPartialNetworkObject_.  # noqa: E501
        :rtype: NetworkType
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this TsoaPartialNetworkObject_.


        :param network_type: The network_type of this TsoaPartialNetworkObject_.  # noqa: E501
        :type: NetworkType
        """

        self._network_type = network_type

    @property
    def network_name(self):
        """Gets the network_name of this TsoaPartialNetworkObject_.  # noqa: E501


        :return: The network_name of this TsoaPartialNetworkObject_.  # noqa: E501
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        """Sets the network_name of this TsoaPartialNetworkObject_.


        :param network_name: The network_name of this TsoaPartialNetworkObject_.  # noqa: E501
        :type: str
        """

        self._network_name = network_name

    @property
    def network_disable_sdn_connections(self):
        """Gets the network_disable_sdn_connections of this TsoaPartialNetworkObject_.  # noqa: E501


        :return: The network_disable_sdn_connections of this TsoaPartialNetworkObject_.  # noqa: E501
        :rtype: bool
        """
        return self._network_disable_sdn_connections

    @network_disable_sdn_connections.setter
    def network_disable_sdn_connections(self, network_disable_sdn_connections):
        """Sets the network_disable_sdn_connections of this TsoaPartialNetworkObject_.


        :param network_disable_sdn_connections: The network_disable_sdn_connections of this TsoaPartialNetworkObject_.  # noqa: E501
        :type: bool
        """

        self._network_disable_sdn_connections = network_disable_sdn_connections

    @property
    def network_metadata(self):
        """Gets the network_metadata of this TsoaPartialNetworkObject_.  # noqa: E501


        :return: The network_metadata of this TsoaPartialNetworkObject_.  # noqa: E501
        :rtype: NetworkMetadata
        """
        return self._network_metadata

    @network_metadata.setter
    def network_metadata(self, network_metadata):
        """Sets the network_metadata of this TsoaPartialNetworkObject_.


        :param network_metadata: The network_metadata of this TsoaPartialNetworkObject_.  # noqa: E501
        :type: NetworkMetadata
        """

        self._network_metadata = network_metadata

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
        if issubclass(TsoaPartialNetworkObject_, dict):
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
        if not isinstance(other, TsoaPartialNetworkObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
