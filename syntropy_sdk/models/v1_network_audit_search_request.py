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


class V1NetworkAuditSearchRequest(object):
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
        "action": "list[str]",
        "_from": "str",
        "performed_by": "str",
        "skip": "int",
        "source": "list[str]",
        "take": "int",
        "to": "str",
        "type": "list[str]",
    }

    attribute_map = {
        "action": "action",
        "_from": "from",
        "performed_by": "performed_by",
        "skip": "skip",
        "source": "source",
        "take": "take",
        "to": "to",
        "type": "type",
    }

    def __init__(
        self,
        action=None,
        _from=None,
        performed_by=None,
        skip=None,
        source=None,
        take=None,
        to=None,
        type=None,
    ):  # noqa: E501
        """V1NetworkAuditSearchRequest - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self.__from = None
        self._performed_by = None
        self._skip = None
        self._source = None
        self._take = None
        self._to = None
        self._type = None
        self.discriminator = None
        if action is not None:
            self.action = action
        self._from = _from
        if performed_by is not None:
            self.performed_by = performed_by
        if skip is not None:
            self.skip = skip
        if source is not None:
            self.source = source
        if take is not None:
            self.take = take
        self.to = to
        if type is not None:
            self.type = type

    @property
    def action(self):
        """Gets the action of this V1NetworkAuditSearchRequest.  # noqa: E501


        :return: The action of this V1NetworkAuditSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this V1NetworkAuditSearchRequest.


        :param action: The action of this V1NetworkAuditSearchRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = [
            "ACTION_CREATED",
            "ACTION_DELETED",
            "ACTION_UPDATED",
        ]  # noqa: E501
        if not set(action).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `action` [{0}], must be a subset of [{1}]".format(  # noqa: E501
                    ", ".join(
                        map(str, set(action) - set(allowed_values))
                    ),  # noqa: E501
                    ", ".join(map(str, allowed_values)),
                )
            )

        self._action = action

    @property
    def _from(self):
        """Gets the _from of this V1NetworkAuditSearchRequest.  # noqa: E501


        :return: The _from of this V1NetworkAuditSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this V1NetworkAuditSearchRequest.


        :param _from: The _from of this V1NetworkAuditSearchRequest.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError(
                "Invalid value for `_from`, must not be `None`"
            )  # noqa: E501

        self.__from = _from

    @property
    def performed_by(self):
        """Gets the performed_by of this V1NetworkAuditSearchRequest.  # noqa: E501


        :return: The performed_by of this V1NetworkAuditSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._performed_by

    @performed_by.setter
    def performed_by(self, performed_by):
        """Sets the performed_by of this V1NetworkAuditSearchRequest.


        :param performed_by: The performed_by of this V1NetworkAuditSearchRequest.  # noqa: E501
        :type: str
        """

        self._performed_by = performed_by

    @property
    def skip(self):
        """Gets the skip of this V1NetworkAuditSearchRequest.  # noqa: E501


        :return: The skip of this V1NetworkAuditSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this V1NetworkAuditSearchRequest.


        :param skip: The skip of this V1NetworkAuditSearchRequest.  # noqa: E501
        :type: int
        """

        self._skip = skip

    @property
    def source(self):
        """Gets the source of this V1NetworkAuditSearchRequest.  # noqa: E501


        :return: The source of this V1NetworkAuditSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1NetworkAuditSearchRequest.


        :param source: The source of this V1NetworkAuditSearchRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["SOURCE_USER", "SOURCE_SYSTEM"]  # noqa: E501
        if not set(source).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `source` [{0}], must be a subset of [{1}]".format(  # noqa: E501
                    ", ".join(
                        map(str, set(source) - set(allowed_values))
                    ),  # noqa: E501
                    ", ".join(map(str, allowed_values)),
                )
            )

        self._source = source

    @property
    def take(self):
        """Gets the take of this V1NetworkAuditSearchRequest.  # noqa: E501


        :return: The take of this V1NetworkAuditSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._take

    @take.setter
    def take(self, take):
        """Sets the take of this V1NetworkAuditSearchRequest.


        :param take: The take of this V1NetworkAuditSearchRequest.  # noqa: E501
        :type: int
        """

        self._take = take

    @property
    def to(self):
        """Gets the to of this V1NetworkAuditSearchRequest.  # noqa: E501


        :return: The to of this V1NetworkAuditSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this V1NetworkAuditSearchRequest.


        :param to: The to of this V1NetworkAuditSearchRequest.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def type(self):
        """Gets the type of this V1NetworkAuditSearchRequest.  # noqa: E501


        :return: The type of this V1NetworkAuditSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1NetworkAuditSearchRequest.


        :param type: The type of this V1NetworkAuditSearchRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = [
            "TYPE_ACCESS_TOKEN",
            "TYPE_AGENT_TOKEN",
            "TYPE_AGENT",
            "TYPE_CONNECTION",
        ]  # noqa: E501
        if not set(type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `type` [{0}], must be a subset of [{1}]".format(  # noqa: E501
                    ", ".join(map(str, set(type) - set(allowed_values))),  # noqa: E501
                    ", ".join(map(str, allowed_values)),
                )
            )

        self._type = type

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
        if issubclass(V1NetworkAuditSearchRequest, dict):
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
        if not isinstance(other, V1NetworkAuditSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
