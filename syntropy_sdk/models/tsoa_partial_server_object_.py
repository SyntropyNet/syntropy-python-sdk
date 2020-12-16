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


class TsoaPartialServerObject_(object):
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
        "server_name": "str",
        "region_id": "float",
        "server_public_ipv4": "str",
        "server_public_ipv6": "str",
        "server_config_ipv4": "str",
        "server_config_ipv6": "str",
        "server_ipv6_encaps": "str",
        "server_ipv6_start": "str",
        "server_ipv6_end": "str",
        "server_ipv6_serialized": "list[str]",
        "server_gateway_ipv4": "str",
        "server_gateway_ipv6": "str",
        "provider_id": "float",
        "topology_id": "float",
        "server_sr_software": "ServerSrSoftware",
        "server_is_transit": "bool",
        "server_is_edge": "bool",
        "server_status": "Status",
        "server_status_reason": "str",
        "server_location_lat": "float",
        "server_location_lon": "float",
        "server_location_city": "str",
        "server_proxy_required": "bool",
        "server_tap_ipv4_cidr": "str",
        "server_tap_host_ipv4_cidr": "str",
        "server_tap_host_bridge": "str",
        "server_public_tap_host_ipv4": "str",
        "server_public_tap_vpp_ipv4": "str",
        "server_agent_status": "ServerAgentStatus",
        "server_agent_key": "str",
        "vpn_id": "float",
        "server_skip_configuration": "bool",
    }

    attribute_map = {
        "server_name": "server_name",
        "region_id": "region_id",
        "server_public_ipv4": "server_public_ipv4",
        "server_public_ipv6": "server_public_ipv6",
        "server_config_ipv4": "server_config_ipv4",
        "server_config_ipv6": "server_config_ipv6",
        "server_ipv6_encaps": "server_ipv6_encaps",
        "server_ipv6_start": "server_ipv6_start",
        "server_ipv6_end": "server_ipv6_end",
        "server_ipv6_serialized": "server_ipv6_serialized",
        "server_gateway_ipv4": "server_gateway_ipv4",
        "server_gateway_ipv6": "server_gateway_ipv6",
        "provider_id": "provider_id",
        "topology_id": "topology_id",
        "server_sr_software": "server_sr_software",
        "server_is_transit": "server_is_transit",
        "server_is_edge": "server_is_edge",
        "server_status": "server_status",
        "server_status_reason": "server_status_reason",
        "server_location_lat": "server_location_lat",
        "server_location_lon": "server_location_lon",
        "server_location_city": "server_location_city",
        "server_proxy_required": "server_proxy_required",
        "server_tap_ipv4_cidr": "server_tap_ipv4_cidr",
        "server_tap_host_ipv4_cidr": "server_tap_host_ipv4_cidr",
        "server_tap_host_bridge": "server_tap_host_bridge",
        "server_public_tap_host_ipv4": "server_public_tap_host_ipv4",
        "server_public_tap_vpp_ipv4": "server_public_tap_vpp_ipv4",
        "server_agent_status": "server_agent_status",
        "server_agent_key": "server_agent_key",
        "vpn_id": "vpn_id",
        "server_skip_configuration": "server_skip_configuration",
    }

    def __init__(
        self,
        server_name=None,
        region_id=None,
        server_public_ipv4=None,
        server_public_ipv6=None,
        server_config_ipv4=None,
        server_config_ipv6=None,
        server_ipv6_encaps=None,
        server_ipv6_start=None,
        server_ipv6_end=None,
        server_ipv6_serialized=None,
        server_gateway_ipv4=None,
        server_gateway_ipv6=None,
        provider_id=None,
        topology_id=None,
        server_sr_software=None,
        server_is_transit=None,
        server_is_edge=None,
        server_status=None,
        server_status_reason=None,
        server_location_lat=None,
        server_location_lon=None,
        server_location_city=None,
        server_proxy_required=None,
        server_tap_ipv4_cidr=None,
        server_tap_host_ipv4_cidr=None,
        server_tap_host_bridge=None,
        server_public_tap_host_ipv4=None,
        server_public_tap_vpp_ipv4=None,
        server_agent_status=None,
        server_agent_key=None,
        vpn_id=None,
        server_skip_configuration=None,
    ):  # noqa: E501
        """TsoaPartialServerObject_ - a model defined in Swagger"""  # noqa: E501
        self._server_name = None
        self._region_id = None
        self._server_public_ipv4 = None
        self._server_public_ipv6 = None
        self._server_config_ipv4 = None
        self._server_config_ipv6 = None
        self._server_ipv6_encaps = None
        self._server_ipv6_start = None
        self._server_ipv6_end = None
        self._server_ipv6_serialized = None
        self._server_gateway_ipv4 = None
        self._server_gateway_ipv6 = None
        self._provider_id = None
        self._topology_id = None
        self._server_sr_software = None
        self._server_is_transit = None
        self._server_is_edge = None
        self._server_status = None
        self._server_status_reason = None
        self._server_location_lat = None
        self._server_location_lon = None
        self._server_location_city = None
        self._server_proxy_required = None
        self._server_tap_ipv4_cidr = None
        self._server_tap_host_ipv4_cidr = None
        self._server_tap_host_bridge = None
        self._server_public_tap_host_ipv4 = None
        self._server_public_tap_vpp_ipv4 = None
        self._server_agent_status = None
        self._server_agent_key = None
        self._vpn_id = None
        self._server_skip_configuration = None
        self.discriminator = None
        if server_name is not None:
            self.server_name = server_name
        if region_id is not None:
            self.region_id = region_id
        if server_public_ipv4 is not None:
            self.server_public_ipv4 = server_public_ipv4
        if server_public_ipv6 is not None:
            self.server_public_ipv6 = server_public_ipv6
        if server_config_ipv4 is not None:
            self.server_config_ipv4 = server_config_ipv4
        if server_config_ipv6 is not None:
            self.server_config_ipv6 = server_config_ipv6
        if server_ipv6_encaps is not None:
            self.server_ipv6_encaps = server_ipv6_encaps
        if server_ipv6_start is not None:
            self.server_ipv6_start = server_ipv6_start
        if server_ipv6_end is not None:
            self.server_ipv6_end = server_ipv6_end
        if server_ipv6_serialized is not None:
            self.server_ipv6_serialized = server_ipv6_serialized
        if server_gateway_ipv4 is not None:
            self.server_gateway_ipv4 = server_gateway_ipv4
        if server_gateway_ipv6 is not None:
            self.server_gateway_ipv6 = server_gateway_ipv6
        if provider_id is not None:
            self.provider_id = provider_id
        if topology_id is not None:
            self.topology_id = topology_id
        if server_sr_software is not None:
            self.server_sr_software = server_sr_software
        if server_is_transit is not None:
            self.server_is_transit = server_is_transit
        if server_is_edge is not None:
            self.server_is_edge = server_is_edge
        if server_status is not None:
            self.server_status = server_status
        if server_status_reason is not None:
            self.server_status_reason = server_status_reason
        if server_location_lat is not None:
            self.server_location_lat = server_location_lat
        if server_location_lon is not None:
            self.server_location_lon = server_location_lon
        if server_location_city is not None:
            self.server_location_city = server_location_city
        if server_proxy_required is not None:
            self.server_proxy_required = server_proxy_required
        if server_tap_ipv4_cidr is not None:
            self.server_tap_ipv4_cidr = server_tap_ipv4_cidr
        if server_tap_host_ipv4_cidr is not None:
            self.server_tap_host_ipv4_cidr = server_tap_host_ipv4_cidr
        if server_tap_host_bridge is not None:
            self.server_tap_host_bridge = server_tap_host_bridge
        if server_public_tap_host_ipv4 is not None:
            self.server_public_tap_host_ipv4 = server_public_tap_host_ipv4
        if server_public_tap_vpp_ipv4 is not None:
            self.server_public_tap_vpp_ipv4 = server_public_tap_vpp_ipv4
        if server_agent_status is not None:
            self.server_agent_status = server_agent_status
        if server_agent_key is not None:
            self.server_agent_key = server_agent_key
        if vpn_id is not None:
            self.vpn_id = vpn_id
        if server_skip_configuration is not None:
            self.server_skip_configuration = server_skip_configuration

    @property
    def server_name(self):
        """Gets the server_name of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_name of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this TsoaPartialServerObject_.


        :param server_name: The server_name of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_name = server_name

    @property
    def region_id(self):
        """Gets the region_id of this TsoaPartialServerObject_.  # noqa: E501


        :return: The region_id of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: float
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this TsoaPartialServerObject_.


        :param region_id: The region_id of this TsoaPartialServerObject_.  # noqa: E501
        :type: float
        """

        self._region_id = region_id

    @property
    def server_public_ipv4(self):
        """Gets the server_public_ipv4 of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_public_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_public_ipv4

    @server_public_ipv4.setter
    def server_public_ipv4(self, server_public_ipv4):
        """Sets the server_public_ipv4 of this TsoaPartialServerObject_.


        :param server_public_ipv4: The server_public_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_public_ipv4 = server_public_ipv4

    @property
    def server_public_ipv6(self):
        """Gets the server_public_ipv6 of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_public_ipv6 of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_public_ipv6

    @server_public_ipv6.setter
    def server_public_ipv6(self, server_public_ipv6):
        """Sets the server_public_ipv6 of this TsoaPartialServerObject_.


        :param server_public_ipv6: The server_public_ipv6 of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_public_ipv6 = server_public_ipv6

    @property
    def server_config_ipv4(self):
        """Gets the server_config_ipv4 of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_config_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_config_ipv4

    @server_config_ipv4.setter
    def server_config_ipv4(self, server_config_ipv4):
        """Sets the server_config_ipv4 of this TsoaPartialServerObject_.


        :param server_config_ipv4: The server_config_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_config_ipv4 = server_config_ipv4

    @property
    def server_config_ipv6(self):
        """Gets the server_config_ipv6 of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_config_ipv6 of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_config_ipv6

    @server_config_ipv6.setter
    def server_config_ipv6(self, server_config_ipv6):
        """Sets the server_config_ipv6 of this TsoaPartialServerObject_.


        :param server_config_ipv6: The server_config_ipv6 of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_config_ipv6 = server_config_ipv6

    @property
    def server_ipv6_encaps(self):
        """Gets the server_ipv6_encaps of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_ipv6_encaps of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_ipv6_encaps

    @server_ipv6_encaps.setter
    def server_ipv6_encaps(self, server_ipv6_encaps):
        """Sets the server_ipv6_encaps of this TsoaPartialServerObject_.


        :param server_ipv6_encaps: The server_ipv6_encaps of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_ipv6_encaps = server_ipv6_encaps

    @property
    def server_ipv6_start(self):
        """Gets the server_ipv6_start of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_ipv6_start of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_ipv6_start

    @server_ipv6_start.setter
    def server_ipv6_start(self, server_ipv6_start):
        """Sets the server_ipv6_start of this TsoaPartialServerObject_.


        :param server_ipv6_start: The server_ipv6_start of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_ipv6_start = server_ipv6_start

    @property
    def server_ipv6_end(self):
        """Gets the server_ipv6_end of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_ipv6_end of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_ipv6_end

    @server_ipv6_end.setter
    def server_ipv6_end(self, server_ipv6_end):
        """Sets the server_ipv6_end of this TsoaPartialServerObject_.


        :param server_ipv6_end: The server_ipv6_end of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_ipv6_end = server_ipv6_end

    @property
    def server_ipv6_serialized(self):
        """Gets the server_ipv6_serialized of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_ipv6_serialized of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: list[str]
        """
        return self._server_ipv6_serialized

    @server_ipv6_serialized.setter
    def server_ipv6_serialized(self, server_ipv6_serialized):
        """Sets the server_ipv6_serialized of this TsoaPartialServerObject_.


        :param server_ipv6_serialized: The server_ipv6_serialized of this TsoaPartialServerObject_.  # noqa: E501
        :type: list[str]
        """

        self._server_ipv6_serialized = server_ipv6_serialized

    @property
    def server_gateway_ipv4(self):
        """Gets the server_gateway_ipv4 of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_gateway_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_gateway_ipv4

    @server_gateway_ipv4.setter
    def server_gateway_ipv4(self, server_gateway_ipv4):
        """Sets the server_gateway_ipv4 of this TsoaPartialServerObject_.


        :param server_gateway_ipv4: The server_gateway_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_gateway_ipv4 = server_gateway_ipv4

    @property
    def server_gateway_ipv6(self):
        """Gets the server_gateway_ipv6 of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_gateway_ipv6 of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_gateway_ipv6

    @server_gateway_ipv6.setter
    def server_gateway_ipv6(self, server_gateway_ipv6):
        """Sets the server_gateway_ipv6 of this TsoaPartialServerObject_.


        :param server_gateway_ipv6: The server_gateway_ipv6 of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_gateway_ipv6 = server_gateway_ipv6

    @property
    def provider_id(self):
        """Gets the provider_id of this TsoaPartialServerObject_.  # noqa: E501


        :return: The provider_id of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: float
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this TsoaPartialServerObject_.


        :param provider_id: The provider_id of this TsoaPartialServerObject_.  # noqa: E501
        :type: float
        """

        self._provider_id = provider_id

    @property
    def topology_id(self):
        """Gets the topology_id of this TsoaPartialServerObject_.  # noqa: E501


        :return: The topology_id of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: float
        """
        return self._topology_id

    @topology_id.setter
    def topology_id(self, topology_id):
        """Sets the topology_id of this TsoaPartialServerObject_.


        :param topology_id: The topology_id of this TsoaPartialServerObject_.  # noqa: E501
        :type: float
        """

        self._topology_id = topology_id

    @property
    def server_sr_software(self):
        """Gets the server_sr_software of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_sr_software of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: ServerSrSoftware
        """
        return self._server_sr_software

    @server_sr_software.setter
    def server_sr_software(self, server_sr_software):
        """Sets the server_sr_software of this TsoaPartialServerObject_.


        :param server_sr_software: The server_sr_software of this TsoaPartialServerObject_.  # noqa: E501
        :type: ServerSrSoftware
        """

        self._server_sr_software = server_sr_software

    @property
    def server_is_transit(self):
        """Gets the server_is_transit of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_is_transit of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: bool
        """
        return self._server_is_transit

    @server_is_transit.setter
    def server_is_transit(self, server_is_transit):
        """Sets the server_is_transit of this TsoaPartialServerObject_.


        :param server_is_transit: The server_is_transit of this TsoaPartialServerObject_.  # noqa: E501
        :type: bool
        """

        self._server_is_transit = server_is_transit

    @property
    def server_is_edge(self):
        """Gets the server_is_edge of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_is_edge of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: bool
        """
        return self._server_is_edge

    @server_is_edge.setter
    def server_is_edge(self, server_is_edge):
        """Sets the server_is_edge of this TsoaPartialServerObject_.


        :param server_is_edge: The server_is_edge of this TsoaPartialServerObject_.  # noqa: E501
        :type: bool
        """

        self._server_is_edge = server_is_edge

    @property
    def server_status(self):
        """Gets the server_status of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_status of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: Status
        """
        return self._server_status

    @server_status.setter
    def server_status(self, server_status):
        """Sets the server_status of this TsoaPartialServerObject_.


        :param server_status: The server_status of this TsoaPartialServerObject_.  # noqa: E501
        :type: Status
        """

        self._server_status = server_status

    @property
    def server_status_reason(self):
        """Gets the server_status_reason of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_status_reason of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_status_reason

    @server_status_reason.setter
    def server_status_reason(self, server_status_reason):
        """Sets the server_status_reason of this TsoaPartialServerObject_.


        :param server_status_reason: The server_status_reason of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_status_reason = server_status_reason

    @property
    def server_location_lat(self):
        """Gets the server_location_lat of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_location_lat of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_location_lat

    @server_location_lat.setter
    def server_location_lat(self, server_location_lat):
        """Sets the server_location_lat of this TsoaPartialServerObject_.


        :param server_location_lat: The server_location_lat of this TsoaPartialServerObject_.  # noqa: E501
        :type: float
        """

        self._server_location_lat = server_location_lat

    @property
    def server_location_lon(self):
        """Gets the server_location_lon of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_location_lon of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_location_lon

    @server_location_lon.setter
    def server_location_lon(self, server_location_lon):
        """Sets the server_location_lon of this TsoaPartialServerObject_.


        :param server_location_lon: The server_location_lon of this TsoaPartialServerObject_.  # noqa: E501
        :type: float
        """

        self._server_location_lon = server_location_lon

    @property
    def server_location_city(self):
        """Gets the server_location_city of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_location_city of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_location_city

    @server_location_city.setter
    def server_location_city(self, server_location_city):
        """Sets the server_location_city of this TsoaPartialServerObject_.


        :param server_location_city: The server_location_city of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_location_city = server_location_city

    @property
    def server_proxy_required(self):
        """Gets the server_proxy_required of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_proxy_required of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: bool
        """
        return self._server_proxy_required

    @server_proxy_required.setter
    def server_proxy_required(self, server_proxy_required):
        """Sets the server_proxy_required of this TsoaPartialServerObject_.


        :param server_proxy_required: The server_proxy_required of this TsoaPartialServerObject_.  # noqa: E501
        :type: bool
        """

        self._server_proxy_required = server_proxy_required

    @property
    def server_tap_ipv4_cidr(self):
        """Gets the server_tap_ipv4_cidr of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_tap_ipv4_cidr of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_tap_ipv4_cidr

    @server_tap_ipv4_cidr.setter
    def server_tap_ipv4_cidr(self, server_tap_ipv4_cidr):
        """Sets the server_tap_ipv4_cidr of this TsoaPartialServerObject_.


        :param server_tap_ipv4_cidr: The server_tap_ipv4_cidr of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_tap_ipv4_cidr = server_tap_ipv4_cidr

    @property
    def server_tap_host_ipv4_cidr(self):
        """Gets the server_tap_host_ipv4_cidr of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_tap_host_ipv4_cidr of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_tap_host_ipv4_cidr

    @server_tap_host_ipv4_cidr.setter
    def server_tap_host_ipv4_cidr(self, server_tap_host_ipv4_cidr):
        """Sets the server_tap_host_ipv4_cidr of this TsoaPartialServerObject_.


        :param server_tap_host_ipv4_cidr: The server_tap_host_ipv4_cidr of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_tap_host_ipv4_cidr = server_tap_host_ipv4_cidr

    @property
    def server_tap_host_bridge(self):
        """Gets the server_tap_host_bridge of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_tap_host_bridge of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_tap_host_bridge

    @server_tap_host_bridge.setter
    def server_tap_host_bridge(self, server_tap_host_bridge):
        """Sets the server_tap_host_bridge of this TsoaPartialServerObject_.


        :param server_tap_host_bridge: The server_tap_host_bridge of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_tap_host_bridge = server_tap_host_bridge

    @property
    def server_public_tap_host_ipv4(self):
        """Gets the server_public_tap_host_ipv4 of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_public_tap_host_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_public_tap_host_ipv4

    @server_public_tap_host_ipv4.setter
    def server_public_tap_host_ipv4(self, server_public_tap_host_ipv4):
        """Sets the server_public_tap_host_ipv4 of this TsoaPartialServerObject_.


        :param server_public_tap_host_ipv4: The server_public_tap_host_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_public_tap_host_ipv4 = server_public_tap_host_ipv4

    @property
    def server_public_tap_vpp_ipv4(self):
        """Gets the server_public_tap_vpp_ipv4 of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_public_tap_vpp_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_public_tap_vpp_ipv4

    @server_public_tap_vpp_ipv4.setter
    def server_public_tap_vpp_ipv4(self, server_public_tap_vpp_ipv4):
        """Sets the server_public_tap_vpp_ipv4 of this TsoaPartialServerObject_.


        :param server_public_tap_vpp_ipv4: The server_public_tap_vpp_ipv4 of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_public_tap_vpp_ipv4 = server_public_tap_vpp_ipv4

    @property
    def server_agent_status(self):
        """Gets the server_agent_status of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_agent_status of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: ServerAgentStatus
        """
        return self._server_agent_status

    @server_agent_status.setter
    def server_agent_status(self, server_agent_status):
        """Sets the server_agent_status of this TsoaPartialServerObject_.


        :param server_agent_status: The server_agent_status of this TsoaPartialServerObject_.  # noqa: E501
        :type: ServerAgentStatus
        """

        self._server_agent_status = server_agent_status

    @property
    def server_agent_key(self):
        """Gets the server_agent_key of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_agent_key of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_agent_key

    @server_agent_key.setter
    def server_agent_key(self, server_agent_key):
        """Sets the server_agent_key of this TsoaPartialServerObject_.


        :param server_agent_key: The server_agent_key of this TsoaPartialServerObject_.  # noqa: E501
        :type: str
        """

        self._server_agent_key = server_agent_key

    @property
    def vpn_id(self):
        """Gets the vpn_id of this TsoaPartialServerObject_.  # noqa: E501


        :return: The vpn_id of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: float
        """
        return self._vpn_id

    @vpn_id.setter
    def vpn_id(self, vpn_id):
        """Sets the vpn_id of this TsoaPartialServerObject_.


        :param vpn_id: The vpn_id of this TsoaPartialServerObject_.  # noqa: E501
        :type: float
        """

        self._vpn_id = vpn_id

    @property
    def server_skip_configuration(self):
        """Gets the server_skip_configuration of this TsoaPartialServerObject_.  # noqa: E501


        :return: The server_skip_configuration of this TsoaPartialServerObject_.  # noqa: E501
        :rtype: bool
        """
        return self._server_skip_configuration

    @server_skip_configuration.setter
    def server_skip_configuration(self, server_skip_configuration):
        """Sets the server_skip_configuration of this TsoaPartialServerObject_.


        :param server_skip_configuration: The server_skip_configuration of this TsoaPartialServerObject_.  # noqa: E501
        :type: bool
        """

        self._server_skip_configuration = server_skip_configuration

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
        if issubclass(TsoaPartialServerObject_, dict):
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
        if not isinstance(other, TsoaPartialServerObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other