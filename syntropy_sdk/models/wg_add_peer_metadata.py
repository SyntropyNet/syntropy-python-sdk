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


class WgAddPeerMetadata(object):
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
        "allowed_ips_info": "list[WgAddPeerMetadataAllowedIpsInfo]",
        "link_tag": "LinkTag",
        "agent_id": "float",
        "connection_id": "float",
        "device_public_ipv4": "str",
        "device_name": "str",
        "device_id": "str",
    }

    attribute_map = {
        "allowed_ips_info": "allowed_ips_info",
        "link_tag": "link_tag",
        "agent_id": "agent_id",
        "connection_id": "connection_id",
        "device_public_ipv4": "device_public_ipv4",
        "device_name": "device_name",
        "device_id": "device_id",
    }

    def __init__(
        self,
        allowed_ips_info=None,
        link_tag=None,
        agent_id=None,
        connection_id=None,
        device_public_ipv4=None,
        device_name=None,
        device_id=None,
    ):  # noqa: E501
        """WgAddPeerMetadata - a model defined in Swagger"""  # noqa: E501
        self._allowed_ips_info = None
        self._link_tag = None
        self._agent_id = None
        self._connection_id = None
        self._device_public_ipv4 = None
        self._device_name = None
        self._device_id = None
        self.discriminator = None
        self.allowed_ips_info = allowed_ips_info
        self.link_tag = link_tag
        self.agent_id = agent_id
        self.connection_id = connection_id
        self.device_public_ipv4 = device_public_ipv4
        self.device_name = device_name
        self.device_id = device_id

    @property
    def allowed_ips_info(self):
        """Gets the allowed_ips_info of this WgAddPeerMetadata.  # noqa: E501


        :return: The allowed_ips_info of this WgAddPeerMetadata.  # noqa: E501
        :rtype: list[WgAddPeerMetadataAllowedIpsInfo]
        """
        return self._allowed_ips_info

    @allowed_ips_info.setter
    def allowed_ips_info(self, allowed_ips_info):
        """Sets the allowed_ips_info of this WgAddPeerMetadata.


        :param allowed_ips_info: The allowed_ips_info of this WgAddPeerMetadata.  # noqa: E501
        :type: list[WgAddPeerMetadataAllowedIpsInfo]
        """
        if allowed_ips_info is None:
            raise ValueError(
                "Invalid value for `allowed_ips_info`, must not be `None`"
            )  # noqa: E501

        self._allowed_ips_info = allowed_ips_info

    @property
    def link_tag(self):
        """Gets the link_tag of this WgAddPeerMetadata.  # noqa: E501


        :return: The link_tag of this WgAddPeerMetadata.  # noqa: E501
        :rtype: LinkTag
        """
        return self._link_tag

    @link_tag.setter
    def link_tag(self, link_tag):
        """Sets the link_tag of this WgAddPeerMetadata.


        :param link_tag: The link_tag of this WgAddPeerMetadata.  # noqa: E501
        :type: LinkTag
        """
        if link_tag is None:
            raise ValueError(
                "Invalid value for `link_tag`, must not be `None`"
            )  # noqa: E501

        self._link_tag = link_tag

    @property
    def agent_id(self):
        """Gets the agent_id of this WgAddPeerMetadata.  # noqa: E501


        :return: The agent_id of this WgAddPeerMetadata.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this WgAddPeerMetadata.


        :param agent_id: The agent_id of this WgAddPeerMetadata.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def connection_id(self):
        """Gets the connection_id of this WgAddPeerMetadata.  # noqa: E501


        :return: The connection_id of this WgAddPeerMetadata.  # noqa: E501
        :rtype: float
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this WgAddPeerMetadata.


        :param connection_id: The connection_id of this WgAddPeerMetadata.  # noqa: E501
        :type: float
        """
        if connection_id is None:
            raise ValueError(
                "Invalid value for `connection_id`, must not be `None`"
            )  # noqa: E501

        self._connection_id = connection_id

    @property
    def device_public_ipv4(self):
        """Gets the device_public_ipv4 of this WgAddPeerMetadata.  # noqa: E501


        :return: The device_public_ipv4 of this WgAddPeerMetadata.  # noqa: E501
        :rtype: str
        """
        return self._device_public_ipv4

    @device_public_ipv4.setter
    def device_public_ipv4(self, device_public_ipv4):
        """Sets the device_public_ipv4 of this WgAddPeerMetadata.


        :param device_public_ipv4: The device_public_ipv4 of this WgAddPeerMetadata.  # noqa: E501
        :type: str
        """
        if device_public_ipv4 is None:
            raise ValueError(
                "Invalid value for `device_public_ipv4`, must not be `None`"
            )  # noqa: E501

        self._device_public_ipv4 = device_public_ipv4

    @property
    def device_name(self):
        """Gets the device_name of this WgAddPeerMetadata.  # noqa: E501


        :return: The device_name of this WgAddPeerMetadata.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this WgAddPeerMetadata.


        :param device_name: The device_name of this WgAddPeerMetadata.  # noqa: E501
        :type: str
        """
        if device_name is None:
            raise ValueError(
                "Invalid value for `device_name`, must not be `None`"
            )  # noqa: E501

        self._device_name = device_name

    @property
    def device_id(self):
        """Gets the device_id of this WgAddPeerMetadata.  # noqa: E501


        :return: The device_id of this WgAddPeerMetadata.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this WgAddPeerMetadata.


        :param device_id: The device_id of this WgAddPeerMetadata.  # noqa: E501
        :type: str
        """
        if device_id is None:
            raise ValueError(
                "Invalid value for `device_id`, must not be `None`"
            )  # noqa: E501

        self._device_id = device_id

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
        if issubclass(WgAddPeerMetadata, dict):
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
        if not isinstance(other, WgAddPeerMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
