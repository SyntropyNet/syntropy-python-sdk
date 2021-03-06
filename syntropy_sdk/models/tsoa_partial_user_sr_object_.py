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


class TsoaPartialUserSrObject_(object):
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
        "user_id": "float",
        "region_id": "float",
        "user_sr_location_lat": "float",
        "user_sr_location_lon": "float",
        "user_sr_location_city": "str",
        "color_id": "float",
        "bandwidth_min": "float",
        "jitter_max": "float",
        "latency_max": "float",
        "price_max": "float",
        "user_ipv4_source_addr": "str",
        "user_ipv6_source_addr": "str",
        "user_ipv4_dest_addr": "str",
        "user_ipv6_dest_addr": "str",
        "user_ipv4_dest_cidr": "str",
        "user_ipv6_dest_cidr": "str",
        "server_vpn_id": "float",
        "server_vin_id": "float",
        "server_ven_id": "float",
        "sr_policy_id": "float",
        "user_sr_direction": "UserSrDirection",
        "user_sr_status": "Status",
        "user_sr_status_reason": "str",
        "user_sr_is_via_sdn": "bool",
    }

    attribute_map = {
        "user_id": "user_id",
        "region_id": "region_id",
        "user_sr_location_lat": "user_sr_location_lat",
        "user_sr_location_lon": "user_sr_location_lon",
        "user_sr_location_city": "user_sr_location_city",
        "color_id": "color_id",
        "bandwidth_min": "bandwidth_min",
        "jitter_max": "jitter_max",
        "latency_max": "latency_max",
        "price_max": "price_max",
        "user_ipv4_source_addr": "user_ipv4_source_addr",
        "user_ipv6_source_addr": "user_ipv6_source_addr",
        "user_ipv4_dest_addr": "user_ipv4_dest_addr",
        "user_ipv6_dest_addr": "user_ipv6_dest_addr",
        "user_ipv4_dest_cidr": "user_ipv4_dest_cidr",
        "user_ipv6_dest_cidr": "user_ipv6_dest_cidr",
        "server_vpn_id": "server_vpn_id",
        "server_vin_id": "server_vin_id",
        "server_ven_id": "server_ven_id",
        "sr_policy_id": "sr_policy_id",
        "user_sr_direction": "user_sr_direction",
        "user_sr_status": "user_sr_status",
        "user_sr_status_reason": "user_sr_status_reason",
        "user_sr_is_via_sdn": "user_sr_is_via_sdn",
    }

    def __init__(
        self,
        user_id=None,
        region_id=None,
        user_sr_location_lat=None,
        user_sr_location_lon=None,
        user_sr_location_city=None,
        color_id=None,
        bandwidth_min=None,
        jitter_max=None,
        latency_max=None,
        price_max=None,
        user_ipv4_source_addr=None,
        user_ipv6_source_addr=None,
        user_ipv4_dest_addr=None,
        user_ipv6_dest_addr=None,
        user_ipv4_dest_cidr=None,
        user_ipv6_dest_cidr=None,
        server_vpn_id=None,
        server_vin_id=None,
        server_ven_id=None,
        sr_policy_id=None,
        user_sr_direction=None,
        user_sr_status=None,
        user_sr_status_reason=None,
        user_sr_is_via_sdn=None,
    ):  # noqa: E501
        """TsoaPartialUserSrObject_ - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._region_id = None
        self._user_sr_location_lat = None
        self._user_sr_location_lon = None
        self._user_sr_location_city = None
        self._color_id = None
        self._bandwidth_min = None
        self._jitter_max = None
        self._latency_max = None
        self._price_max = None
        self._user_ipv4_source_addr = None
        self._user_ipv6_source_addr = None
        self._user_ipv4_dest_addr = None
        self._user_ipv6_dest_addr = None
        self._user_ipv4_dest_cidr = None
        self._user_ipv6_dest_cidr = None
        self._server_vpn_id = None
        self._server_vin_id = None
        self._server_ven_id = None
        self._sr_policy_id = None
        self._user_sr_direction = None
        self._user_sr_status = None
        self._user_sr_status_reason = None
        self._user_sr_is_via_sdn = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if region_id is not None:
            self.region_id = region_id
        if user_sr_location_lat is not None:
            self.user_sr_location_lat = user_sr_location_lat
        if user_sr_location_lon is not None:
            self.user_sr_location_lon = user_sr_location_lon
        if user_sr_location_city is not None:
            self.user_sr_location_city = user_sr_location_city
        if color_id is not None:
            self.color_id = color_id
        if bandwidth_min is not None:
            self.bandwidth_min = bandwidth_min
        if jitter_max is not None:
            self.jitter_max = jitter_max
        if latency_max is not None:
            self.latency_max = latency_max
        if price_max is not None:
            self.price_max = price_max
        if user_ipv4_source_addr is not None:
            self.user_ipv4_source_addr = user_ipv4_source_addr
        if user_ipv6_source_addr is not None:
            self.user_ipv6_source_addr = user_ipv6_source_addr
        if user_ipv4_dest_addr is not None:
            self.user_ipv4_dest_addr = user_ipv4_dest_addr
        if user_ipv6_dest_addr is not None:
            self.user_ipv6_dest_addr = user_ipv6_dest_addr
        if user_ipv4_dest_cidr is not None:
            self.user_ipv4_dest_cidr = user_ipv4_dest_cidr
        if user_ipv6_dest_cidr is not None:
            self.user_ipv6_dest_cidr = user_ipv6_dest_cidr
        if server_vpn_id is not None:
            self.server_vpn_id = server_vpn_id
        if server_vin_id is not None:
            self.server_vin_id = server_vin_id
        if server_ven_id is not None:
            self.server_ven_id = server_ven_id
        if sr_policy_id is not None:
            self.sr_policy_id = sr_policy_id
        if user_sr_direction is not None:
            self.user_sr_direction = user_sr_direction
        if user_sr_status is not None:
            self.user_sr_status = user_sr_status
        if user_sr_status_reason is not None:
            self.user_sr_status_reason = user_sr_status_reason
        if user_sr_is_via_sdn is not None:
            self.user_sr_is_via_sdn = user_sr_is_via_sdn

    @property
    def user_id(self):
        """Gets the user_id of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TsoaPartialUserSrObject_.


        :param user_id: The user_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def region_id(self):
        """Gets the region_id of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The region_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this TsoaPartialUserSrObject_.


        :param region_id: The region_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._region_id = region_id

    @property
    def user_sr_location_lat(self):
        """Gets the user_sr_location_lat of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_sr_location_lat of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._user_sr_location_lat

    @user_sr_location_lat.setter
    def user_sr_location_lat(self, user_sr_location_lat):
        """Sets the user_sr_location_lat of this TsoaPartialUserSrObject_.


        :param user_sr_location_lat: The user_sr_location_lat of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._user_sr_location_lat = user_sr_location_lat

    @property
    def user_sr_location_lon(self):
        """Gets the user_sr_location_lon of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_sr_location_lon of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._user_sr_location_lon

    @user_sr_location_lon.setter
    def user_sr_location_lon(self, user_sr_location_lon):
        """Sets the user_sr_location_lon of this TsoaPartialUserSrObject_.


        :param user_sr_location_lon: The user_sr_location_lon of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._user_sr_location_lon = user_sr_location_lon

    @property
    def user_sr_location_city(self):
        """Gets the user_sr_location_city of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_sr_location_city of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: str
        """
        return self._user_sr_location_city

    @user_sr_location_city.setter
    def user_sr_location_city(self, user_sr_location_city):
        """Sets the user_sr_location_city of this TsoaPartialUserSrObject_.


        :param user_sr_location_city: The user_sr_location_city of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: str
        """

        self._user_sr_location_city = user_sr_location_city

    @property
    def color_id(self):
        """Gets the color_id of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The color_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._color_id

    @color_id.setter
    def color_id(self, color_id):
        """Sets the color_id of this TsoaPartialUserSrObject_.


        :param color_id: The color_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._color_id = color_id

    @property
    def bandwidth_min(self):
        """Gets the bandwidth_min of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The bandwidth_min of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._bandwidth_min

    @bandwidth_min.setter
    def bandwidth_min(self, bandwidth_min):
        """Sets the bandwidth_min of this TsoaPartialUserSrObject_.


        :param bandwidth_min: The bandwidth_min of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._bandwidth_min = bandwidth_min

    @property
    def jitter_max(self):
        """Gets the jitter_max of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The jitter_max of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._jitter_max

    @jitter_max.setter
    def jitter_max(self, jitter_max):
        """Sets the jitter_max of this TsoaPartialUserSrObject_.


        :param jitter_max: The jitter_max of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._jitter_max = jitter_max

    @property
    def latency_max(self):
        """Gets the latency_max of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The latency_max of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._latency_max

    @latency_max.setter
    def latency_max(self, latency_max):
        """Sets the latency_max of this TsoaPartialUserSrObject_.


        :param latency_max: The latency_max of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._latency_max = latency_max

    @property
    def price_max(self):
        """Gets the price_max of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The price_max of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._price_max

    @price_max.setter
    def price_max(self, price_max):
        """Sets the price_max of this TsoaPartialUserSrObject_.


        :param price_max: The price_max of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._price_max = price_max

    @property
    def user_ipv4_source_addr(self):
        """Gets the user_ipv4_source_addr of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_ipv4_source_addr of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: str
        """
        return self._user_ipv4_source_addr

    @user_ipv4_source_addr.setter
    def user_ipv4_source_addr(self, user_ipv4_source_addr):
        """Sets the user_ipv4_source_addr of this TsoaPartialUserSrObject_.


        :param user_ipv4_source_addr: The user_ipv4_source_addr of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: str
        """

        self._user_ipv4_source_addr = user_ipv4_source_addr

    @property
    def user_ipv6_source_addr(self):
        """Gets the user_ipv6_source_addr of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_ipv6_source_addr of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: str
        """
        return self._user_ipv6_source_addr

    @user_ipv6_source_addr.setter
    def user_ipv6_source_addr(self, user_ipv6_source_addr):
        """Sets the user_ipv6_source_addr of this TsoaPartialUserSrObject_.


        :param user_ipv6_source_addr: The user_ipv6_source_addr of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: str
        """

        self._user_ipv6_source_addr = user_ipv6_source_addr

    @property
    def user_ipv4_dest_addr(self):
        """Gets the user_ipv4_dest_addr of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_ipv4_dest_addr of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: str
        """
        return self._user_ipv4_dest_addr

    @user_ipv4_dest_addr.setter
    def user_ipv4_dest_addr(self, user_ipv4_dest_addr):
        """Sets the user_ipv4_dest_addr of this TsoaPartialUserSrObject_.


        :param user_ipv4_dest_addr: The user_ipv4_dest_addr of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: str
        """

        self._user_ipv4_dest_addr = user_ipv4_dest_addr

    @property
    def user_ipv6_dest_addr(self):
        """Gets the user_ipv6_dest_addr of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_ipv6_dest_addr of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: str
        """
        return self._user_ipv6_dest_addr

    @user_ipv6_dest_addr.setter
    def user_ipv6_dest_addr(self, user_ipv6_dest_addr):
        """Sets the user_ipv6_dest_addr of this TsoaPartialUserSrObject_.


        :param user_ipv6_dest_addr: The user_ipv6_dest_addr of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: str
        """

        self._user_ipv6_dest_addr = user_ipv6_dest_addr

    @property
    def user_ipv4_dest_cidr(self):
        """Gets the user_ipv4_dest_cidr of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_ipv4_dest_cidr of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: str
        """
        return self._user_ipv4_dest_cidr

    @user_ipv4_dest_cidr.setter
    def user_ipv4_dest_cidr(self, user_ipv4_dest_cidr):
        """Sets the user_ipv4_dest_cidr of this TsoaPartialUserSrObject_.


        :param user_ipv4_dest_cidr: The user_ipv4_dest_cidr of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: str
        """

        self._user_ipv4_dest_cidr = user_ipv4_dest_cidr

    @property
    def user_ipv6_dest_cidr(self):
        """Gets the user_ipv6_dest_cidr of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_ipv6_dest_cidr of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: str
        """
        return self._user_ipv6_dest_cidr

    @user_ipv6_dest_cidr.setter
    def user_ipv6_dest_cidr(self, user_ipv6_dest_cidr):
        """Sets the user_ipv6_dest_cidr of this TsoaPartialUserSrObject_.


        :param user_ipv6_dest_cidr: The user_ipv6_dest_cidr of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: str
        """

        self._user_ipv6_dest_cidr = user_ipv6_dest_cidr

    @property
    def server_vpn_id(self):
        """Gets the server_vpn_id of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The server_vpn_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_vpn_id

    @server_vpn_id.setter
    def server_vpn_id(self, server_vpn_id):
        """Sets the server_vpn_id of this TsoaPartialUserSrObject_.


        :param server_vpn_id: The server_vpn_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._server_vpn_id = server_vpn_id

    @property
    def server_vin_id(self):
        """Gets the server_vin_id of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The server_vin_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_vin_id

    @server_vin_id.setter
    def server_vin_id(self, server_vin_id):
        """Sets the server_vin_id of this TsoaPartialUserSrObject_.


        :param server_vin_id: The server_vin_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._server_vin_id = server_vin_id

    @property
    def server_ven_id(self):
        """Gets the server_ven_id of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The server_ven_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_ven_id

    @server_ven_id.setter
    def server_ven_id(self, server_ven_id):
        """Sets the server_ven_id of this TsoaPartialUserSrObject_.


        :param server_ven_id: The server_ven_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._server_ven_id = server_ven_id

    @property
    def sr_policy_id(self):
        """Gets the sr_policy_id of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The sr_policy_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: float
        """
        return self._sr_policy_id

    @sr_policy_id.setter
    def sr_policy_id(self, sr_policy_id):
        """Sets the sr_policy_id of this TsoaPartialUserSrObject_.


        :param sr_policy_id: The sr_policy_id of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: float
        """

        self._sr_policy_id = sr_policy_id

    @property
    def user_sr_direction(self):
        """Gets the user_sr_direction of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_sr_direction of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: UserSrDirection
        """
        return self._user_sr_direction

    @user_sr_direction.setter
    def user_sr_direction(self, user_sr_direction):
        """Sets the user_sr_direction of this TsoaPartialUserSrObject_.


        :param user_sr_direction: The user_sr_direction of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: UserSrDirection
        """

        self._user_sr_direction = user_sr_direction

    @property
    def user_sr_status(self):
        """Gets the user_sr_status of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_sr_status of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: Status
        """
        return self._user_sr_status

    @user_sr_status.setter
    def user_sr_status(self, user_sr_status):
        """Sets the user_sr_status of this TsoaPartialUserSrObject_.


        :param user_sr_status: The user_sr_status of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: Status
        """

        self._user_sr_status = user_sr_status

    @property
    def user_sr_status_reason(self):
        """Gets the user_sr_status_reason of this TsoaPartialUserSrObject_.  # noqa: E501


        :return: The user_sr_status_reason of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: str
        """
        return self._user_sr_status_reason

    @user_sr_status_reason.setter
    def user_sr_status_reason(self, user_sr_status_reason):
        """Sets the user_sr_status_reason of this TsoaPartialUserSrObject_.


        :param user_sr_status_reason: The user_sr_status_reason of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: str
        """

        self._user_sr_status_reason = user_sr_status_reason

    @property
    def user_sr_is_via_sdn(self):
        """Gets the user_sr_is_via_sdn of this TsoaPartialUserSrObject_.  # noqa: E501

        Indicates if current configuration routes traffic via SDN.  # noqa: E501

        :return: The user_sr_is_via_sdn of this TsoaPartialUserSrObject_.  # noqa: E501
        :rtype: bool
        """
        return self._user_sr_is_via_sdn

    @user_sr_is_via_sdn.setter
    def user_sr_is_via_sdn(self, user_sr_is_via_sdn):
        """Sets the user_sr_is_via_sdn of this TsoaPartialUserSrObject_.

        Indicates if current configuration routes traffic via SDN.  # noqa: E501

        :param user_sr_is_via_sdn: The user_sr_is_via_sdn of this TsoaPartialUserSrObject_.  # noqa: E501
        :type: bool
        """

        self._user_sr_is_via_sdn = user_sr_is_via_sdn

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
        if issubclass(TsoaPartialUserSrObject_, dict):
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
        if not isinstance(other, TsoaPartialUserSrObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
