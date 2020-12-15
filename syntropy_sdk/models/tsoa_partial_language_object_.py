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


class TsoaPartialLanguageObject_(object):
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
        "lang_code": "str",
        "lang_title": "str",
        "lang_native_title": "str",
        "lang_weight": "float",
        "lang_visibility": "VisibilityType",
    }

    attribute_map = {
        "lang_code": "lang_code",
        "lang_title": "lang_title",
        "lang_native_title": "lang_native_title",
        "lang_weight": "lang_weight",
        "lang_visibility": "lang_visibility",
    }

    def __init__(
        self,
        lang_code=None,
        lang_title=None,
        lang_native_title=None,
        lang_weight=None,
        lang_visibility=None,
    ):  # noqa: E501
        """TsoaPartialLanguageObject_ - a model defined in Swagger"""  # noqa: E501
        self._lang_code = None
        self._lang_title = None
        self._lang_native_title = None
        self._lang_weight = None
        self._lang_visibility = None
        self.discriminator = None
        if lang_code is not None:
            self.lang_code = lang_code
        if lang_title is not None:
            self.lang_title = lang_title
        if lang_native_title is not None:
            self.lang_native_title = lang_native_title
        if lang_weight is not None:
            self.lang_weight = lang_weight
        if lang_visibility is not None:
            self.lang_visibility = lang_visibility

    @property
    def lang_code(self):
        """Gets the lang_code of this TsoaPartialLanguageObject_.  # noqa: E501


        :return: The lang_code of this TsoaPartialLanguageObject_.  # noqa: E501
        :rtype: str
        """
        return self._lang_code

    @lang_code.setter
    def lang_code(self, lang_code):
        """Sets the lang_code of this TsoaPartialLanguageObject_.


        :param lang_code: The lang_code of this TsoaPartialLanguageObject_.  # noqa: E501
        :type: str
        """

        self._lang_code = lang_code

    @property
    def lang_title(self):
        """Gets the lang_title of this TsoaPartialLanguageObject_.  # noqa: E501


        :return: The lang_title of this TsoaPartialLanguageObject_.  # noqa: E501
        :rtype: str
        """
        return self._lang_title

    @lang_title.setter
    def lang_title(self, lang_title):
        """Sets the lang_title of this TsoaPartialLanguageObject_.


        :param lang_title: The lang_title of this TsoaPartialLanguageObject_.  # noqa: E501
        :type: str
        """

        self._lang_title = lang_title

    @property
    def lang_native_title(self):
        """Gets the lang_native_title of this TsoaPartialLanguageObject_.  # noqa: E501


        :return: The lang_native_title of this TsoaPartialLanguageObject_.  # noqa: E501
        :rtype: str
        """
        return self._lang_native_title

    @lang_native_title.setter
    def lang_native_title(self, lang_native_title):
        """Sets the lang_native_title of this TsoaPartialLanguageObject_.


        :param lang_native_title: The lang_native_title of this TsoaPartialLanguageObject_.  # noqa: E501
        :type: str
        """

        self._lang_native_title = lang_native_title

    @property
    def lang_weight(self):
        """Gets the lang_weight of this TsoaPartialLanguageObject_.  # noqa: E501


        :return: The lang_weight of this TsoaPartialLanguageObject_.  # noqa: E501
        :rtype: float
        """
        return self._lang_weight

    @lang_weight.setter
    def lang_weight(self, lang_weight):
        """Sets the lang_weight of this TsoaPartialLanguageObject_.


        :param lang_weight: The lang_weight of this TsoaPartialLanguageObject_.  # noqa: E501
        :type: float
        """

        self._lang_weight = lang_weight

    @property
    def lang_visibility(self):
        """Gets the lang_visibility of this TsoaPartialLanguageObject_.  # noqa: E501


        :return: The lang_visibility of this TsoaPartialLanguageObject_.  # noqa: E501
        :rtype: VisibilityType
        """
        return self._lang_visibility

    @lang_visibility.setter
    def lang_visibility(self, lang_visibility):
        """Sets the lang_visibility of this TsoaPartialLanguageObject_.


        :param lang_visibility: The lang_visibility of this TsoaPartialLanguageObject_.  # noqa: E501
        :type: VisibilityType
        """

        self._lang_visibility = lang_visibility

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
        if issubclass(TsoaPartialLanguageObject_, dict):
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
        if not isinstance(other, TsoaPartialLanguageObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
