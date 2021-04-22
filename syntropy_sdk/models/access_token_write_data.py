# coding: utf-8

"""
    syntropy-auth-service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AccessTokenWriteData(object):
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
        "permissions": "list[str]",
        "access_token_expiration": "datetime",
        "access_token_name": "str",
        "access_token_description": "str",
    }

    attribute_map = {
        "permissions": "permissions",
        "access_token_expiration": "access_token_expiration",
        "access_token_name": "access_token_name",
        "access_token_description": "access_token_description",
    }

    def __init__(
        self,
        permissions=None,
        access_token_expiration=None,
        access_token_name=None,
        access_token_description=None,
    ):  # noqa: E501
        """AccessTokenWriteData - a model defined in Swagger"""  # noqa: E501
        self._permissions = None
        self._access_token_expiration = None
        self._access_token_name = None
        self._access_token_description = None
        self.discriminator = None
        self.permissions = permissions
        self.access_token_expiration = access_token_expiration
        if access_token_name is not None:
            self.access_token_name = access_token_name
        if access_token_description is not None:
            self.access_token_description = access_token_description

    @property
    def permissions(self):
        """Gets the permissions of this AccessTokenWriteData.  # noqa: E501


        :return: The permissions of this AccessTokenWriteData.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this AccessTokenWriteData.


        :param permissions: The permissions of this AccessTokenWriteData.  # noqa: E501
        :type: list[str]
        """
        if permissions is None:
            raise ValueError(
                "Invalid value for `permissions`, must not be `None`"
            )  # noqa: E501

        self._permissions = permissions

    @property
    def access_token_expiration(self):
        """Gets the access_token_expiration of this AccessTokenWriteData.  # noqa: E501


        :return: The access_token_expiration of this AccessTokenWriteData.  # noqa: E501
        :rtype: datetime
        """
        return self._access_token_expiration

    @access_token_expiration.setter
    def access_token_expiration(self, access_token_expiration):
        """Sets the access_token_expiration of this AccessTokenWriteData.


        :param access_token_expiration: The access_token_expiration of this AccessTokenWriteData.  # noqa: E501
        :type: datetime
        """
        if access_token_expiration is None:
            raise ValueError(
                "Invalid value for `access_token_expiration`, must not be `None`"
            )  # noqa: E501

        self._access_token_expiration = access_token_expiration

    @property
    def access_token_name(self):
        """Gets the access_token_name of this AccessTokenWriteData.  # noqa: E501


        :return: The access_token_name of this AccessTokenWriteData.  # noqa: E501
        :rtype: str
        """
        return self._access_token_name

    @access_token_name.setter
    def access_token_name(self, access_token_name):
        """Sets the access_token_name of this AccessTokenWriteData.


        :param access_token_name: The access_token_name of this AccessTokenWriteData.  # noqa: E501
        :type: str
        """

        self._access_token_name = access_token_name

    @property
    def access_token_description(self):
        """Gets the access_token_description of this AccessTokenWriteData.  # noqa: E501


        :return: The access_token_description of this AccessTokenWriteData.  # noqa: E501
        :rtype: str
        """
        return self._access_token_description

    @access_token_description.setter
    def access_token_description(self, access_token_description):
        """Sets the access_token_description of this AccessTokenWriteData.


        :param access_token_description: The access_token_description of this AccessTokenWriteData.  # noqa: E501
        :type: str
        """

        self._access_token_description = access_token_description

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
        if issubclass(AccessTokenWriteData, dict):
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
        if not isinstance(other, AccessTokenWriteData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
