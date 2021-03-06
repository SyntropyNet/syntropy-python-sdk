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


class PlatformAgentMessageType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    WG_CONF = "WG_CONF"
    GET_INFO = "GET_INFO"
    NETWORK_INFO = "NETWORK_INFO"
    LOGGER = "LOGGER"
    CONFIG_INFO = "CONFIG_INFO"
    IFACES_PEERS_BW_DATA = "IFACES_PEERS_BW_DATA"
    IFACES_BW_DATA = "IFACES_BW_DATA"
    AUTO_PING = "AUTO_PING"
    GET_CONFIG_INFO = "GET_CONFIG_INFO"
    UPDATE_AGENT_CONFIG = "UPDATE_AGENT_CONFIG"
    HW_SERVICE_INFO = "HW_SERVICE_INFO"
    CONTAINER_INFO = "CONTAINER_INFO"
    KUBERNETES_SERVICE_INFO = "KUBERNETES_SERVICE_INFO"
    WG_ROUTE_STATUS = "WG_ROUTE_STATUS"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}

    attribute_map = {}

    def __init__(self):  # noqa: E501
        """PlatformAgentMessageType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(PlatformAgentMessageType, dict):
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
        if not isinstance(other, PlatformAgentMessageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
