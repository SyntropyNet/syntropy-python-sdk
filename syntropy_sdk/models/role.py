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


class Role(object):
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
        "role_id": "float",
        "role_name": "str",
        "users": "list[User]",
        "user_workspaces": "list[UserWorkspace]",
        "workspace_invitations": "list[WorkspaceInvitation]",
        "permissions": "list[Permission]",
    }

    attribute_map = {
        "role_id": "role_id",
        "role_name": "role_name",
        "users": "users",
        "user_workspaces": "user_workspaces",
        "workspace_invitations": "workspace_invitations",
        "permissions": "permissions",
    }

    def __init__(
        self,
        role_id=None,
        role_name=None,
        users=None,
        user_workspaces=None,
        workspace_invitations=None,
        permissions=None,
    ):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501
        self._role_id = None
        self._role_name = None
        self._users = None
        self._user_workspaces = None
        self._workspace_invitations = None
        self._permissions = None
        self.discriminator = None
        self.role_id = role_id
        self.role_name = role_name
        if users is not None:
            self.users = users
        if user_workspaces is not None:
            self.user_workspaces = user_workspaces
        if workspace_invitations is not None:
            self.workspace_invitations = workspace_invitations
        if permissions is not None:
            self.permissions = permissions

    @property
    def role_id(self):
        """Gets the role_id of this Role.  # noqa: E501


        :return: The role_id of this Role.  # noqa: E501
        :rtype: float
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this Role.


        :param role_id: The role_id of this Role.  # noqa: E501
        :type: float
        """
        if role_id is None:
            raise ValueError(
                "Invalid value for `role_id`, must not be `None`"
            )  # noqa: E501

        self._role_id = role_id

    @property
    def role_name(self):
        """Gets the role_name of this Role.  # noqa: E501


        :return: The role_name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this Role.


        :param role_name: The role_name of this Role.  # noqa: E501
        :type: str
        """
        if role_name is None:
            raise ValueError(
                "Invalid value for `role_name`, must not be `None`"
            )  # noqa: E501

        self._role_name = role_name

    @property
    def users(self):
        """Gets the users of this Role.  # noqa: E501


        :return: The users of this Role.  # noqa: E501
        :rtype: list[User]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Role.


        :param users: The users of this Role.  # noqa: E501
        :type: list[User]
        """

        self._users = users

    @property
    def user_workspaces(self):
        """Gets the user_workspaces of this Role.  # noqa: E501


        :return: The user_workspaces of this Role.  # noqa: E501
        :rtype: list[UserWorkspace]
        """
        return self._user_workspaces

    @user_workspaces.setter
    def user_workspaces(self, user_workspaces):
        """Sets the user_workspaces of this Role.


        :param user_workspaces: The user_workspaces of this Role.  # noqa: E501
        :type: list[UserWorkspace]
        """

        self._user_workspaces = user_workspaces

    @property
    def workspace_invitations(self):
        """Gets the workspace_invitations of this Role.  # noqa: E501


        :return: The workspace_invitations of this Role.  # noqa: E501
        :rtype: list[WorkspaceInvitation]
        """
        return self._workspace_invitations

    @workspace_invitations.setter
    def workspace_invitations(self, workspace_invitations):
        """Sets the workspace_invitations of this Role.


        :param workspace_invitations: The workspace_invitations of this Role.  # noqa: E501
        :type: list[WorkspaceInvitation]
        """

        self._workspace_invitations = workspace_invitations

    @property
    def permissions(self):
        """Gets the permissions of this Role.  # noqa: E501


        :return: The permissions of this Role.  # noqa: E501
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Role.


        :param permissions: The permissions of this Role.  # noqa: E501
        :type: list[Permission]
        """

        self._permissions = permissions

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other