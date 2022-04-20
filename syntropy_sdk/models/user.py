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


class User(object):
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
        "user_email": "str",
        "user_password": "str",
        "user_id": "float",
        "user_created_at": "datetime",
        "user_updated_at": "datetime",
        "user_settings": "UserSettings",
        "workspace_default_id": "float",
        "permissions": "list[Permission]",
        "user_workspaces": "list[UserWorkspace]",
        "role": "Role",
        "default_workspace": "Workspace",
    }

    attribute_map = {
        "user_email": "user_email",
        "user_password": "user_password",
        "user_id": "user_id",
        "user_created_at": "user_created_at",
        "user_updated_at": "user_updated_at",
        "user_settings": "user_settings",
        "workspace_default_id": "workspace_default_id",
        "permissions": "permissions",
        "user_workspaces": "user_workspaces",
        "role": "role",
        "default_workspace": "default_workspace",
    }

    def __init__(
        self,
        user_email=None,
        user_password=None,
        user_id=None,
        user_created_at=None,
        user_updated_at=None,
        user_settings=None,
        workspace_default_id=None,
        permissions=None,
        user_workspaces=None,
        role=None,
        default_workspace=None,
    ):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._user_email = None
        self._user_password = None
        self._user_id = None
        self._user_created_at = None
        self._user_updated_at = None
        self._user_settings = None
        self._workspace_default_id = None
        self._permissions = None
        self._user_workspaces = None
        self._role = None
        self._default_workspace = None
        self.discriminator = None
        self.user_email = user_email
        self.user_password = user_password
        self.user_id = user_id
        self.user_created_at = user_created_at
        self.user_updated_at = user_updated_at
        self.user_settings = user_settings
        if workspace_default_id is not None:
            self.workspace_default_id = workspace_default_id
        if permissions is not None:
            self.permissions = permissions
        self.user_workspaces = user_workspaces
        if role is not None:
            self.role = role
        self.default_workspace = default_workspace

    @property
    def user_email(self):
        """Gets the user_email of this User.  # noqa: E501


        :return: The user_email of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this User.


        :param user_email: The user_email of this User.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError(
                "Invalid value for `user_email`, must not be `None`"
            )  # noqa: E501

        self._user_email = user_email

    @property
    def user_password(self):
        """Gets the user_password of this User.  # noqa: E501


        :return: The user_password of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """Sets the user_password of this User.


        :param user_password: The user_password of this User.  # noqa: E501
        :type: str
        """
        if user_password is None:
            raise ValueError(
                "Invalid value for `user_password`, must not be `None`"
            )  # noqa: E501

        self._user_password = user_password

    @property
    def user_id(self):
        """Gets the user_id of this User.  # noqa: E501


        :return: The user_id of this User.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this User.


        :param user_id: The user_id of this User.  # noqa: E501
        :type: float
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def user_created_at(self):
        """Gets the user_created_at of this User.  # noqa: E501


        :return: The user_created_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._user_created_at

    @user_created_at.setter
    def user_created_at(self, user_created_at):
        """Sets the user_created_at of this User.


        :param user_created_at: The user_created_at of this User.  # noqa: E501
        :type: datetime
        """
        if user_created_at is None:
            raise ValueError(
                "Invalid value for `user_created_at`, must not be `None`"
            )  # noqa: E501

        self._user_created_at = user_created_at

    @property
    def user_updated_at(self):
        """Gets the user_updated_at of this User.  # noqa: E501


        :return: The user_updated_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._user_updated_at

    @user_updated_at.setter
    def user_updated_at(self, user_updated_at):
        """Sets the user_updated_at of this User.


        :param user_updated_at: The user_updated_at of this User.  # noqa: E501
        :type: datetime
        """
        if user_updated_at is None:
            raise ValueError(
                "Invalid value for `user_updated_at`, must not be `None`"
            )  # noqa: E501

        self._user_updated_at = user_updated_at

    @property
    def user_settings(self):
        """Gets the user_settings of this User.  # noqa: E501


        :return: The user_settings of this User.  # noqa: E501
        :rtype: UserSettings
        """
        return self._user_settings

    @user_settings.setter
    def user_settings(self, user_settings):
        """Sets the user_settings of this User.


        :param user_settings: The user_settings of this User.  # noqa: E501
        :type: UserSettings
        """
        if user_settings is None:
            raise ValueError(
                "Invalid value for `user_settings`, must not be `None`"
            )  # noqa: E501

        self._user_settings = user_settings

    @property
    def workspace_default_id(self):
        """Gets the workspace_default_id of this User.  # noqa: E501


        :return: The workspace_default_id of this User.  # noqa: E501
        :rtype: float
        """
        return self._workspace_default_id

    @workspace_default_id.setter
    def workspace_default_id(self, workspace_default_id):
        """Sets the workspace_default_id of this User.


        :param workspace_default_id: The workspace_default_id of this User.  # noqa: E501
        :type: float
        """

        self._workspace_default_id = workspace_default_id

    @property
    def permissions(self):
        """Gets the permissions of this User.  # noqa: E501


        :return: The permissions of this User.  # noqa: E501
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this User.


        :param permissions: The permissions of this User.  # noqa: E501
        :type: list[Permission]
        """

        self._permissions = permissions

    @property
    def user_workspaces(self):
        """Gets the user_workspaces of this User.  # noqa: E501


        :return: The user_workspaces of this User.  # noqa: E501
        :rtype: list[UserWorkspace]
        """
        return self._user_workspaces

    @user_workspaces.setter
    def user_workspaces(self, user_workspaces):
        """Sets the user_workspaces of this User.


        :param user_workspaces: The user_workspaces of this User.  # noqa: E501
        :type: list[UserWorkspace]
        """
        if user_workspaces is None:
            raise ValueError(
                "Invalid value for `user_workspaces`, must not be `None`"
            )  # noqa: E501

        self._user_workspaces = user_workspaces

    @property
    def role(self):
        """Gets the role of this User.  # noqa: E501


        :return: The role of this User.  # noqa: E501
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.


        :param role: The role of this User.  # noqa: E501
        :type: Role
        """

        self._role = role

    @property
    def default_workspace(self):
        """Gets the default_workspace of this User.  # noqa: E501


        :return: The default_workspace of this User.  # noqa: E501
        :rtype: Workspace
        """
        return self._default_workspace

    @default_workspace.setter
    def default_workspace(self, default_workspace):
        """Sets the default_workspace of this User.


        :param default_workspace: The default_workspace of this User.  # noqa: E501
        :type: Workspace
        """
        if default_workspace is None:
            raise ValueError(
                "Invalid value for `default_workspace`, must not be `None`"
            )  # noqa: E501

        self._default_workspace = default_workspace

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
