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


class V1NetworkAgentsCreateRequest(object):
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
        "agent_tags": "list[str]",
        "api_key": "str",
        "agent_name": "str",
        "agent_provider_id": "IdNumber",
    }

    attribute_map = {
        "agent_tags": "agent_tags",
        "api_key": "api_key",
        "agent_name": "agent_name",
        "agent_provider_id": "agent_provider_id",
    }

    def __init__(
        self, agent_tags=None, api_key=None, agent_name=None, agent_provider_id=None
    ):  # noqa: E501
        """V1NetworkAgentsCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._agent_tags = None
        self._api_key = None
        self._agent_name = None
        self._agent_provider_id = None
        self.discriminator = None
        if agent_tags is not None:
            self.agent_tags = agent_tags
        self.api_key = api_key
        self.agent_name = agent_name
        if agent_provider_id is not None:
            self.agent_provider_id = agent_provider_id

    @property
    def agent_tags(self):
        """Gets the agent_tags of this V1NetworkAgentsCreateRequest.  # noqa: E501


        :return: The agent_tags of this V1NetworkAgentsCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, agent_tags):
        """Sets the agent_tags of this V1NetworkAgentsCreateRequest.


        :param agent_tags: The agent_tags of this V1NetworkAgentsCreateRequest.  # noqa: E501
        :type: list[str]
        """

        self._agent_tags = agent_tags

    @property
    def api_key(self):
        """Gets the api_key of this V1NetworkAgentsCreateRequest.  # noqa: E501


        :return: The api_key of this V1NetworkAgentsCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this V1NetworkAgentsCreateRequest.


        :param api_key: The api_key of this V1NetworkAgentsCreateRequest.  # noqa: E501
        :type: str
        """
        if api_key is None:
            raise ValueError(
                "Invalid value for `api_key`, must not be `None`"
            )  # noqa: E501

        self._api_key = api_key

    @property
    def agent_name(self):
        """Gets the agent_name of this V1NetworkAgentsCreateRequest.  # noqa: E501


        :return: The agent_name of this V1NetworkAgentsCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this V1NetworkAgentsCreateRequest.


        :param agent_name: The agent_name of this V1NetworkAgentsCreateRequest.  # noqa: E501
        :type: str
        """
        if agent_name is None:
            raise ValueError(
                "Invalid value for `agent_name`, must not be `None`"
            )  # noqa: E501

        self._agent_name = agent_name

    @property
    def agent_provider_id(self):
        """Gets the agent_provider_id of this V1NetworkAgentsCreateRequest.  # noqa: E501


        :return: The agent_provider_id of this V1NetworkAgentsCreateRequest.  # noqa: E501
        :rtype: IdNumber
        """
        return self._agent_provider_id

    @agent_provider_id.setter
    def agent_provider_id(self, agent_provider_id):
        """Sets the agent_provider_id of this V1NetworkAgentsCreateRequest.


        :param agent_provider_id: The agent_provider_id of this V1NetworkAgentsCreateRequest.  # noqa: E501
        :type: IdNumber
        """

        self._agent_provider_id = agent_provider_id

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
        if issubclass(V1NetworkAgentsCreateRequest, dict):
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
        if not isinstance(other, V1NetworkAgentsCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
