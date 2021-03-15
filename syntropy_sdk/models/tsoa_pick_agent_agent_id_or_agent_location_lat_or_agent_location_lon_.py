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


class TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_(object):
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
        "agent_id": "float",
        "agent_location_lat": "float",
        "agent_location_lon": "float",
    }

    attribute_map = {
        "agent_id": "agent_id",
        "agent_location_lat": "agent_location_lat",
        "agent_location_lon": "agent_location_lon",
    }

    def __init__(
        self, agent_id=None, agent_location_lat=None, agent_location_lon=None
    ):  # noqa: E501
        """TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_ - a model defined in Swagger"""  # noqa: E501
        self._agent_id = None
        self._agent_location_lat = None
        self._agent_location_lon = None
        self.discriminator = None
        self.agent_id = agent_id
        if agent_location_lat is not None:
            self.agent_location_lat = agent_location_lat
        if agent_location_lon is not None:
            self.agent_location_lon = agent_location_lon

    @property
    def agent_id(self):
        """Gets the agent_id of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501


        :return: The agent_id of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.


        :param agent_id: The agent_id of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def agent_location_lat(self):
        """Gets the agent_location_lat of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501


        :return: The agent_location_lat of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501
        :rtype: float
        """
        return self._agent_location_lat

    @agent_location_lat.setter
    def agent_location_lat(self, agent_location_lat):
        """Sets the agent_location_lat of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.


        :param agent_location_lat: The agent_location_lat of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501
        :type: float
        """

        self._agent_location_lat = agent_location_lat

    @property
    def agent_location_lon(self):
        """Gets the agent_location_lon of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501


        :return: The agent_location_lon of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501
        :rtype: float
        """
        return self._agent_location_lon

    @agent_location_lon.setter
    def agent_location_lon(self, agent_location_lon):
        """Sets the agent_location_lon of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.


        :param agent_location_lon: The agent_location_lon of this TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.  # noqa: E501
        :type: float
        """

        self._agent_location_lon = agent_location_lon

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
        if issubclass(TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_, dict):
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
        if not isinstance(
            other, TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
