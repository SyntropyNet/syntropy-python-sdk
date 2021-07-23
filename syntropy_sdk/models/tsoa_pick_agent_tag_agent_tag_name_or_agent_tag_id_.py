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


class TsoaPickAgentTagAgentTagNameOrAgentTagId_(object):
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
    swagger_types = {"agent_tag_name": "str", "agent_tag_id": "float"}

    attribute_map = {"agent_tag_name": "agent_tag_name", "agent_tag_id": "agent_tag_id"}

    def __init__(self, agent_tag_name=None, agent_tag_id=None):  # noqa: E501
        """TsoaPickAgentTagAgentTagNameOrAgentTagId_ - a model defined in Swagger"""  # noqa: E501
        self._agent_tag_name = None
        self._agent_tag_id = None
        self.discriminator = None
        self.agent_tag_name = agent_tag_name
        self.agent_tag_id = agent_tag_id

    @property
    def agent_tag_name(self):
        """Gets the agent_tag_name of this TsoaPickAgentTagAgentTagNameOrAgentTagId_.  # noqa: E501


        :return: The agent_tag_name of this TsoaPickAgentTagAgentTagNameOrAgentTagId_.  # noqa: E501
        :rtype: str
        """
        return self._agent_tag_name

    @agent_tag_name.setter
    def agent_tag_name(self, agent_tag_name):
        """Sets the agent_tag_name of this TsoaPickAgentTagAgentTagNameOrAgentTagId_.


        :param agent_tag_name: The agent_tag_name of this TsoaPickAgentTagAgentTagNameOrAgentTagId_.  # noqa: E501
        :type: str
        """
        if agent_tag_name is None:
            raise ValueError(
                "Invalid value for `agent_tag_name`, must not be `None`"
            )  # noqa: E501

        self._agent_tag_name = agent_tag_name

    @property
    def agent_tag_id(self):
        """Gets the agent_tag_id of this TsoaPickAgentTagAgentTagNameOrAgentTagId_.  # noqa: E501


        :return: The agent_tag_id of this TsoaPickAgentTagAgentTagNameOrAgentTagId_.  # noqa: E501
        :rtype: float
        """
        return self._agent_tag_id

    @agent_tag_id.setter
    def agent_tag_id(self, agent_tag_id):
        """Sets the agent_tag_id of this TsoaPickAgentTagAgentTagNameOrAgentTagId_.


        :param agent_tag_id: The agent_tag_id of this TsoaPickAgentTagAgentTagNameOrAgentTagId_.  # noqa: E501
        :type: float
        """
        if agent_tag_id is None:
            raise ValueError(
                "Invalid value for `agent_tag_id`, must not be `None`"
            )  # noqa: E501

        self._agent_tag_id = agent_tag_id

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
        if issubclass(TsoaPickAgentTagAgentTagNameOrAgentTagId_, dict):
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
        if not isinstance(other, TsoaPickAgentTagAgentTagNameOrAgentTagId_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other