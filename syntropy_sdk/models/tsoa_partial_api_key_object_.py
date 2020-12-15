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


class TsoaPartialApiKeyObject_(object):
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
        "organization_id": "float",
        "user_id": "float",
        "api_key_secret": "str",
        "api_key_name": "str",
        "api_key_is_suspended": "bool",
        "api_key_valid_until": "str",
    }

    attribute_map = {
        "organization_id": "organization_id",
        "user_id": "user_id",
        "api_key_secret": "api_key_secret",
        "api_key_name": "api_key_name",
        "api_key_is_suspended": "api_key_is_suspended",
        "api_key_valid_until": "api_key_valid_until",
    }

    def __init__(
        self,
        organization_id=None,
        user_id=None,
        api_key_secret=None,
        api_key_name=None,
        api_key_is_suspended=None,
        api_key_valid_until=None,
    ):  # noqa: E501
        """TsoaPartialApiKeyObject_ - a model defined in Swagger"""  # noqa: E501
        self._organization_id = None
        self._user_id = None
        self._api_key_secret = None
        self._api_key_name = None
        self._api_key_is_suspended = None
        self._api_key_valid_until = None
        self.discriminator = None
        if organization_id is not None:
            self.organization_id = organization_id
        if user_id is not None:
            self.user_id = user_id
        if api_key_secret is not None:
            self.api_key_secret = api_key_secret
        if api_key_name is not None:
            self.api_key_name = api_key_name
        if api_key_is_suspended is not None:
            self.api_key_is_suspended = api_key_is_suspended
        if api_key_valid_until is not None:
            self.api_key_valid_until = api_key_valid_until

    @property
    def organization_id(self):
        """Gets the organization_id of this TsoaPartialApiKeyObject_.  # noqa: E501


        :return: The organization_id of this TsoaPartialApiKeyObject_.  # noqa: E501
        :rtype: float
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this TsoaPartialApiKeyObject_.


        :param organization_id: The organization_id of this TsoaPartialApiKeyObject_.  # noqa: E501
        :type: float
        """

        self._organization_id = organization_id

    @property
    def user_id(self):
        """Gets the user_id of this TsoaPartialApiKeyObject_.  # noqa: E501


        :return: The user_id of this TsoaPartialApiKeyObject_.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TsoaPartialApiKeyObject_.


        :param user_id: The user_id of this TsoaPartialApiKeyObject_.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def api_key_secret(self):
        """Gets the api_key_secret of this TsoaPartialApiKeyObject_.  # noqa: E501


        :return: The api_key_secret of this TsoaPartialApiKeyObject_.  # noqa: E501
        :rtype: str
        """
        return self._api_key_secret

    @api_key_secret.setter
    def api_key_secret(self, api_key_secret):
        """Sets the api_key_secret of this TsoaPartialApiKeyObject_.


        :param api_key_secret: The api_key_secret of this TsoaPartialApiKeyObject_.  # noqa: E501
        :type: str
        """

        self._api_key_secret = api_key_secret

    @property
    def api_key_name(self):
        """Gets the api_key_name of this TsoaPartialApiKeyObject_.  # noqa: E501


        :return: The api_key_name of this TsoaPartialApiKeyObject_.  # noqa: E501
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        """Sets the api_key_name of this TsoaPartialApiKeyObject_.


        :param api_key_name: The api_key_name of this TsoaPartialApiKeyObject_.  # noqa: E501
        :type: str
        """

        self._api_key_name = api_key_name

    @property
    def api_key_is_suspended(self):
        """Gets the api_key_is_suspended of this TsoaPartialApiKeyObject_.  # noqa: E501


        :return: The api_key_is_suspended of this TsoaPartialApiKeyObject_.  # noqa: E501
        :rtype: bool
        """
        return self._api_key_is_suspended

    @api_key_is_suspended.setter
    def api_key_is_suspended(self, api_key_is_suspended):
        """Sets the api_key_is_suspended of this TsoaPartialApiKeyObject_.


        :param api_key_is_suspended: The api_key_is_suspended of this TsoaPartialApiKeyObject_.  # noqa: E501
        :type: bool
        """

        self._api_key_is_suspended = api_key_is_suspended

    @property
    def api_key_valid_until(self):
        """Gets the api_key_valid_until of this TsoaPartialApiKeyObject_.  # noqa: E501


        :return: The api_key_valid_until of this TsoaPartialApiKeyObject_.  # noqa: E501
        :rtype: str
        """
        return self._api_key_valid_until

    @api_key_valid_until.setter
    def api_key_valid_until(self, api_key_valid_until):
        """Sets the api_key_valid_until of this TsoaPartialApiKeyObject_.


        :param api_key_valid_until: The api_key_valid_until of this TsoaPartialApiKeyObject_.  # noqa: E501
        :type: str
        """

        self._api_key_valid_until = api_key_valid_until

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
        if issubclass(TsoaPartialApiKeyObject_, dict):
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
        if not isinstance(other, TsoaPartialApiKeyObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
