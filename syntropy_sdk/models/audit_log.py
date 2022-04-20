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


class AuditLog(object):
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
        "action_type": "str",
        "parameters": "str",
        "performed_by": "str",
        "record_type": "str",
        "source_type": "str",
        "timestamp": "str",
        "user_id": "int",
        "workspace_id": "int",
    }

    attribute_map = {
        "action_type": "action_type",
        "parameters": "parameters",
        "performed_by": "performed_by",
        "record_type": "record_type",
        "source_type": "source_type",
        "timestamp": "timestamp",
        "user_id": "user_id",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        action_type=None,
        parameters=None,
        performed_by=None,
        record_type=None,
        source_type=None,
        timestamp=None,
        user_id=None,
        workspace_id=None,
    ):  # noqa: E501
        """AuditLog - a model defined in Swagger"""  # noqa: E501
        self._action_type = None
        self._parameters = None
        self._performed_by = None
        self._record_type = None
        self._source_type = None
        self._timestamp = None
        self._user_id = None
        self._workspace_id = None
        self.discriminator = None
        self.action_type = action_type
        self.parameters = parameters
        self.performed_by = performed_by
        self.record_type = record_type
        self.source_type = source_type
        self.timestamp = timestamp
        self.user_id = user_id
        self.workspace_id = workspace_id

    @property
    def action_type(self):
        """Gets the action_type of this AuditLog.  # noqa: E501


        :return: The action_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this AuditLog.


        :param action_type: The action_type of this AuditLog.  # noqa: E501
        :type: str
        """
        if action_type is None:
            raise ValueError(
                "Invalid value for `action_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "ACTION_CREATED",
            "ACTION_DELETED",
            "ACTION_UPDATED",
        ]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}".format(  # noqa: E501
                    action_type, allowed_values
                )
            )

        self._action_type = action_type

    @property
    def parameters(self):
        """Gets the parameters of this AuditLog.  # noqa: E501


        :return: The parameters of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this AuditLog.


        :param parameters: The parameters of this AuditLog.  # noqa: E501
        :type: str
        """
        if parameters is None:
            raise ValueError(
                "Invalid value for `parameters`, must not be `None`"
            )  # noqa: E501

        self._parameters = parameters

    @property
    def performed_by(self):
        """Gets the performed_by of this AuditLog.  # noqa: E501


        :return: The performed_by of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._performed_by

    @performed_by.setter
    def performed_by(self, performed_by):
        """Sets the performed_by of this AuditLog.


        :param performed_by: The performed_by of this AuditLog.  # noqa: E501
        :type: str
        """
        if performed_by is None:
            raise ValueError(
                "Invalid value for `performed_by`, must not be `None`"
            )  # noqa: E501

        self._performed_by = performed_by

    @property
    def record_type(self):
        """Gets the record_type of this AuditLog.  # noqa: E501


        :return: The record_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this AuditLog.


        :param record_type: The record_type of this AuditLog.  # noqa: E501
        :type: str
        """
        if record_type is None:
            raise ValueError(
                "Invalid value for `record_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "TYPE_ACCESS_TOKEN",
            "TYPE_AGENT_TOKEN",
            "TYPE_AGENT",
            "TYPE_CONNECTION",
            "TYPE_SERVICE",
        ]  # noqa: E501
        if record_type not in allowed_values:
            raise ValueError(
                "Invalid value for `record_type` ({0}), must be one of {1}".format(  # noqa: E501
                    record_type, allowed_values
                )
            )

        self._record_type = record_type

    @property
    def source_type(self):
        """Gets the source_type of this AuditLog.  # noqa: E501


        :return: The source_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this AuditLog.


        :param source_type: The source_type of this AuditLog.  # noqa: E501
        :type: str
        """
        if source_type is None:
            raise ValueError(
                "Invalid value for `source_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["SOURCE_USER", "SOURCE_SYSTEM"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}".format(  # noqa: E501
                    source_type, allowed_values
                )
            )

        self._source_type = source_type

    @property
    def timestamp(self):
        """Gets the timestamp of this AuditLog.  # noqa: E501


        :return: The timestamp of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AuditLog.


        :param timestamp: The timestamp of this AuditLog.  # noqa: E501
        :type: str
        """
        if timestamp is None:
            raise ValueError(
                "Invalid value for `timestamp`, must not be `None`"
            )  # noqa: E501

        self._timestamp = timestamp

    @property
    def user_id(self):
        """Gets the user_id of this AuditLog.  # noqa: E501


        :return: The user_id of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuditLog.


        :param user_id: The user_id of this AuditLog.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this AuditLog.  # noqa: E501


        :return: The workspace_id of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this AuditLog.


        :param workspace_id: The workspace_id of this AuditLog.  # noqa: E501
        :type: int
        """
        if workspace_id is None:
            raise ValueError(
                "Invalid value for `workspace_id`, must not be `None`"
            )  # noqa: E501

        self._workspace_id = workspace_id

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
        if issubclass(AuditLog, dict):
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
        if not isinstance(other, AuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other