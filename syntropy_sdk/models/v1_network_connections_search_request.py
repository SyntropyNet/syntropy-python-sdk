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


class V1NetworkConnectionsSearchRequest(object):
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
        "filter": "V1ConnectionFilter",
        "order": "V1ConnectionOrder",
        "skip": "V1SkipNumber",
        "take": "V1TakeNumber",
    }

    attribute_map = {
        "filter": "filter",
        "order": "order",
        "skip": "skip",
        "take": "take",
    }

    def __init__(self, filter=None, order=None, skip=None, take=None):  # noqa: E501
        """V1NetworkConnectionsSearchRequest - a model defined in Swagger"""  # noqa: E501
        self._filter = None
        self._order = None
        self._skip = None
        self._take = None
        self.discriminator = None
        if filter is not None:
            self.filter = filter
        if order is not None:
            self.order = order
        if skip is not None:
            self.skip = skip
        if take is not None:
            self.take = take

    @property
    def filter(self):
        """Gets the filter of this V1NetworkConnectionsSearchRequest.  # noqa: E501


        :return: The filter of this V1NetworkConnectionsSearchRequest.  # noqa: E501
        :rtype: V1ConnectionFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this V1NetworkConnectionsSearchRequest.


        :param filter: The filter of this V1NetworkConnectionsSearchRequest.  # noqa: E501
        :type: V1ConnectionFilter
        """

        self._filter = filter

    @property
    def order(self):
        """Gets the order of this V1NetworkConnectionsSearchRequest.  # noqa: E501


        :return: The order of this V1NetworkConnectionsSearchRequest.  # noqa: E501
        :rtype: V1ConnectionOrder
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this V1NetworkConnectionsSearchRequest.


        :param order: The order of this V1NetworkConnectionsSearchRequest.  # noqa: E501
        :type: V1ConnectionOrder
        """

        self._order = order

    @property
    def skip(self):
        """Gets the skip of this V1NetworkConnectionsSearchRequest.  # noqa: E501


        :return: The skip of this V1NetworkConnectionsSearchRequest.  # noqa: E501
        :rtype: V1SkipNumber
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this V1NetworkConnectionsSearchRequest.


        :param skip: The skip of this V1NetworkConnectionsSearchRequest.  # noqa: E501
        :type: V1SkipNumber
        """

        self._skip = skip

    @property
    def take(self):
        """Gets the take of this V1NetworkConnectionsSearchRequest.  # noqa: E501


        :return: The take of this V1NetworkConnectionsSearchRequest.  # noqa: E501
        :rtype: V1TakeNumber
        """
        return self._take

    @take.setter
    def take(self, take):
        """Sets the take of this V1NetworkConnectionsSearchRequest.


        :param take: The take of this V1NetworkConnectionsSearchRequest.  # noqa: E501
        :type: V1TakeNumber
        """

        self._take = take

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
        if issubclass(V1NetworkConnectionsSearchRequest, dict):
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
        if not isinstance(other, V1NetworkConnectionsSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other