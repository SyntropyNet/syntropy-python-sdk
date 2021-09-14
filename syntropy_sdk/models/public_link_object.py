# coding: utf-8

"""
    syntropy-controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PublicLinkObject(object):
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
    swagger_types = {"link_title": "str", "link_url": "str", "link_type": "str"}

    attribute_map = {
        "link_title": "link_title",
        "link_url": "link_url",
        "link_type": "link_type",
    }

    def __init__(self, link_title=None, link_url=None, link_type=None):  # noqa: E501
        """PublicLinkObject - a model defined in Swagger"""  # noqa: E501
        self._link_title = None
        self._link_url = None
        self._link_type = None
        self.discriminator = None
        self.link_title = link_title
        self.link_url = link_url
        self.link_type = link_type

    @property
    def link_title(self):
        """Gets the link_title of this PublicLinkObject.  # noqa: E501


        :return: The link_title of this PublicLinkObject.  # noqa: E501
        :rtype: str
        """
        return self._link_title

    @link_title.setter
    def link_title(self, link_title):
        """Sets the link_title of this PublicLinkObject.


        :param link_title: The link_title of this PublicLinkObject.  # noqa: E501
        :type: str
        """
        if link_title is None:
            raise ValueError(
                "Invalid value for `link_title`, must not be `None`"
            )  # noqa: E501

        self._link_title = link_title

    @property
    def link_url(self):
        """Gets the link_url of this PublicLinkObject.  # noqa: E501


        :return: The link_url of this PublicLinkObject.  # noqa: E501
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url):
        """Sets the link_url of this PublicLinkObject.


        :param link_url: The link_url of this PublicLinkObject.  # noqa: E501
        :type: str
        """
        if link_url is None:
            raise ValueError(
                "Invalid value for `link_url`, must not be `None`"
            )  # noqa: E501

        self._link_url = link_url

    @property
    def link_type(self):
        """Gets the link_type of this PublicLinkObject.  # noqa: E501


        :return: The link_type of this PublicLinkObject.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this PublicLinkObject.


        :param link_type: The link_type of this PublicLinkObject.  # noqa: E501
        :type: str
        """
        if link_type is None:
            raise ValueError(
                "Invalid value for `link_type`, must not be `None`"
            )  # noqa: E501

        self._link_type = link_type

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
        if issubclass(PublicLinkObject, dict):
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
        if not isinstance(other, PublicLinkObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
