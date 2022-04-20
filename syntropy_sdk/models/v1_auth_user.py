# coding: utf-8

"""
    Syntropy network API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@syntropynet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class V1AuthUser(object):
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
        "user_id": "int",
        "user_email": "str",
        "user_settings": "UserSettings",
        "user_scopes": "list[str]",
    }

    attribute_map = {
        "user_id": "user_id",
        "user_email": "user_email",
        "user_settings": "user_settings",
        "user_scopes": "user_scopes",
    }

    def __init__(
        self, user_id=None, user_email=None, user_settings=None, user_scopes=None
    ):  # noqa: E501
        """V1AuthUser - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._user_email = None
        self._user_settings = None
        self._user_scopes = None
        self.discriminator = None
        self.user_id = user_id
        self.user_email = user_email
        self.user_settings = user_settings
        self.user_scopes = user_scopes

    @property
    def user_id(self):
        """Gets the user_id of this V1AuthUser.  # noqa: E501


        :return: The user_id of this V1AuthUser.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this V1AuthUser.


        :param user_id: The user_id of this V1AuthUser.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def user_email(self):
        """Gets the user_email of this V1AuthUser.  # noqa: E501


        :return: The user_email of this V1AuthUser.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this V1AuthUser.


        :param user_email: The user_email of this V1AuthUser.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError(
                "Invalid value for `user_email`, must not be `None`"
            )  # noqa: E501

        self._user_email = user_email

    @property
    def user_settings(self):
        """Gets the user_settings of this V1AuthUser.  # noqa: E501


        :return: The user_settings of this V1AuthUser.  # noqa: E501
        :rtype: UserSettings
        """
        return self._user_settings

    @user_settings.setter
    def user_settings(self, user_settings):
        """Sets the user_settings of this V1AuthUser.


        :param user_settings: The user_settings of this V1AuthUser.  # noqa: E501
        :type: UserSettings
        """
        if user_settings is None:
            raise ValueError(
                "Invalid value for `user_settings`, must not be `None`"
            )  # noqa: E501

        self._user_settings = user_settings

    @property
    def user_scopes(self):
        """Gets the user_scopes of this V1AuthUser.  # noqa: E501


        :return: The user_scopes of this V1AuthUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_scopes

    @user_scopes.setter
    def user_scopes(self, user_scopes):
        """Sets the user_scopes of this V1AuthUser.


        :param user_scopes: The user_scopes of this V1AuthUser.  # noqa: E501
        :type: list[str]
        """
        if user_scopes is None:
            raise ValueError(
                "Invalid value for `user_scopes`, must not be `None`"
            )  # noqa: E501

        self._user_scopes = user_scopes

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
        if issubclass(V1AuthUser, dict):
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
        if not isinstance(other, V1AuthUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other