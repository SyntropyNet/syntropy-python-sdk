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


class WgRemovePeerArgs(object):
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
    swagger_types = {"allowed_ips": "list[str]", "public_key": "str", "ifname": "str"}

    attribute_map = {
        "allowed_ips": "allowed_ips",
        "public_key": "public_key",
        "ifname": "ifname",
    }

    def __init__(self, allowed_ips=None, public_key=None, ifname=None):  # noqa: E501
        """WgRemovePeerArgs - a model defined in Swagger"""  # noqa: E501
        self._allowed_ips = None
        self._public_key = None
        self._ifname = None
        self.discriminator = None
        self.allowed_ips = allowed_ips
        self.public_key = public_key
        self.ifname = ifname

    @property
    def allowed_ips(self):
        """Gets the allowed_ips of this WgRemovePeerArgs.  # noqa: E501


        :return: The allowed_ips of this WgRemovePeerArgs.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_ips

    @allowed_ips.setter
    def allowed_ips(self, allowed_ips):
        """Sets the allowed_ips of this WgRemovePeerArgs.


        :param allowed_ips: The allowed_ips of this WgRemovePeerArgs.  # noqa: E501
        :type: list[str]
        """
        if allowed_ips is None:
            raise ValueError(
                "Invalid value for `allowed_ips`, must not be `None`"
            )  # noqa: E501

        self._allowed_ips = allowed_ips

    @property
    def public_key(self):
        """Gets the public_key of this WgRemovePeerArgs.  # noqa: E501


        :return: The public_key of this WgRemovePeerArgs.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this WgRemovePeerArgs.


        :param public_key: The public_key of this WgRemovePeerArgs.  # noqa: E501
        :type: str
        """
        if public_key is None:
            raise ValueError(
                "Invalid value for `public_key`, must not be `None`"
            )  # noqa: E501

        self._public_key = public_key

    @property
    def ifname(self):
        """Gets the ifname of this WgRemovePeerArgs.  # noqa: E501


        :return: The ifname of this WgRemovePeerArgs.  # noqa: E501
        :rtype: str
        """
        return self._ifname

    @ifname.setter
    def ifname(self, ifname):
        """Sets the ifname of this WgRemovePeerArgs.


        :param ifname: The ifname of this WgRemovePeerArgs.  # noqa: E501
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
        if issubclass(WgRemovePeerArgs, dict):
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
        if not isinstance(other, WgRemovePeerArgs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
