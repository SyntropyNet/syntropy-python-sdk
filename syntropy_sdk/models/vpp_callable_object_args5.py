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


class VppCallableObjectArgs5(object):
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
    swagger_types = {"ext_addr": "str", "local_addr": "str", "ifname": "str"}

    attribute_map = {
        "ext_addr": "ext_addr",
        "local_addr": "local_addr",
        "ifname": "ifname",
    }

    def __init__(self, ext_addr=None, local_addr=None, ifname=None):  # noqa: E501
        """VppCallableObjectArgs5 - a model defined in Swagger"""  # noqa: E501
        self._ext_addr = None
        self._local_addr = None
        self._ifname = None
        self.discriminator = None
        self.ext_addr = ext_addr
        self.local_addr = local_addr
        self.ifname = ifname

    @property
    def ext_addr(self):
        """Gets the ext_addr of this VppCallableObjectArgs5.  # noqa: E501


        :return: The ext_addr of this VppCallableObjectArgs5.  # noqa: E501
        :rtype: str
        """
        return self._ext_addr

    @ext_addr.setter
    def ext_addr(self, ext_addr):
        """Sets the ext_addr of this VppCallableObjectArgs5.


        :param ext_addr: The ext_addr of this VppCallableObjectArgs5.  # noqa: E501
        :type: str
        """
        if ext_addr is None:
            raise ValueError(
                "Invalid value for `ext_addr`, must not be `None`"
            )  # noqa: E501

        self._ext_addr = ext_addr

    @property
    def local_addr(self):
        """Gets the local_addr of this VppCallableObjectArgs5.  # noqa: E501


        :return: The local_addr of this VppCallableObjectArgs5.  # noqa: E501
        :rtype: str
        """
        return self._local_addr

    @local_addr.setter
    def local_addr(self, local_addr):
        """Sets the local_addr of this VppCallableObjectArgs5.


        :param local_addr: The local_addr of this VppCallableObjectArgs5.  # noqa: E501
        :type: str
        """
        if local_addr is None:
            raise ValueError(
                "Invalid value for `local_addr`, must not be `None`"
            )  # noqa: E501

        self._local_addr = local_addr

    @property
    def ifname(self):
        """Gets the ifname of this VppCallableObjectArgs5.  # noqa: E501


        :return: The ifname of this VppCallableObjectArgs5.  # noqa: E501
        :rtype: str
        """
        return self._ifname

    @ifname.setter
    def ifname(self, ifname):
        """Sets the ifname of this VppCallableObjectArgs5.


        :param ifname: The ifname of this VppCallableObjectArgs5.  # noqa: E501
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
        if issubclass(VppCallableObjectArgs5, dict):
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
        if not isinstance(other, VppCallableObjectArgs5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
