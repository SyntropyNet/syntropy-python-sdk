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


class VppCallableObjectArgs4(object):
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
    swagger_types = {"tun_addr": "str", "dst": "str", "src": "str"}

    attribute_map = {"tun_addr": "tun_addr", "dst": "dst", "src": "src"}

    def __init__(self, tun_addr=None, dst=None, src=None):  # noqa: E501
        """VppCallableObjectArgs4 - a model defined in Swagger"""  # noqa: E501
        self._tun_addr = None
        self._dst = None
        self._src = None
        self.discriminator = None
        self.tun_addr = tun_addr
        self.dst = dst
        self.src = src

    @property
    def tun_addr(self):
        """Gets the tun_addr of this VppCallableObjectArgs4.  # noqa: E501


        :return: The tun_addr of this VppCallableObjectArgs4.  # noqa: E501
        :rtype: str
        """
        return self._tun_addr

    @tun_addr.setter
    def tun_addr(self, tun_addr):
        """Sets the tun_addr of this VppCallableObjectArgs4.


        :param tun_addr: The tun_addr of this VppCallableObjectArgs4.  # noqa: E501
        :type: str
        """
        if tun_addr is None:
            raise ValueError(
                "Invalid value for `tun_addr`, must not be `None`"
            )  # noqa: E501

        self._tun_addr = tun_addr

    @property
    def dst(self):
        """Gets the dst of this VppCallableObjectArgs4.  # noqa: E501


        :return: The dst of this VppCallableObjectArgs4.  # noqa: E501
        :rtype: str
        """
        return self._dst

    @dst.setter
    def dst(self, dst):
        """Sets the dst of this VppCallableObjectArgs4.


        :param dst: The dst of this VppCallableObjectArgs4.  # noqa: E501
        :type: str
        """
        if dst is None:
            raise ValueError(
                "Invalid value for `dst`, must not be `None`"
            )  # noqa: E501

        self._dst = dst

    @property
    def src(self):
        """Gets the src of this VppCallableObjectArgs4.  # noqa: E501


        :return: The src of this VppCallableObjectArgs4.  # noqa: E501
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this VppCallableObjectArgs4.


        :param src: The src of this VppCallableObjectArgs4.  # noqa: E501
        :type: str
        """
        if src is None:
            raise ValueError(
                "Invalid value for `src`, must not be `None`"
            )  # noqa: E501

        self._src = src

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
        if issubclass(VppCallableObjectArgs4, dict):
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
        if not isinstance(other, VppCallableObjectArgs4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
