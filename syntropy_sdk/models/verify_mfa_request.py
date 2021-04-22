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


class VerifyMFARequest(object):
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
        "code": "AnyOfVerifyMFARequestCode",
        "code_type": "MfaCodeType",
        "secret_key": "str",
    }

    attribute_map = {
        "user_id": "user_id",
        "code": "code",
        "code_type": "codeType",
        "secret_key": "secretKey",
    }

    def __init__(
        self, user_id=None, code=None, code_type=None, secret_key=None
    ):  # noqa: E501
        """VerifyMFARequest - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._code = None
        self._code_type = None
        self._secret_key = None
        self.discriminator = None
        self.user_id = user_id
        self.code = code
        self.code_type = code_type
        self.secret_key = secret_key

    @property
    def user_id(self):
        """Gets the user_id of this VerifyMFARequest.  # noqa: E501


        :return: The user_id of this VerifyMFARequest.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this VerifyMFARequest.


        :param user_id: The user_id of this VerifyMFARequest.  # noqa: E501
        :type: float
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def code(self):
        """Gets the code of this VerifyMFARequest.  # noqa: E501


        :return: The code of this VerifyMFARequest.  # noqa: E501
        :rtype: AnyOfVerifyMFARequestCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VerifyMFARequest.


        :param code: The code of this VerifyMFARequest.  # noqa: E501
        :type: AnyOfVerifyMFARequestCode
        """
        if code is None:
            raise ValueError(
                "Invalid value for `code`, must not be `None`"
            )  # noqa: E501

        self._code = code

    @property
    def code_type(self):
        """Gets the code_type of this VerifyMFARequest.  # noqa: E501


        :return: The code_type of this VerifyMFARequest.  # noqa: E501
        :rtype: MfaCodeType
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this VerifyMFARequest.


        :param code_type: The code_type of this VerifyMFARequest.  # noqa: E501
        :type: MfaCodeType
        """
        if code_type is None:
            raise ValueError(
                "Invalid value for `code_type`, must not be `None`"
            )  # noqa: E501

        self._code_type = code_type

    @property
    def secret_key(self):
        """Gets the secret_key of this VerifyMFARequest.  # noqa: E501


        :return: The secret_key of this VerifyMFARequest.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this VerifyMFARequest.


        :param secret_key: The secret_key of this VerifyMFARequest.  # noqa: E501
        :type: str
        """
        if secret_key is None:
            raise ValueError(
                "Invalid value for `secret_key`, must not be `None`"
            )  # noqa: E501

        self._secret_key = secret_key

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
        if issubclass(VerifyMFARequest, dict):
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
        if not isinstance(other, VerifyMFARequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
