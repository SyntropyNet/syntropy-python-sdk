# coding: utf-8

"""
    syntropy-controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class VppCallableObjectArgs9(object):
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
    swagger_types = {"dst_addr": "str", "src_addr": "str", "ifname": "str"}

    attribute_map = {"dst_addr": "dst_addr", "src_addr": "src_addr", "ifname": "ifname"}

    def __init__(self, dst_addr=None, src_addr=None, ifname=None):  # noqa: E501
        """VppCallableObjectArgs9 - a model defined in Swagger"""  # noqa: E501
        self._dst_addr = None
        self._src_addr = None
        self._ifname = None
        self.discriminator = None
        self.dst_addr = dst_addr
        self.src_addr = src_addr
        self.ifname = ifname

    @property
    def dst_addr(self):
        """Gets the dst_addr of this VppCallableObjectArgs9.  # noqa: E501


        :return: The dst_addr of this VppCallableObjectArgs9.  # noqa: E501
        :rtype: str
        """
        return self._dst_addr

    @dst_addr.setter
    def dst_addr(self, dst_addr):
        """Sets the dst_addr of this VppCallableObjectArgs9.


        :param dst_addr: The dst_addr of this VppCallableObjectArgs9.  # noqa: E501
        :type: str
        """
        if dst_addr is None:
            raise ValueError(
                "Invalid value for `dst_addr`, must not be `None`"
            )  # noqa: E501

        self._dst_addr = dst_addr

    @property
    def src_addr(self):
        """Gets the src_addr of this VppCallableObjectArgs9.  # noqa: E501


        :return: The src_addr of this VppCallableObjectArgs9.  # noqa: E501
        :rtype: str
        """
        return self._src_addr

    @src_addr.setter
    def src_addr(self, src_addr):
        """Sets the src_addr of this VppCallableObjectArgs9.


        :param src_addr: The src_addr of this VppCallableObjectArgs9.  # noqa: E501
        :type: str
        """
        if src_addr is None:
            raise ValueError(
                "Invalid value for `src_addr`, must not be `None`"
            )  # noqa: E501

        self._src_addr = src_addr

    @property
    def ifname(self):
        """Gets the ifname of this VppCallableObjectArgs9.  # noqa: E501


        :return: The ifname of this VppCallableObjectArgs9.  # noqa: E501
        :rtype: str
        """
        return self._ifname

    @ifname.setter
    def ifname(self, ifname):
        """Sets the ifname of this VppCallableObjectArgs9.


        :param ifname: The ifname of this VppCallableObjectArgs9.  # noqa: E501
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
        if issubclass(VppCallableObjectArgs9, dict):
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
        if not isinstance(other, VppCallableObjectArgs9):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
