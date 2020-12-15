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


class VppCallableObjectArgs1(object):
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
        "state": "str",
        "addr": "str",
        "host_ifname": "str",
        "ifname": "str",
    }

    attribute_map = {
        "state": "state",
        "addr": "addr",
        "host_ifname": "host_ifname",
        "ifname": "ifname",
    }

    def __init__(
        self, state=None, addr=None, host_ifname=None, ifname=None
    ):  # noqa: E501
        """VppCallableObjectArgs1 - a model defined in Swagger"""  # noqa: E501
        self._state = None
        self._addr = None
        self._host_ifname = None
        self._ifname = None
        self.discriminator = None
        self.state = state
        self.addr = addr
        self.host_ifname = host_ifname
        self.ifname = ifname

    @property
    def state(self):
        """Gets the state of this VppCallableObjectArgs1.  # noqa: E501


        :return: The state of this VppCallableObjectArgs1.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VppCallableObjectArgs1.


        :param state: The state of this VppCallableObjectArgs1.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError(
                "Invalid value for `state`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["both"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}".format(  # noqa: E501
                    state, allowed_values
                )
            )

        self._state = state

    @property
    def addr(self):
        """Gets the addr of this VppCallableObjectArgs1.  # noqa: E501


        :return: The addr of this VppCallableObjectArgs1.  # noqa: E501
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this VppCallableObjectArgs1.


        :param addr: The addr of this VppCallableObjectArgs1.  # noqa: E501
        :type: str
        """
        if addr is None:
            raise ValueError(
                "Invalid value for `addr`, must not be `None`"
            )  # noqa: E501

        self._addr = addr

    @property
    def host_ifname(self):
        """Gets the host_ifname of this VppCallableObjectArgs1.  # noqa: E501


        :return: The host_ifname of this VppCallableObjectArgs1.  # noqa: E501
        :rtype: str
        """
        return self._host_ifname

    @host_ifname.setter
    def host_ifname(self, host_ifname):
        """Sets the host_ifname of this VppCallableObjectArgs1.


        :param host_ifname: The host_ifname of this VppCallableObjectArgs1.  # noqa: E501
        :type: str
        """
        if host_ifname is None:
            raise ValueError(
                "Invalid value for `host_ifname`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["vpp1out"]  # noqa: E501
        if host_ifname not in allowed_values:
            raise ValueError(
                "Invalid value for `host_ifname` ({0}), must be one of {1}".format(  # noqa: E501
                    host_ifname, allowed_values
                )
            )

        self._host_ifname = host_ifname

    @property
    def ifname(self):
        """Gets the ifname of this VppCallableObjectArgs1.  # noqa: E501


        :return: The ifname of this VppCallableObjectArgs1.  # noqa: E501
        :rtype: str
        """
        return self._ifname

    @ifname.setter
    def ifname(self, ifname):
        """Sets the ifname of this VppCallableObjectArgs1.


        :param ifname: The ifname of this VppCallableObjectArgs1.  # noqa: E501
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
        if issubclass(VppCallableObjectArgs1, dict):
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
        if not isinstance(other, VppCallableObjectArgs1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
