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


class TsoaPartialAgentProviderObject_(object):
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
    swagger_types = {"agent_provider_name": "str", "agent_provider_icon_url": "str"}

    attribute_map = {
        "agent_provider_name": "agent_provider_name",
        "agent_provider_icon_url": "agent_provider_icon_url",
    }

    def __init__(
        self, agent_provider_name=None, agent_provider_icon_url=None
    ):  # noqa: E501
        """TsoaPartialAgentProviderObject_ - a model defined in Swagger"""  # noqa: E501
        self._agent_provider_name = None
        self._agent_provider_icon_url = None
        self.discriminator = None
        if agent_provider_name is not None:
            self.agent_provider_name = agent_provider_name
        if agent_provider_icon_url is not None:
            self.agent_provider_icon_url = agent_provider_icon_url

    @property
    def agent_provider_name(self):
        """Gets the agent_provider_name of this TsoaPartialAgentProviderObject_.  # noqa: E501


        :return: The agent_provider_name of this TsoaPartialAgentProviderObject_.  # noqa: E501
        :rtype: str
        """
        return self._agent_provider_name

    @agent_provider_name.setter
    def agent_provider_name(self, agent_provider_name):
        """Sets the agent_provider_name of this TsoaPartialAgentProviderObject_.


        :param agent_provider_name: The agent_provider_name of this TsoaPartialAgentProviderObject_.  # noqa: E501
        :type: str
        """

        self._agent_provider_name = agent_provider_name

    @property
    def agent_provider_icon_url(self):
        """Gets the agent_provider_icon_url of this TsoaPartialAgentProviderObject_.  # noqa: E501


        :return: The agent_provider_icon_url of this TsoaPartialAgentProviderObject_.  # noqa: E501
        :rtype: str
        """
        return self._agent_provider_icon_url

    @agent_provider_icon_url.setter
    def agent_provider_icon_url(self, agent_provider_icon_url):
        """Sets the agent_provider_icon_url of this TsoaPartialAgentProviderObject_.


        :param agent_provider_icon_url: The agent_provider_icon_url of this TsoaPartialAgentProviderObject_.  # noqa: E501
        :type: str
        """

        self._agent_provider_icon_url = agent_provider_icon_url

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
        if issubclass(TsoaPartialAgentProviderObject_, dict):
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
        if not isinstance(other, TsoaPartialAgentProviderObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
