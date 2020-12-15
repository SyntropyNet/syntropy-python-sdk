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


class AppConnectConfigObjectConfigParams(object):
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
        "vpn_endpoint_ip": "str",
        "app_dest_ip_cidrs_str": "str",
        "app_dest_ip_cidrs": "list[str]",
        "vpn_internal_ipv4": "str",
        "vpn_public_key": "str",
        "app_private_key": "str",
        "app_internal_ipv4": "str",
    }

    attribute_map = {
        "vpn_endpoint_ip": "vpn_endpoint_ip",
        "app_dest_ip_cidrs_str": "app_dest_ip_cidrs_str",
        "app_dest_ip_cidrs": "app_dest_ip_cidrs",
        "vpn_internal_ipv4": "vpn_internal_ipv4",
        "vpn_public_key": "vpn_public_key",
        "app_private_key": "app_private_key",
        "app_internal_ipv4": "app_internal_ipv4",
    }

    def __init__(
        self,
        vpn_endpoint_ip=None,
        app_dest_ip_cidrs_str=None,
        app_dest_ip_cidrs=None,
        vpn_internal_ipv4=None,
        vpn_public_key=None,
        app_private_key=None,
        app_internal_ipv4=None,
    ):  # noqa: E501
        """AppConnectConfigObjectConfigParams - a model defined in Swagger"""  # noqa: E501
        self._vpn_endpoint_ip = None
        self._app_dest_ip_cidrs_str = None
        self._app_dest_ip_cidrs = None
        self._vpn_internal_ipv4 = None
        self._vpn_public_key = None
        self._app_private_key = None
        self._app_internal_ipv4 = None
        self.discriminator = None
        self.vpn_endpoint_ip = vpn_endpoint_ip
        self.app_dest_ip_cidrs_str = app_dest_ip_cidrs_str
        self.app_dest_ip_cidrs = app_dest_ip_cidrs
        self.vpn_internal_ipv4 = vpn_internal_ipv4
        self.vpn_public_key = vpn_public_key
        if app_private_key is not None:
            self.app_private_key = app_private_key
        self.app_internal_ipv4 = app_internal_ipv4

    @property
    def vpn_endpoint_ip(self):
        """Gets the vpn_endpoint_ip of this AppConnectConfigObjectConfigParams.  # noqa: E501


        :return: The vpn_endpoint_ip of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :rtype: str
        """
        return self._vpn_endpoint_ip

    @vpn_endpoint_ip.setter
    def vpn_endpoint_ip(self, vpn_endpoint_ip):
        """Sets the vpn_endpoint_ip of this AppConnectConfigObjectConfigParams.


        :param vpn_endpoint_ip: The vpn_endpoint_ip of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :type: str
        """
        if vpn_endpoint_ip is None:
            raise ValueError(
                "Invalid value for `vpn_endpoint_ip`, must not be `None`"
            )  # noqa: E501

        self._vpn_endpoint_ip = vpn_endpoint_ip

    @property
    def app_dest_ip_cidrs_str(self):
        """Gets the app_dest_ip_cidrs_str of this AppConnectConfigObjectConfigParams.  # noqa: E501

        Stringified CIDRs list, i. e.: \"1.1.1.1/32, 2.2.2.2/32\".  # noqa: E501

        :return: The app_dest_ip_cidrs_str of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :rtype: str
        """
        return self._app_dest_ip_cidrs_str

    @app_dest_ip_cidrs_str.setter
    def app_dest_ip_cidrs_str(self, app_dest_ip_cidrs_str):
        """Sets the app_dest_ip_cidrs_str of this AppConnectConfigObjectConfigParams.

        Stringified CIDRs list, i. e.: \"1.1.1.1/32, 2.2.2.2/32\".  # noqa: E501

        :param app_dest_ip_cidrs_str: The app_dest_ip_cidrs_str of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :type: str
        """
        if app_dest_ip_cidrs_str is None:
            raise ValueError(
                "Invalid value for `app_dest_ip_cidrs_str`, must not be `None`"
            )  # noqa: E501

        self._app_dest_ip_cidrs_str = app_dest_ip_cidrs_str

    @property
    def app_dest_ip_cidrs(self):
        """Gets the app_dest_ip_cidrs of this AppConnectConfigObjectConfigParams.  # noqa: E501


        :return: The app_dest_ip_cidrs of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_dest_ip_cidrs

    @app_dest_ip_cidrs.setter
    def app_dest_ip_cidrs(self, app_dest_ip_cidrs):
        """Sets the app_dest_ip_cidrs of this AppConnectConfigObjectConfigParams.


        :param app_dest_ip_cidrs: The app_dest_ip_cidrs of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :type: list[str]
        """
        if app_dest_ip_cidrs is None:
            raise ValueError(
                "Invalid value for `app_dest_ip_cidrs`, must not be `None`"
            )  # noqa: E501

        self._app_dest_ip_cidrs = app_dest_ip_cidrs

    @property
    def vpn_internal_ipv4(self):
        """Gets the vpn_internal_ipv4 of this AppConnectConfigObjectConfigParams.  # noqa: E501


        :return: The vpn_internal_ipv4 of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :rtype: str
        """
        return self._vpn_internal_ipv4

    @vpn_internal_ipv4.setter
    def vpn_internal_ipv4(self, vpn_internal_ipv4):
        """Sets the vpn_internal_ipv4 of this AppConnectConfigObjectConfigParams.


        :param vpn_internal_ipv4: The vpn_internal_ipv4 of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :type: str
        """
        if vpn_internal_ipv4 is None:
            raise ValueError(
                "Invalid value for `vpn_internal_ipv4`, must not be `None`"
            )  # noqa: E501

        self._vpn_internal_ipv4 = vpn_internal_ipv4

    @property
    def vpn_public_key(self):
        """Gets the vpn_public_key of this AppConnectConfigObjectConfigParams.  # noqa: E501


        :return: The vpn_public_key of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :rtype: str
        """
        return self._vpn_public_key

    @vpn_public_key.setter
    def vpn_public_key(self, vpn_public_key):
        """Sets the vpn_public_key of this AppConnectConfigObjectConfigParams.


        :param vpn_public_key: The vpn_public_key of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :type: str
        """
        if vpn_public_key is None:
            raise ValueError(
                "Invalid value for `vpn_public_key`, must not be `None`"
            )  # noqa: E501

        self._vpn_public_key = vpn_public_key

    @property
    def app_private_key(self):
        """Gets the app_private_key of this AppConnectConfigObjectConfigParams.  # noqa: E501


        :return: The app_private_key of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :rtype: str
        """
        return self._app_private_key

    @app_private_key.setter
    def app_private_key(self, app_private_key):
        """Sets the app_private_key of this AppConnectConfigObjectConfigParams.


        :param app_private_key: The app_private_key of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :type: str
        """

        self._app_private_key = app_private_key

    @property
    def app_internal_ipv4(self):
        """Gets the app_internal_ipv4 of this AppConnectConfigObjectConfigParams.  # noqa: E501


        :return: The app_internal_ipv4 of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :rtype: str
        """
        return self._app_internal_ipv4

    @app_internal_ipv4.setter
    def app_internal_ipv4(self, app_internal_ipv4):
        """Sets the app_internal_ipv4 of this AppConnectConfigObjectConfigParams.


        :param app_internal_ipv4: The app_internal_ipv4 of this AppConnectConfigObjectConfigParams.  # noqa: E501
        :type: str
        """
        if app_internal_ipv4 is None:
            raise ValueError(
                "Invalid value for `app_internal_ipv4`, must not be `None`"
            )  # noqa: E501

        self._app_internal_ipv4 = app_internal_ipv4

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
        if issubclass(AppConnectConfigObjectConfigParams, dict):
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
        if not isinstance(other, AppConnectConfigObjectConfigParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
