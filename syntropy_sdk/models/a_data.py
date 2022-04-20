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

class AData(object):
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
        'columns': 'list[str]',
        'dataset': 'list[list[object]]'
    }

    attribute_map = {
        'columns': 'columns',
        'dataset': 'dataset'
    }

    def __init__(self, columns=None, dataset=None):  # noqa: E501
        """AData - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self._dataset = None
        self.discriminator = None
        self.columns = columns
        self.dataset = dataset

    @property
    def columns(self):
        """Gets the columns of this AData.  # noqa: E501


        :return: The columns of this AData.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this AData.


        :param columns: The columns of this AData.  # noqa: E501
        :type: list[str]
        """
        if columns is None:
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501

        self._columns = columns

    @property
    def dataset(self):
        """Gets the dataset of this AData.  # noqa: E501


        :return: The dataset of this AData.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this AData.


        :param dataset: The dataset of this AData.  # noqa: E501
        :type: list[list[object]]
        """
        if dataset is None:
            raise ValueError("Invalid value for `dataset`, must not be `None`")  # noqa: E501

        self._dataset = dataset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AData, dict):
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
        if not isinstance(other, AData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
