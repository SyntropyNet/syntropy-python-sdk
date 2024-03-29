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


class UserWithRole(object):
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
        "user_id": "float",
        "user_email": "str",
        "role_name": "WorkspaceRoleName",
        "user_2fa_enabled": "bool",
        "user_workspace_created_at": "datetime",
    }

    attribute_map = {
        "user_id": "user_id",
        "user_email": "user_email",
        "role_name": "role_name",
        "user_2fa_enabled": "user_2fa_enabled",
        "user_workspace_created_at": "user_workspace_created_at",
    }

    def __init__(
        self,
        user_id=None,
        user_email=None,
        role_name=None,
        user_2fa_enabled=None,
        user_workspace_created_at=None,
    ):  # noqa: E501
        """UserWithRole - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._user_email = None
        self._role_name = None
        self._user_2fa_enabled = None
        self._user_workspace_created_at = None
        self.discriminator = None
        self.user_id = user_id
        self.user_email = user_email
        self.role_name = role_name
        if user_2fa_enabled is not None:
            self.user_2fa_enabled = user_2fa_enabled
        self.user_workspace_created_at = user_workspace_created_at

    @property
    def user_id(self):
        """Gets the user_id of this UserWithRole.  # noqa: E501


        :return: The user_id of this UserWithRole.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserWithRole.


        :param user_id: The user_id of this UserWithRole.  # noqa: E501
        :type: float
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def user_email(self):
        """Gets the user_email of this UserWithRole.  # noqa: E501


        :return: The user_email of this UserWithRole.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this UserWithRole.


        :param user_email: The user_email of this UserWithRole.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError(
                "Invalid value for `user_email`, must not be `None`"
            )  # noqa: E501

        self._user_email = user_email

    @property
    def role_name(self):
        """Gets the role_name of this UserWithRole.  # noqa: E501


        :return: The role_name of this UserWithRole.  # noqa: E501
        :rtype: WorkspaceRoleName
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this UserWithRole.


        :param role_name: The role_name of this UserWithRole.  # noqa: E501
        :type: WorkspaceRoleName
        """
        if role_name is None:
            raise ValueError(
                "Invalid value for `role_name`, must not be `None`"
            )  # noqa: E501

        self._role_name = role_name

    @property
    def user_2fa_enabled(self):
        """Gets the user_2fa_enabled of this UserWithRole.  # noqa: E501


        :return: The user_2fa_enabled of this UserWithRole.  # noqa: E501
        :rtype: bool
        """
        return self._user_2fa_enabled

    @user_2fa_enabled.setter
    def user_2fa_enabled(self, user_2fa_enabled):
        """Sets the user_2fa_enabled of this UserWithRole.


        :param user_2fa_enabled: The user_2fa_enabled of this UserWithRole.  # noqa: E501
        :type: bool
        """

        self._user_2fa_enabled = user_2fa_enabled

    @property
    def user_workspace_created_at(self):
        """Gets the user_workspace_created_at of this UserWithRole.  # noqa: E501


        :return: The user_workspace_created_at of this UserWithRole.  # noqa: E501
        :rtype: datetime
        """
        return self._user_workspace_created_at

    @user_workspace_created_at.setter
    def user_workspace_created_at(self, user_workspace_created_at):
        """Sets the user_workspace_created_at of this UserWithRole.


        :param user_workspace_created_at: The user_workspace_created_at of this UserWithRole.  # noqa: E501
        :type: datetime
        """
        if user_workspace_created_at is None:
            raise ValueError(
                "Invalid value for `user_workspace_created_at`, must not be `None`"
            )  # noqa: E501

        self._user_workspace_created_at = user_workspace_created_at

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
        if issubclass(UserWithRole, dict):
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
        if not isinstance(other, UserWithRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
