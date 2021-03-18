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


class ApiKeyDto(object):
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
        "api_key_is_suspended": "bool",
        "api_key_name": "str",
        "api_key_valid_until": "AnyOfApiKeyDtoApiKeyValidUntil",
        "api_key_secret": "str",
        "user_id": "float",
        "api_key_id": "float",
        "api_key_created_at": "AnyOfApiKeyDtoApiKeyCreatedAt",
        "api_key_updated_at": "AnyOfApiKeyDtoApiKeyUpdatedAt",
        "api_key_status": "bool",
    }

    attribute_map = {
        "api_key_is_suspended": "api_key_is_suspended",
        "api_key_name": "api_key_name",
        "api_key_valid_until": "api_key_valid_until",
        "api_key_secret": "api_key_secret",
        "user_id": "user_id",
        "api_key_id": "api_key_id",
        "api_key_created_at": "api_key_created_at",
        "api_key_updated_at": "api_key_updated_at",
        "api_key_status": "api_key_status",
    }

    def __init__(
        self,
        api_key_is_suspended=None,
        api_key_name=None,
        api_key_valid_until=None,
        api_key_secret=None,
        user_id=None,
        api_key_id=None,
        api_key_created_at=None,
        api_key_updated_at=None,
        api_key_status=None,
    ):  # noqa: E501
        """ApiKeyDto - a model defined in Swagger"""  # noqa: E501
        self._api_key_is_suspended = None
        self._api_key_name = None
        self._api_key_valid_until = None
        self._api_key_secret = None
        self._user_id = None
        self._api_key_id = None
        self._api_key_created_at = None
        self._api_key_updated_at = None
        self._api_key_status = None
        self.discriminator = None
        if api_key_is_suspended is not None:
            self.api_key_is_suspended = api_key_is_suspended
        self.api_key_name = api_key_name
        if api_key_valid_until is not None:
            self.api_key_valid_until = api_key_valid_until
        self.api_key_secret = api_key_secret
        self.user_id = user_id
        self.api_key_id = api_key_id
        self.api_key_created_at = api_key_created_at
        self.api_key_updated_at = api_key_updated_at
        self.api_key_status = api_key_status

    @property
    def api_key_is_suspended(self):
        """Gets the api_key_is_suspended of this ApiKeyDto.  # noqa: E501


        :return: The api_key_is_suspended of this ApiKeyDto.  # noqa: E501
        :rtype: bool
        """
        return self._api_key_is_suspended

    @api_key_is_suspended.setter
    def api_key_is_suspended(self, api_key_is_suspended):
        """Sets the api_key_is_suspended of this ApiKeyDto.


        :param api_key_is_suspended: The api_key_is_suspended of this ApiKeyDto.  # noqa: E501
        :type: bool
        """

        self._api_key_is_suspended = api_key_is_suspended

    @property
    def api_key_name(self):
        """Gets the api_key_name of this ApiKeyDto.  # noqa: E501


        :return: The api_key_name of this ApiKeyDto.  # noqa: E501
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        """Sets the api_key_name of this ApiKeyDto.


        :param api_key_name: The api_key_name of this ApiKeyDto.  # noqa: E501
        :type: str
        """
        if api_key_name is None:
            raise ValueError(
                "Invalid value for `api_key_name`, must not be `None`"
            )  # noqa: E501

        self._api_key_name = api_key_name

    @property
    def api_key_valid_until(self):
        """Gets the api_key_valid_until of this ApiKeyDto.  # noqa: E501


        :return: The api_key_valid_until of this ApiKeyDto.  # noqa: E501
        :rtype: AnyOfApiKeyDtoApiKeyValidUntil
        """
        return self._api_key_valid_until

    @api_key_valid_until.setter
    def api_key_valid_until(self, api_key_valid_until):
        """Sets the api_key_valid_until of this ApiKeyDto.


        :param api_key_valid_until: The api_key_valid_until of this ApiKeyDto.  # noqa: E501
        :type: AnyOfApiKeyDtoApiKeyValidUntil
        """

        self._api_key_valid_until = api_key_valid_until

    @property
    def api_key_secret(self):
        """Gets the api_key_secret of this ApiKeyDto.  # noqa: E501


        :return: The api_key_secret of this ApiKeyDto.  # noqa: E501
        :rtype: str
        """
        return self._api_key_secret

    @api_key_secret.setter
    def api_key_secret(self, api_key_secret):
        """Sets the api_key_secret of this ApiKeyDto.


        :param api_key_secret: The api_key_secret of this ApiKeyDto.  # noqa: E501
        :type: str
        """
        if api_key_secret is None:
            raise ValueError(
                "Invalid value for `api_key_secret`, must not be `None`"
            )  # noqa: E501

        self._api_key_secret = api_key_secret

    @property
    def user_id(self):
        """Gets the user_id of this ApiKeyDto.  # noqa: E501


        :return: The user_id of this ApiKeyDto.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ApiKeyDto.


        :param user_id: The user_id of this ApiKeyDto.  # noqa: E501
        :type: float
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def api_key_id(self):
        """Gets the api_key_id of this ApiKeyDto.  # noqa: E501


        :return: The api_key_id of this ApiKeyDto.  # noqa: E501
        :rtype: float
        """
        return self._api_key_id

    @api_key_id.setter
    def api_key_id(self, api_key_id):
        """Sets the api_key_id of this ApiKeyDto.


        :param api_key_id: The api_key_id of this ApiKeyDto.  # noqa: E501
        :type: float
        """
        if api_key_id is None:
            raise ValueError(
                "Invalid value for `api_key_id`, must not be `None`"
            )  # noqa: E501

        self._api_key_id = api_key_id

    @property
    def api_key_created_at(self):
        """Gets the api_key_created_at of this ApiKeyDto.  # noqa: E501


        :return: The api_key_created_at of this ApiKeyDto.  # noqa: E501
        :rtype: AnyOfApiKeyDtoApiKeyCreatedAt
        """
        return self._api_key_created_at

    @api_key_created_at.setter
    def api_key_created_at(self, api_key_created_at):
        """Sets the api_key_created_at of this ApiKeyDto.


        :param api_key_created_at: The api_key_created_at of this ApiKeyDto.  # noqa: E501
        :type: AnyOfApiKeyDtoApiKeyCreatedAt
        """
        if api_key_created_at is None:
            raise ValueError(
                "Invalid value for `api_key_created_at`, must not be `None`"
            )  # noqa: E501

        self._api_key_created_at = api_key_created_at

    @property
    def api_key_updated_at(self):
        """Gets the api_key_updated_at of this ApiKeyDto.  # noqa: E501


        :return: The api_key_updated_at of this ApiKeyDto.  # noqa: E501
        :rtype: AnyOfApiKeyDtoApiKeyUpdatedAt
        """
        return self._api_key_updated_at

    @api_key_updated_at.setter
    def api_key_updated_at(self, api_key_updated_at):
        """Sets the api_key_updated_at of this ApiKeyDto.


        :param api_key_updated_at: The api_key_updated_at of this ApiKeyDto.  # noqa: E501
        :type: AnyOfApiKeyDtoApiKeyUpdatedAt
        """
        if api_key_updated_at is None:
            raise ValueError(
                "Invalid value for `api_key_updated_at`, must not be `None`"
            )  # noqa: E501

        self._api_key_updated_at = api_key_updated_at

    @property
    def api_key_status(self):
        """Gets the api_key_status of this ApiKeyDto.  # noqa: E501


        :return: The api_key_status of this ApiKeyDto.  # noqa: E501
        :rtype: bool
        """
        return self._api_key_status

    @api_key_status.setter
    def api_key_status(self, api_key_status):
        """Sets the api_key_status of this ApiKeyDto.


        :param api_key_status: The api_key_status of this ApiKeyDto.  # noqa: E501
        :type: bool
        """
        if api_key_status is None:
            raise ValueError(
                "Invalid value for `api_key_status`, must not be `None`"
            )  # noqa: E501

        self._api_key_status = api_key_status

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
        if issubclass(ApiKeyDto, dict):
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
        if not isinstance(other, ApiKeyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
