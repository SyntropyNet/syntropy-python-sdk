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


class WorkspaceInvitation(object):
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
        "workspace_id": "float",
        "user_email": "str",
        "role_id": "float",
        "user_inviter_id": "float",
        "role_name": "WorkspaceRoleName",
        "workspace_invitation_id": "float",
        "workspace_invitation_created_at": "datetime",
        "workspace_invitation_accepted_at": "datetime",
        "workspace_invitation_declined_at": "datetime",
    }

    attribute_map = {
        "workspace_id": "workspace_id",
        "user_email": "user_email",
        "role_id": "role_id",
        "user_inviter_id": "user_inviter_id",
        "role_name": "role_name",
        "workspace_invitation_id": "workspace_invitation_id",
        "workspace_invitation_created_at": "workspace_invitation_created_at",
        "workspace_invitation_accepted_at": "workspace_invitation_accepted_at",
        "workspace_invitation_declined_at": "workspace_invitation_declined_at",
    }

    def __init__(
        self,
        workspace_id=None,
        user_email=None,
        role_id=None,
        user_inviter_id=None,
        role_name=None,
        workspace_invitation_id=None,
        workspace_invitation_created_at=None,
        workspace_invitation_accepted_at=None,
        workspace_invitation_declined_at=None,
    ):  # noqa: E501
        """WorkspaceInvitation - a model defined in Swagger"""  # noqa: E501
        self._workspace_id = None
        self._user_email = None
        self._role_id = None
        self._user_inviter_id = None
        self._role_name = None
        self._workspace_invitation_id = None
        self._workspace_invitation_created_at = None
        self._workspace_invitation_accepted_at = None
        self._workspace_invitation_declined_at = None
        self.discriminator = None
        self.workspace_id = workspace_id
        self.user_email = user_email
        self.role_id = role_id
        self.user_inviter_id = user_inviter_id
        self.role_name = role_name
        self.workspace_invitation_id = workspace_invitation_id
        self.workspace_invitation_created_at = workspace_invitation_created_at
        self.workspace_invitation_accepted_at = workspace_invitation_accepted_at
        self.workspace_invitation_declined_at = workspace_invitation_declined_at

    @property
    def workspace_id(self):
        """Gets the workspace_id of this WorkspaceInvitation.  # noqa: E501


        :return: The workspace_id of this WorkspaceInvitation.  # noqa: E501
        :rtype: float
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this WorkspaceInvitation.


        :param workspace_id: The workspace_id of this WorkspaceInvitation.  # noqa: E501
        :type: float
        """
        if workspace_id is None:
            raise ValueError(
                "Invalid value for `workspace_id`, must not be `None`"
            )  # noqa: E501

        self._workspace_id = workspace_id

    @property
    def user_email(self):
        """Gets the user_email of this WorkspaceInvitation.  # noqa: E501


        :return: The user_email of this WorkspaceInvitation.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this WorkspaceInvitation.


        :param user_email: The user_email of this WorkspaceInvitation.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError(
                "Invalid value for `user_email`, must not be `None`"
            )  # noqa: E501

        self._user_email = user_email

    @property
    def role_id(self):
        """Gets the role_id of this WorkspaceInvitation.  # noqa: E501


        :return: The role_id of this WorkspaceInvitation.  # noqa: E501
        :rtype: float
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this WorkspaceInvitation.


        :param role_id: The role_id of this WorkspaceInvitation.  # noqa: E501
        :type: float
        """
        if role_id is None:
            raise ValueError(
                "Invalid value for `role_id`, must not be `None`"
            )  # noqa: E501

        self._role_id = role_id

    @property
    def user_inviter_id(self):
        """Gets the user_inviter_id of this WorkspaceInvitation.  # noqa: E501


        :return: The user_inviter_id of this WorkspaceInvitation.  # noqa: E501
        :rtype: float
        """
        return self._user_inviter_id

    @user_inviter_id.setter
    def user_inviter_id(self, user_inviter_id):
        """Sets the user_inviter_id of this WorkspaceInvitation.


        :param user_inviter_id: The user_inviter_id of this WorkspaceInvitation.  # noqa: E501
        :type: float
        """
        if user_inviter_id is None:
            raise ValueError(
                "Invalid value for `user_inviter_id`, must not be `None`"
            )  # noqa: E501

        self._user_inviter_id = user_inviter_id

    @property
    def role_name(self):
        """Gets the role_name of this WorkspaceInvitation.  # noqa: E501


        :return: The role_name of this WorkspaceInvitation.  # noqa: E501
        :rtype: WorkspaceRoleName
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this WorkspaceInvitation.


        :param role_name: The role_name of this WorkspaceInvitation.  # noqa: E501
        :type: WorkspaceRoleName
        """
        if role_name is None:
            raise ValueError(
                "Invalid value for `role_name`, must not be `None`"
            )  # noqa: E501

        self._role_name = role_name

    @property
    def workspace_invitation_id(self):
        """Gets the workspace_invitation_id of this WorkspaceInvitation.  # noqa: E501


        :return: The workspace_invitation_id of this WorkspaceInvitation.  # noqa: E501
        :rtype: float
        """
        return self._workspace_invitation_id

    @workspace_invitation_id.setter
    def workspace_invitation_id(self, workspace_invitation_id):
        """Sets the workspace_invitation_id of this WorkspaceInvitation.


        :param workspace_invitation_id: The workspace_invitation_id of this WorkspaceInvitation.  # noqa: E501
        :type: float
        """
        if workspace_invitation_id is None:
            raise ValueError(
                "Invalid value for `workspace_invitation_id`, must not be `None`"
            )  # noqa: E501

        self._workspace_invitation_id = workspace_invitation_id

    @property
    def workspace_invitation_created_at(self):
        """Gets the workspace_invitation_created_at of this WorkspaceInvitation.  # noqa: E501


        :return: The workspace_invitation_created_at of this WorkspaceInvitation.  # noqa: E501
        :rtype: datetime
        """
        return self._workspace_invitation_created_at

    @workspace_invitation_created_at.setter
    def workspace_invitation_created_at(self, workspace_invitation_created_at):
        """Sets the workspace_invitation_created_at of this WorkspaceInvitation.


        :param workspace_invitation_created_at: The workspace_invitation_created_at of this WorkspaceInvitation.  # noqa: E501
        :type: datetime
        """
        if workspace_invitation_created_at is None:
            raise ValueError(
                "Invalid value for `workspace_invitation_created_at`, must not be `None`"
            )  # noqa: E501

        self._workspace_invitation_created_at = workspace_invitation_created_at

    @property
    def workspace_invitation_accepted_at(self):
        """Gets the workspace_invitation_accepted_at of this WorkspaceInvitation.  # noqa: E501


        :return: The workspace_invitation_accepted_at of this WorkspaceInvitation.  # noqa: E501
        :rtype: datetime
        """
        return self._workspace_invitation_accepted_at

    @workspace_invitation_accepted_at.setter
    def workspace_invitation_accepted_at(self, workspace_invitation_accepted_at):
        """Sets the workspace_invitation_accepted_at of this WorkspaceInvitation.


        :param workspace_invitation_accepted_at: The workspace_invitation_accepted_at of this WorkspaceInvitation.  # noqa: E501
        :type: datetime
        """
        if workspace_invitation_accepted_at is None:
            raise ValueError(
                "Invalid value for `workspace_invitation_accepted_at`, must not be `None`"
            )  # noqa: E501

        self._workspace_invitation_accepted_at = workspace_invitation_accepted_at

    @property
    def workspace_invitation_declined_at(self):
        """Gets the workspace_invitation_declined_at of this WorkspaceInvitation.  # noqa: E501


        :return: The workspace_invitation_declined_at of this WorkspaceInvitation.  # noqa: E501
        :rtype: datetime
        """
        return self._workspace_invitation_declined_at

    @workspace_invitation_declined_at.setter
    def workspace_invitation_declined_at(self, workspace_invitation_declined_at):
        """Sets the workspace_invitation_declined_at of this WorkspaceInvitation.


        :param workspace_invitation_declined_at: The workspace_invitation_declined_at of this WorkspaceInvitation.  # noqa: E501
        :type: datetime
        """
        if workspace_invitation_declined_at is None:
            raise ValueError(
                "Invalid value for `workspace_invitation_declined_at`, must not be `None`"
            )  # noqa: E501

        self._workspace_invitation_declined_at = workspace_invitation_declined_at

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
        if issubclass(WorkspaceInvitation, dict):
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
        if not isinstance(other, WorkspaceInvitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
