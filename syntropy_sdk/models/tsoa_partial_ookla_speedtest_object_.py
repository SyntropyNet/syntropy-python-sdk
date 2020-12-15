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


class TsoaPartialOoklaSpeedtestObject_(object):
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
        "app_id": "float",
        "server_vpn_id": "float",
        "ookla_speedtest_via": "SpeedtestVia",
        "ookla_speedtest_src_ipv4": "str",
        "ookla_speedtest_dst_ipv4": "str",
        "ookla_speedtest_latency": "float",
        "ookla_speedtest_http_latency": "float",
        "ookla_speedtest_icmp_latency": "float",
        "ookla_speedtest_download": "float",
        "ookla_speedtest_upload": "float",
        "ookla_speedtest_country": "str",
        "ookla_speedtest_city": "str",
        "ookla_speedtest_host": "str",
        "ookla_speedtest_execution_time": "float",
        "ookla_speedtest_traceroute": "str",
        "sr_policy_fw_route": "list[float]",
        "sr_policy_bw_route": "list[float]",
    }

    attribute_map = {
        "user_id": "user_id",
        "app_id": "app_id",
        "server_vpn_id": "server_vpn_id",
        "ookla_speedtest_via": "ookla_speedtest_via",
        "ookla_speedtest_src_ipv4": "ookla_speedtest_src_ipv4",
        "ookla_speedtest_dst_ipv4": "ookla_speedtest_dst_ipv4",
        "ookla_speedtest_latency": "ookla_speedtest_latency",
        "ookla_speedtest_http_latency": "ookla_speedtest_http_latency",
        "ookla_speedtest_icmp_latency": "ookla_speedtest_icmp_latency",
        "ookla_speedtest_download": "ookla_speedtest_download",
        "ookla_speedtest_upload": "ookla_speedtest_upload",
        "ookla_speedtest_country": "ookla_speedtest_country",
        "ookla_speedtest_city": "ookla_speedtest_city",
        "ookla_speedtest_host": "ookla_speedtest_host",
        "ookla_speedtest_execution_time": "ookla_speedtest_execution_time",
        "ookla_speedtest_traceroute": "ookla_speedtest_traceroute",
        "sr_policy_fw_route": "sr_policy_fw_route",
        "sr_policy_bw_route": "sr_policy_bw_route",
    }

    def __init__(
        self,
        user_id=None,
        app_id=None,
        server_vpn_id=None,
        ookla_speedtest_via=None,
        ookla_speedtest_src_ipv4=None,
        ookla_speedtest_dst_ipv4=None,
        ookla_speedtest_latency=None,
        ookla_speedtest_http_latency=None,
        ookla_speedtest_icmp_latency=None,
        ookla_speedtest_download=None,
        ookla_speedtest_upload=None,
        ookla_speedtest_country=None,
        ookla_speedtest_city=None,
        ookla_speedtest_host=None,
        ookla_speedtest_execution_time=None,
        ookla_speedtest_traceroute=None,
        sr_policy_fw_route=None,
        sr_policy_bw_route=None,
    ):  # noqa: E501
        """TsoaPartialOoklaSpeedtestObject_ - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._app_id = None
        self._server_vpn_id = None
        self._ookla_speedtest_via = None
        self._ookla_speedtest_src_ipv4 = None
        self._ookla_speedtest_dst_ipv4 = None
        self._ookla_speedtest_latency = None
        self._ookla_speedtest_http_latency = None
        self._ookla_speedtest_icmp_latency = None
        self._ookla_speedtest_download = None
        self._ookla_speedtest_upload = None
        self._ookla_speedtest_country = None
        self._ookla_speedtest_city = None
        self._ookla_speedtest_host = None
        self._ookla_speedtest_execution_time = None
        self._ookla_speedtest_traceroute = None
        self._sr_policy_fw_route = None
        self._sr_policy_bw_route = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if app_id is not None:
            self.app_id = app_id
        if server_vpn_id is not None:
            self.server_vpn_id = server_vpn_id
        if ookla_speedtest_via is not None:
            self.ookla_speedtest_via = ookla_speedtest_via
        if ookla_speedtest_src_ipv4 is not None:
            self.ookla_speedtest_src_ipv4 = ookla_speedtest_src_ipv4
        if ookla_speedtest_dst_ipv4 is not None:
            self.ookla_speedtest_dst_ipv4 = ookla_speedtest_dst_ipv4
        if ookla_speedtest_latency is not None:
            self.ookla_speedtest_latency = ookla_speedtest_latency
        if ookla_speedtest_http_latency is not None:
            self.ookla_speedtest_http_latency = ookla_speedtest_http_latency
        if ookla_speedtest_icmp_latency is not None:
            self.ookla_speedtest_icmp_latency = ookla_speedtest_icmp_latency
        if ookla_speedtest_download is not None:
            self.ookla_speedtest_download = ookla_speedtest_download
        if ookla_speedtest_upload is not None:
            self.ookla_speedtest_upload = ookla_speedtest_upload
        if ookla_speedtest_country is not None:
            self.ookla_speedtest_country = ookla_speedtest_country
        if ookla_speedtest_city is not None:
            self.ookla_speedtest_city = ookla_speedtest_city
        if ookla_speedtest_host is not None:
            self.ookla_speedtest_host = ookla_speedtest_host
        if ookla_speedtest_execution_time is not None:
            self.ookla_speedtest_execution_time = ookla_speedtest_execution_time
        if ookla_speedtest_traceroute is not None:
            self.ookla_speedtest_traceroute = ookla_speedtest_traceroute
        if sr_policy_fw_route is not None:
            self.sr_policy_fw_route = sr_policy_fw_route
        if sr_policy_bw_route is not None:
            self.sr_policy_bw_route = sr_policy_bw_route

    @property
    def user_id(self):
        """Gets the user_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The user_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TsoaPartialOoklaSpeedtestObject_.


        :param user_id: The user_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def app_id(self):
        """Gets the app_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The app_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this TsoaPartialOoklaSpeedtestObject_.


        :param app_id: The app_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._app_id = app_id

    @property
    def server_vpn_id(self):
        """Gets the server_vpn_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The server_vpn_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_vpn_id

    @server_vpn_id.setter
    def server_vpn_id(self, server_vpn_id):
        """Sets the server_vpn_id of this TsoaPartialOoklaSpeedtestObject_.


        :param server_vpn_id: The server_vpn_id of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._server_vpn_id = server_vpn_id

    @property
    def ookla_speedtest_via(self):
        """Gets the ookla_speedtest_via of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_via of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: SpeedtestVia
        """
        return self._ookla_speedtest_via

    @ookla_speedtest_via.setter
    def ookla_speedtest_via(self, ookla_speedtest_via):
        """Sets the ookla_speedtest_via of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_via: The ookla_speedtest_via of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: SpeedtestVia
        """

        self._ookla_speedtest_via = ookla_speedtest_via

    @property
    def ookla_speedtest_src_ipv4(self):
        """Gets the ookla_speedtest_src_ipv4 of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_src_ipv4 of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: str
        """
        return self._ookla_speedtest_src_ipv4

    @ookla_speedtest_src_ipv4.setter
    def ookla_speedtest_src_ipv4(self, ookla_speedtest_src_ipv4):
        """Sets the ookla_speedtest_src_ipv4 of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_src_ipv4: The ookla_speedtest_src_ipv4 of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: str
        """

        self._ookla_speedtest_src_ipv4 = ookla_speedtest_src_ipv4

    @property
    def ookla_speedtest_dst_ipv4(self):
        """Gets the ookla_speedtest_dst_ipv4 of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_dst_ipv4 of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: str
        """
        return self._ookla_speedtest_dst_ipv4

    @ookla_speedtest_dst_ipv4.setter
    def ookla_speedtest_dst_ipv4(self, ookla_speedtest_dst_ipv4):
        """Sets the ookla_speedtest_dst_ipv4 of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_dst_ipv4: The ookla_speedtest_dst_ipv4 of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: str
        """

        self._ookla_speedtest_dst_ipv4 = ookla_speedtest_dst_ipv4

    @property
    def ookla_speedtest_latency(self):
        """Gets the ookla_speedtest_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._ookla_speedtest_latency

    @ookla_speedtest_latency.setter
    def ookla_speedtest_latency(self, ookla_speedtest_latency):
        """Sets the ookla_speedtest_latency of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_latency: The ookla_speedtest_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._ookla_speedtest_latency = ookla_speedtest_latency

    @property
    def ookla_speedtest_http_latency(self):
        """Gets the ookla_speedtest_http_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_http_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._ookla_speedtest_http_latency

    @ookla_speedtest_http_latency.setter
    def ookla_speedtest_http_latency(self, ookla_speedtest_http_latency):
        """Sets the ookla_speedtest_http_latency of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_http_latency: The ookla_speedtest_http_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._ookla_speedtest_http_latency = ookla_speedtest_http_latency

    @property
    def ookla_speedtest_icmp_latency(self):
        """Gets the ookla_speedtest_icmp_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_icmp_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._ookla_speedtest_icmp_latency

    @ookla_speedtest_icmp_latency.setter
    def ookla_speedtest_icmp_latency(self, ookla_speedtest_icmp_latency):
        """Sets the ookla_speedtest_icmp_latency of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_icmp_latency: The ookla_speedtest_icmp_latency of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._ookla_speedtest_icmp_latency = ookla_speedtest_icmp_latency

    @property
    def ookla_speedtest_download(self):
        """Gets the ookla_speedtest_download of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_download of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._ookla_speedtest_download

    @ookla_speedtest_download.setter
    def ookla_speedtest_download(self, ookla_speedtest_download):
        """Sets the ookla_speedtest_download of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_download: The ookla_speedtest_download of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._ookla_speedtest_download = ookla_speedtest_download

    @property
    def ookla_speedtest_upload(self):
        """Gets the ookla_speedtest_upload of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_upload of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._ookla_speedtest_upload

    @ookla_speedtest_upload.setter
    def ookla_speedtest_upload(self, ookla_speedtest_upload):
        """Sets the ookla_speedtest_upload of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_upload: The ookla_speedtest_upload of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._ookla_speedtest_upload = ookla_speedtest_upload

    @property
    def ookla_speedtest_country(self):
        """Gets the ookla_speedtest_country of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_country of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: str
        """
        return self._ookla_speedtest_country

    @ookla_speedtest_country.setter
    def ookla_speedtest_country(self, ookla_speedtest_country):
        """Sets the ookla_speedtest_country of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_country: The ookla_speedtest_country of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: str
        """

        self._ookla_speedtest_country = ookla_speedtest_country

    @property
    def ookla_speedtest_city(self):
        """Gets the ookla_speedtest_city of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_city of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: str
        """
        return self._ookla_speedtest_city

    @ookla_speedtest_city.setter
    def ookla_speedtest_city(self, ookla_speedtest_city):
        """Sets the ookla_speedtest_city of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_city: The ookla_speedtest_city of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: str
        """

        self._ookla_speedtest_city = ookla_speedtest_city

    @property
    def ookla_speedtest_host(self):
        """Gets the ookla_speedtest_host of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_host of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: str
        """
        return self._ookla_speedtest_host

    @ookla_speedtest_host.setter
    def ookla_speedtest_host(self, ookla_speedtest_host):
        """Sets the ookla_speedtest_host of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_host: The ookla_speedtest_host of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: str
        """

        self._ookla_speedtest_host = ookla_speedtest_host

    @property
    def ookla_speedtest_execution_time(self):
        """Gets the ookla_speedtest_execution_time of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_execution_time of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: float
        """
        return self._ookla_speedtest_execution_time

    @ookla_speedtest_execution_time.setter
    def ookla_speedtest_execution_time(self, ookla_speedtest_execution_time):
        """Sets the ookla_speedtest_execution_time of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_execution_time: The ookla_speedtest_execution_time of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: float
        """

        self._ookla_speedtest_execution_time = ookla_speedtest_execution_time

    @property
    def ookla_speedtest_traceroute(self):
        """Gets the ookla_speedtest_traceroute of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The ookla_speedtest_traceroute of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: str
        """
        return self._ookla_speedtest_traceroute

    @ookla_speedtest_traceroute.setter
    def ookla_speedtest_traceroute(self, ookla_speedtest_traceroute):
        """Sets the ookla_speedtest_traceroute of this TsoaPartialOoklaSpeedtestObject_.


        :param ookla_speedtest_traceroute: The ookla_speedtest_traceroute of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: str
        """

        self._ookla_speedtest_traceroute = ookla_speedtest_traceroute

    @property
    def sr_policy_fw_route(self):
        """Gets the sr_policy_fw_route of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The sr_policy_fw_route of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: list[float]
        """
        return self._sr_policy_fw_route

    @sr_policy_fw_route.setter
    def sr_policy_fw_route(self, sr_policy_fw_route):
        """Sets the sr_policy_fw_route of this TsoaPartialOoklaSpeedtestObject_.


        :param sr_policy_fw_route: The sr_policy_fw_route of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: list[float]
        """

        self._sr_policy_fw_route = sr_policy_fw_route

    @property
    def sr_policy_bw_route(self):
        """Gets the sr_policy_bw_route of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501


        :return: The sr_policy_bw_route of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :rtype: list[float]
        """
        return self._sr_policy_bw_route

    @sr_policy_bw_route.setter
    def sr_policy_bw_route(self, sr_policy_bw_route):
        """Sets the sr_policy_bw_route of this TsoaPartialOoklaSpeedtestObject_.


        :param sr_policy_bw_route: The sr_policy_bw_route of this TsoaPartialOoklaSpeedtestObject_.  # noqa: E501
        :type: list[float]
        """

        self._sr_policy_bw_route = sr_policy_bw_route

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
        if issubclass(TsoaPartialOoklaSpeedtestObject_, dict):
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
        if not isinstance(other, TsoaPartialOoklaSpeedtestObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
