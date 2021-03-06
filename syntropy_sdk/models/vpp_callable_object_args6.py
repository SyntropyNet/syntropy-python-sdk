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


class VppCallableObjectArgs6(object):
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
        "enable": "bool",
        "port_range": "str",
        "addr": "str",
        "ifname": "str",
    }

    attribute_map = {
        "enable": "enable",
        "port_range": "port_range",
        "addr": "addr",
        "ifname": "ifname",
    }

    def __init__(
        self, enable=None, port_range=None, addr=None, ifname=None
    ):  # noqa: E501
        """VppCallableObjectArgs6 - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._port_range = None
        self._addr = None
        self._ifname = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if port_range is not None:
            self.port_range = port_range
        self.addr = addr
        self.ifname = ifname

    @property
    def enable(self):
        """Gets the enable of this VppCallableObjectArgs6.  # noqa: E501


        :return: The enable of this VppCallableObjectArgs6.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this VppCallableObjectArgs6.


        :param enable: The enable of this VppCallableObjectArgs6.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def port_range(self):
        """Gets the port_range of this VppCallableObjectArgs6.  # noqa: E501


        :return: The port_range of this VppCallableObjectArgs6.  # noqa: E501
        :rtype: str
        """
        return self._port_range

    @port_range.setter
    def port_range(self, port_range):
        """Sets the port_range of this VppCallableObjectArgs6.


        :param port_range: The port_range of this VppCallableObjectArgs6.  # noqa: E501
        :type: str
        """

        self._port_range = port_range

    @property
    def addr(self):
        """Gets the addr of this VppCallableObjectArgs6.  # noqa: E501


        :return: The addr of this VppCallableObjectArgs6.  # noqa: E501
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this VppCallableObjectArgs6.


        :param addr: The addr of this VppCallableObjectArgs6.  # noqa: E501
        :type: str
        """
        if addr is None:
            raise ValueError(
                "Invalid value for `addr`, must not be `None`"
            )  # noqa: E501

        self._addr = addr

    @property
    def ifname(self):
        """Gets the ifname of this VppCallableObjectArgs6.  # noqa: E501


        :return: The ifname of this VppCallableObjectArgs6.  # noqa: E501
        :rtype: str
        """
        return self._ifname

    @ifname.setter
    def ifname(self, ifname):
        """Sets the ifname of this VppCallableObjectArgs6.


        :param ifname: The ifname of this VppCallableObjectArgs6.  # noqa: E501
        :type: str
        """
        if ifname is None:
            raise ValueError(
                "Invalid value for `ifname`, must not be `None`"
            )  # noqa: E501

        self._ifname = ifname

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
        if issubclass(VppCallableObjectArgs6, dict):
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
        if not isinstance(other, VppCallableObjectArgs6):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
