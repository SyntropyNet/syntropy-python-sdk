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


class TsoaPartialAgentConnectionObject_(object):
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
        "agent_1_id": "float",
        "agent_interface_1_id": "float",
        "agent_2_id": "float",
        "agent_interface_2_id": "float",
        "user_id": "float",
        "agent_sdn_policy_id": "float",
        "agent_connection_link_tag": "LinkTag",
        "agent_connection_status": "AgentConnectionStatus",
        "agent_connection_last_handshake": "datetime",
        "agent_connection_tx_bytes_total": "float",
        "agent_connection_rx_bytes_total": "float",
        "agent_connection_latency_ms": "float",
        "agent_connection_packet_loss": "float",
    }

    attribute_map = {
        "agent_1_id": "agent_1_id",
        "agent_interface_1_id": "agent_interface_1_id",
        "agent_2_id": "agent_2_id",
        "agent_interface_2_id": "agent_interface_2_id",
        "user_id": "user_id",
        "agent_sdn_policy_id": "agent_sdn_policy_id",
        "agent_connection_link_tag": "agent_connection_link_tag",
        "agent_connection_status": "agent_connection_status",
        "agent_connection_last_handshake": "agent_connection_last_handshake",
        "agent_connection_tx_bytes_total": "agent_connection_tx_bytes_total",
        "agent_connection_rx_bytes_total": "agent_connection_rx_bytes_total",
        "agent_connection_latency_ms": "agent_connection_latency_ms",
        "agent_connection_packet_loss": "agent_connection_packet_loss",
    }

    def __init__(
        self,
        agent_1_id=None,
        agent_interface_1_id=None,
        agent_2_id=None,
        agent_interface_2_id=None,
        user_id=None,
        agent_sdn_policy_id=None,
        agent_connection_link_tag=None,
        agent_connection_status=None,
        agent_connection_last_handshake=None,
        agent_connection_tx_bytes_total=None,
        agent_connection_rx_bytes_total=None,
        agent_connection_latency_ms=None,
        agent_connection_packet_loss=None,
    ):  # noqa: E501
        """TsoaPartialAgentConnectionObject_ - a model defined in Swagger"""  # noqa: E501
        self._agent_1_id = None
        self._agent_interface_1_id = None
        self._agent_2_id = None
        self._agent_interface_2_id = None
        self._user_id = None
        self._agent_sdn_policy_id = None
        self._agent_connection_link_tag = None
        self._agent_connection_status = None
        self._agent_connection_last_handshake = None
        self._agent_connection_tx_bytes_total = None
        self._agent_connection_rx_bytes_total = None
        self._agent_connection_latency_ms = None
        self._agent_connection_packet_loss = None
        self.discriminator = None
        if agent_1_id is not None:
            self.agent_1_id = agent_1_id
        if agent_interface_1_id is not None:
            self.agent_interface_1_id = agent_interface_1_id
        if agent_2_id is not None:
            self.agent_2_id = agent_2_id
        if agent_interface_2_id is not None:
            self.agent_interface_2_id = agent_interface_2_id
        if user_id is not None:
            self.user_id = user_id
        if agent_sdn_policy_id is not None:
            self.agent_sdn_policy_id = agent_sdn_policy_id
        if agent_connection_link_tag is not None:
            self.agent_connection_link_tag = agent_connection_link_tag
        if agent_connection_status is not None:
            self.agent_connection_status = agent_connection_status
        if agent_connection_last_handshake is not None:
            self.agent_connection_last_handshake = agent_connection_last_handshake
        if agent_connection_tx_bytes_total is not None:
            self.agent_connection_tx_bytes_total = agent_connection_tx_bytes_total
        if agent_connection_rx_bytes_total is not None:
            self.agent_connection_rx_bytes_total = agent_connection_rx_bytes_total
        if agent_connection_latency_ms is not None:
            self.agent_connection_latency_ms = agent_connection_latency_ms
        if agent_connection_packet_loss is not None:
            self.agent_connection_packet_loss = agent_connection_packet_loss

    @property
    def agent_1_id(self):
        """Gets the agent_1_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_1_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_1_id

    @agent_1_id.setter
    def agent_1_id(self, agent_1_id):
        """Sets the agent_1_id of this TsoaPartialAgentConnectionObject_.


        :param agent_1_id: The agent_1_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_1_id = agent_1_id

    @property
    def agent_interface_1_id(self):
        """Gets the agent_interface_1_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_interface_1_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_interface_1_id

    @agent_interface_1_id.setter
    def agent_interface_1_id(self, agent_interface_1_id):
        """Sets the agent_interface_1_id of this TsoaPartialAgentConnectionObject_.


        :param agent_interface_1_id: The agent_interface_1_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_interface_1_id = agent_interface_1_id

    @property
    def agent_2_id(self):
        """Gets the agent_2_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_2_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_2_id

    @agent_2_id.setter
    def agent_2_id(self, agent_2_id):
        """Sets the agent_2_id of this TsoaPartialAgentConnectionObject_.


        :param agent_2_id: The agent_2_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_2_id = agent_2_id

    @property
    def agent_interface_2_id(self):
        """Gets the agent_interface_2_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_interface_2_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_interface_2_id

    @agent_interface_2_id.setter
    def agent_interface_2_id(self, agent_interface_2_id):
        """Sets the agent_interface_2_id of this TsoaPartialAgentConnectionObject_.


        :param agent_interface_2_id: The agent_interface_2_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_interface_2_id = agent_interface_2_id

    @property
    def user_id(self):
        """Gets the user_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The user_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TsoaPartialAgentConnectionObject_.


        :param user_id: The user_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def agent_sdn_policy_id(self):
        """Gets the agent_sdn_policy_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_sdn_policy_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_sdn_policy_id

    @agent_sdn_policy_id.setter
    def agent_sdn_policy_id(self, agent_sdn_policy_id):
        """Sets the agent_sdn_policy_id of this TsoaPartialAgentConnectionObject_.


        :param agent_sdn_policy_id: The agent_sdn_policy_id of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_sdn_policy_id = agent_sdn_policy_id

    @property
    def agent_connection_link_tag(self):
        """Gets the agent_connection_link_tag of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_connection_link_tag of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: LinkTag
        """
        return self._agent_connection_link_tag

    @agent_connection_link_tag.setter
    def agent_connection_link_tag(self, agent_connection_link_tag):
        """Sets the agent_connection_link_tag of this TsoaPartialAgentConnectionObject_.


        :param agent_connection_link_tag: The agent_connection_link_tag of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: LinkTag
        """

        self._agent_connection_link_tag = agent_connection_link_tag

    @property
    def agent_connection_status(self):
        """Gets the agent_connection_status of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_connection_status of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: AgentConnectionStatus
        """
        return self._agent_connection_status

    @agent_connection_status.setter
    def agent_connection_status(self, agent_connection_status):
        """Sets the agent_connection_status of this TsoaPartialAgentConnectionObject_.


        :param agent_connection_status: The agent_connection_status of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: AgentConnectionStatus
        """

        self._agent_connection_status = agent_connection_status

    @property
    def agent_connection_last_handshake(self):
        """Gets the agent_connection_last_handshake of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_connection_last_handshake of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_connection_last_handshake

    @agent_connection_last_handshake.setter
    def agent_connection_last_handshake(self, agent_connection_last_handshake):
        """Sets the agent_connection_last_handshake of this TsoaPartialAgentConnectionObject_.


        :param agent_connection_last_handshake: The agent_connection_last_handshake of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: datetime
        """

        self._agent_connection_last_handshake = agent_connection_last_handshake

    @property
    def agent_connection_tx_bytes_total(self):
        """Gets the agent_connection_tx_bytes_total of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_connection_tx_bytes_total of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_connection_tx_bytes_total

    @agent_connection_tx_bytes_total.setter
    def agent_connection_tx_bytes_total(self, agent_connection_tx_bytes_total):
        """Sets the agent_connection_tx_bytes_total of this TsoaPartialAgentConnectionObject_.


        :param agent_connection_tx_bytes_total: The agent_connection_tx_bytes_total of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_connection_tx_bytes_total = agent_connection_tx_bytes_total

    @property
    def agent_connection_rx_bytes_total(self):
        """Gets the agent_connection_rx_bytes_total of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_connection_rx_bytes_total of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_connection_rx_bytes_total

    @agent_connection_rx_bytes_total.setter
    def agent_connection_rx_bytes_total(self, agent_connection_rx_bytes_total):
        """Sets the agent_connection_rx_bytes_total of this TsoaPartialAgentConnectionObject_.


        :param agent_connection_rx_bytes_total: The agent_connection_rx_bytes_total of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_connection_rx_bytes_total = agent_connection_rx_bytes_total

    @property
    def agent_connection_latency_ms(self):
        """Gets the agent_connection_latency_ms of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_connection_latency_ms of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_connection_latency_ms

    @agent_connection_latency_ms.setter
    def agent_connection_latency_ms(self, agent_connection_latency_ms):
        """Sets the agent_connection_latency_ms of this TsoaPartialAgentConnectionObject_.


        :param agent_connection_latency_ms: The agent_connection_latency_ms of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_connection_latency_ms = agent_connection_latency_ms

    @property
    def agent_connection_packet_loss(self):
        """Gets the agent_connection_packet_loss of this TsoaPartialAgentConnectionObject_.  # noqa: E501


        :return: The agent_connection_packet_loss of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :rtype: float
        """
        return self._agent_connection_packet_loss

    @agent_connection_packet_loss.setter
    def agent_connection_packet_loss(self, agent_connection_packet_loss):
        """Sets the agent_connection_packet_loss of this TsoaPartialAgentConnectionObject_.


        :param agent_connection_packet_loss: The agent_connection_packet_loss of this TsoaPartialAgentConnectionObject_.  # noqa: E501
        :type: float
        """

        self._agent_connection_packet_loss = agent_connection_packet_loss

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
        if issubclass(TsoaPartialAgentConnectionObject_, dict):
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
        if not isinstance(other, TsoaPartialAgentConnectionObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
