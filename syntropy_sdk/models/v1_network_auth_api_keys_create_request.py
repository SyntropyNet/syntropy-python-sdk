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


class V1NetworkAuthApiKeysCreateRequest(object):
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
        "api_key_name": "str",
        "api_key_description": "str",
        "api_key_valid_until": "datetime",
        "api_key_allowed_tag_names": "list[str]",
    }

    attribute_map = {
        "api_key_name": "api_key_name",
        "api_key_description": "api_key_description",
        "api_key_valid_until": "api_key_valid_until",
        "api_key_allowed_tag_names": "api_key_allowed_tag_names",
    }

    def __init__(
        self,
        api_key_name=None,
        api_key_description=None,
        api_key_valid_until=None,
        api_key_allowed_tag_names=None,
    ):  # noqa: E501
        """V1NetworkAuthApiKeysCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._api_key_name = None
        self._api_key_description = None
        self._api_key_valid_until = None
        self._api_key_allowed_tag_names = None
        self.discriminator = None
        self.api_key_name = api_key_name
        if api_key_description is not None:
            self.api_key_description = api_key_description
        if api_key_valid_until is not None:
            self.api_key_valid_until = api_key_valid_until
        if api_key_allowed_tag_names is not None:
            self.api_key_allowed_tag_names = api_key_allowed_tag_names

    @property
    def api_key_name(self):
        """Gets the api_key_name of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501


        :return: The api_key_name of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        """Sets the api_key_name of this V1NetworkAuthApiKeysCreateRequest.


        :param api_key_name: The api_key_name of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501
        :type: str
        """
        if api_key_name is None:
            raise ValueError(
                "Invalid value for `api_key_name`, must not be `None`"
            )  # noqa: E501

        self._api_key_name = api_key_name

    @property
    def api_key_description(self):
        """Gets the api_key_description of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501


        :return: The api_key_description of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_key_description

    @api_key_description.setter
    def api_key_description(self, api_key_description):
        """Sets the api_key_description of this V1NetworkAuthApiKeysCreateRequest.


        :param api_key_description: The api_key_description of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501
        :type: str
        """

        self._api_key_description = api_key_description

    @property
    def api_key_valid_until(self):
        """Gets the api_key_valid_until of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501


        :return: The api_key_valid_until of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._api_key_valid_until

    @api_key_valid_until.setter
    def api_key_valid_until(self, api_key_valid_until):
        """Sets the api_key_valid_until of this V1NetworkAuthApiKeysCreateRequest.


        :param api_key_valid_until: The api_key_valid_until of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501
        :type: datetime
        """

        self._api_key_valid_until = api_key_valid_until

    @property
    def api_key_allowed_tag_names(self):
        """Gets the api_key_allowed_tag_names of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501


        :return: The api_key_allowed_tag_names of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._api_key_allowed_tag_names

    @api_key_allowed_tag_names.setter
    def api_key_allowed_tag_names(self, api_key_allowed_tag_names):
        """Sets the api_key_allowed_tag_names of this V1NetworkAuthApiKeysCreateRequest.


        :param api_key_allowed_tag_names: The api_key_allowed_tag_names of this V1NetworkAuthApiKeysCreateRequest.  # noqa: E501
        :type: list[str]
        """

        self._api_key_allowed_tag_names = api_key_allowed_tag_names

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
        if issubclass(V1NetworkAuthApiKeysCreateRequest, dict):
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
        if not isinstance(other, V1NetworkAuthApiKeysCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other