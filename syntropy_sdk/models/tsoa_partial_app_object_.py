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


class TsoaPartialAppObject_(object):
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
        "server_vin_id": "float",
        "app_location_lat": "float",
        "app_location_lon": "float",
        "app_location_city": "str",
        "app_device_id": "str",
        "app_public_ipv4": "str",
        "app_public_ipv6": "str",
        "app_internal_ipv4": "str",
        "app_public_key": "str",
        "app_status": "AppStatus",
        "app_device_type": "str",
        "app_ws_status": "AppWsStatus",
        "app_x_forwarded_for_ip": "str",
        "app_skip_sdn": "bool",
        "app_debug_mode": "bool",
        "app_not_allowed_internal_ipv4_cidrs": "list[str]",
        "app_dest_unreachable_timeout_sec": "float",
    }

    attribute_map = {
        "user_id": "user_id",
        "server_vin_id": "server_vin_id",
        "app_location_lat": "app_location_lat",
        "app_location_lon": "app_location_lon",
        "app_location_city": "app_location_city",
        "app_device_id": "app_device_id",
        "app_public_ipv4": "app_public_ipv4",
        "app_public_ipv6": "app_public_ipv6",
        "app_internal_ipv4": "app_internal_ipv4",
        "app_public_key": "app_public_key",
        "app_status": "app_status",
        "app_device_type": "app_device_type",
        "app_ws_status": "app_ws_status",
        "app_x_forwarded_for_ip": "app_x_forwarded_for_ip",
        "app_skip_sdn": "app_skip_sdn",
        "app_debug_mode": "app_debug_mode",
        "app_not_allowed_internal_ipv4_cidrs": "app_not_allowed_internal_ipv4_cidrs",
        "app_dest_unreachable_timeout_sec": "app_dest_unreachable_timeout_sec",
    }

    def __init__(
        self,
        user_id=None,
        server_vin_id=None,
        app_location_lat=None,
        app_location_lon=None,
        app_location_city=None,
        app_device_id=None,
        app_public_ipv4=None,
        app_public_ipv6=None,
        app_internal_ipv4=None,
        app_public_key=None,
        app_status=None,
        app_device_type=None,
        app_ws_status=None,
        app_x_forwarded_for_ip=None,
        app_skip_sdn=None,
        app_debug_mode=None,
        app_not_allowed_internal_ipv4_cidrs=None,
        app_dest_unreachable_timeout_sec=None,
    ):  # noqa: E501
        """TsoaPartialAppObject_ - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._server_vin_id = None
        self._app_location_lat = None
        self._app_location_lon = None
        self._app_location_city = None
        self._app_device_id = None
        self._app_public_ipv4 = None
        self._app_public_ipv6 = None
        self._app_internal_ipv4 = None
        self._app_public_key = None
        self._app_status = None
        self._app_device_type = None
        self._app_ws_status = None
        self._app_x_forwarded_for_ip = None
        self._app_skip_sdn = None
        self._app_debug_mode = None
        self._app_not_allowed_internal_ipv4_cidrs = None
        self._app_dest_unreachable_timeout_sec = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if server_vin_id is not None:
            self.server_vin_id = server_vin_id
        if app_location_lat is not None:
            self.app_location_lat = app_location_lat
        if app_location_lon is not None:
            self.app_location_lon = app_location_lon
        if app_location_city is not None:
            self.app_location_city = app_location_city
        if app_device_id is not None:
            self.app_device_id = app_device_id
        if app_public_ipv4 is not None:
            self.app_public_ipv4 = app_public_ipv4
        if app_public_ipv6 is not None:
            self.app_public_ipv6 = app_public_ipv6
        if app_internal_ipv4 is not None:
            self.app_internal_ipv4 = app_internal_ipv4
        if app_public_key is not None:
            self.app_public_key = app_public_key
        if app_status is not None:
            self.app_status = app_status
        if app_device_type is not None:
            self.app_device_type = app_device_type
        if app_ws_status is not None:
            self.app_ws_status = app_ws_status
        if app_x_forwarded_for_ip is not None:
            self.app_x_forwarded_for_ip = app_x_forwarded_for_ip
        if app_skip_sdn is not None:
            self.app_skip_sdn = app_skip_sdn
        if app_debug_mode is not None:
            self.app_debug_mode = app_debug_mode
        if app_not_allowed_internal_ipv4_cidrs is not None:
            self.app_not_allowed_internal_ipv4_cidrs = (
                app_not_allowed_internal_ipv4_cidrs
            )
        if app_dest_unreachable_timeout_sec is not None:
            self.app_dest_unreachable_timeout_sec = app_dest_unreachable_timeout_sec

    @property
    def user_id(self):
        """Gets the user_id of this TsoaPartialAppObject_.  # noqa: E501


        :return: The user_id of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TsoaPartialAppObject_.


        :param user_id: The user_id of this TsoaPartialAppObject_.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def server_vin_id(self):
        """Gets the server_vin_id of this TsoaPartialAppObject_.  # noqa: E501


        :return: The server_vin_id of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_vin_id

    @server_vin_id.setter
    def server_vin_id(self, server_vin_id):
        """Sets the server_vin_id of this TsoaPartialAppObject_.


        :param server_vin_id: The server_vin_id of this TsoaPartialAppObject_.  # noqa: E501
        :type: float
        """

        self._server_vin_id = server_vin_id

    @property
    def app_location_lat(self):
        """Gets the app_location_lat of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_location_lat of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: float
        """
        return self._app_location_lat

    @app_location_lat.setter
    def app_location_lat(self, app_location_lat):
        """Sets the app_location_lat of this TsoaPartialAppObject_.


        :param app_location_lat: The app_location_lat of this TsoaPartialAppObject_.  # noqa: E501
        :type: float
        """

        self._app_location_lat = app_location_lat

    @property
    def app_location_lon(self):
        """Gets the app_location_lon of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_location_lon of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: float
        """
        return self._app_location_lon

    @app_location_lon.setter
    def app_location_lon(self, app_location_lon):
        """Sets the app_location_lon of this TsoaPartialAppObject_.


        :param app_location_lon: The app_location_lon of this TsoaPartialAppObject_.  # noqa: E501
        :type: float
        """

        self._app_location_lon = app_location_lon

    @property
    def app_location_city(self):
        """Gets the app_location_city of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_location_city of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: str
        """
        return self._app_location_city

    @app_location_city.setter
    def app_location_city(self, app_location_city):
        """Sets the app_location_city of this TsoaPartialAppObject_.


        :param app_location_city: The app_location_city of this TsoaPartialAppObject_.  # noqa: E501
        :type: str
        """

        self._app_location_city = app_location_city

    @property
    def app_device_id(self):
        """Gets the app_device_id of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_device_id of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: str
        """
        return self._app_device_id

    @app_device_id.setter
    def app_device_id(self, app_device_id):
        """Sets the app_device_id of this TsoaPartialAppObject_.


        :param app_device_id: The app_device_id of this TsoaPartialAppObject_.  # noqa: E501
        :type: str
        """

        self._app_device_id = app_device_id

    @property
    def app_public_ipv4(self):
        """Gets the app_public_ipv4 of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_public_ipv4 of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: str
        """
        return self._app_public_ipv4

    @app_public_ipv4.setter
    def app_public_ipv4(self, app_public_ipv4):
        """Sets the app_public_ipv4 of this TsoaPartialAppObject_.


        :param app_public_ipv4: The app_public_ipv4 of this TsoaPartialAppObject_.  # noqa: E501
        :type: str
        """

        self._app_public_ipv4 = app_public_ipv4

    @property
    def app_public_ipv6(self):
        """Gets the app_public_ipv6 of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_public_ipv6 of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: str
        """
        return self._app_public_ipv6

    @app_public_ipv6.setter
    def app_public_ipv6(self, app_public_ipv6):
        """Sets the app_public_ipv6 of this TsoaPartialAppObject_.


        :param app_public_ipv6: The app_public_ipv6 of this TsoaPartialAppObject_.  # noqa: E501
        :type: str
        """

        self._app_public_ipv6 = app_public_ipv6

    @property
    def app_internal_ipv4(self):
        """Gets the app_internal_ipv4 of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_internal_ipv4 of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: str
        """
        return self._app_internal_ipv4

    @app_internal_ipv4.setter
    def app_internal_ipv4(self, app_internal_ipv4):
        """Sets the app_internal_ipv4 of this TsoaPartialAppObject_.


        :param app_internal_ipv4: The app_internal_ipv4 of this TsoaPartialAppObject_.  # noqa: E501
        :type: str
        """

        self._app_internal_ipv4 = app_internal_ipv4

    @property
    def app_public_key(self):
        """Gets the app_public_key of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_public_key of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: str
        """
        return self._app_public_key

    @app_public_key.setter
    def app_public_key(self, app_public_key):
        """Sets the app_public_key of this TsoaPartialAppObject_.


        :param app_public_key: The app_public_key of this TsoaPartialAppObject_.  # noqa: E501
        :type: str
        """

        self._app_public_key = app_public_key

    @property
    def app_status(self):
        """Gets the app_status of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_status of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: AppStatus
        """
        return self._app_status

    @app_status.setter
    def app_status(self, app_status):
        """Sets the app_status of this TsoaPartialAppObject_.


        :param app_status: The app_status of this TsoaPartialAppObject_.  # noqa: E501
        :type: AppStatus
        """

        self._app_status = app_status

    @property
    def app_device_type(self):
        """Gets the app_device_type of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_device_type of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: str
        """
        return self._app_device_type

    @app_device_type.setter
    def app_device_type(self, app_device_type):
        """Sets the app_device_type of this TsoaPartialAppObject_.


        :param app_device_type: The app_device_type of this TsoaPartialAppObject_.  # noqa: E501
        :type: str
        """

        self._app_device_type = app_device_type

    @property
    def app_ws_status(self):
        """Gets the app_ws_status of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_ws_status of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: AppWsStatus
        """
        return self._app_ws_status

    @app_ws_status.setter
    def app_ws_status(self, app_ws_status):
        """Sets the app_ws_status of this TsoaPartialAppObject_.


        :param app_ws_status: The app_ws_status of this TsoaPartialAppObject_.  # noqa: E501
        :type: AppWsStatus
        """

        self._app_ws_status = app_ws_status

    @property
    def app_x_forwarded_for_ip(self):
        """Gets the app_x_forwarded_for_ip of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_x_forwarded_for_ip of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: str
        """
        return self._app_x_forwarded_for_ip

    @app_x_forwarded_for_ip.setter
    def app_x_forwarded_for_ip(self, app_x_forwarded_for_ip):
        """Sets the app_x_forwarded_for_ip of this TsoaPartialAppObject_.


        :param app_x_forwarded_for_ip: The app_x_forwarded_for_ip of this TsoaPartialAppObject_.  # noqa: E501
        :type: str
        """

        self._app_x_forwarded_for_ip = app_x_forwarded_for_ip

    @property
    def app_skip_sdn(self):
        """Gets the app_skip_sdn of this TsoaPartialAppObject_.  # noqa: E501

        Flag to tell controller not to route traffic via SDN.  # noqa: E501

        :return: The app_skip_sdn of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: bool
        """
        return self._app_skip_sdn

    @app_skip_sdn.setter
    def app_skip_sdn(self, app_skip_sdn):
        """Sets the app_skip_sdn of this TsoaPartialAppObject_.

        Flag to tell controller not to route traffic via SDN.  # noqa: E501

        :param app_skip_sdn: The app_skip_sdn of this TsoaPartialAppObject_.  # noqa: E501
        :type: bool
        """

        self._app_skip_sdn = app_skip_sdn

    @property
    def app_debug_mode(self):
        """Gets the app_debug_mode of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_debug_mode of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: bool
        """
        return self._app_debug_mode

    @app_debug_mode.setter
    def app_debug_mode(self, app_debug_mode):
        """Sets the app_debug_mode of this TsoaPartialAppObject_.


        :param app_debug_mode: The app_debug_mode of this TsoaPartialAppObject_.  # noqa: E501
        :type: bool
        """

        self._app_debug_mode = app_debug_mode

    @property
    def app_not_allowed_internal_ipv4_cidrs(self):
        """Gets the app_not_allowed_internal_ipv4_cidrs of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_not_allowed_internal_ipv4_cidrs of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_not_allowed_internal_ipv4_cidrs

    @app_not_allowed_internal_ipv4_cidrs.setter
    def app_not_allowed_internal_ipv4_cidrs(self, app_not_allowed_internal_ipv4_cidrs):
        """Sets the app_not_allowed_internal_ipv4_cidrs of this TsoaPartialAppObject_.


        :param app_not_allowed_internal_ipv4_cidrs: The app_not_allowed_internal_ipv4_cidrs of this TsoaPartialAppObject_.  # noqa: E501
        :type: list[str]
        """

        self._app_not_allowed_internal_ipv4_cidrs = app_not_allowed_internal_ipv4_cidrs

    @property
    def app_dest_unreachable_timeout_sec(self):
        """Gets the app_dest_unreachable_timeout_sec of this TsoaPartialAppObject_.  # noqa: E501


        :return: The app_dest_unreachable_timeout_sec of this TsoaPartialAppObject_.  # noqa: E501
        :rtype: float
        """
        return self._app_dest_unreachable_timeout_sec

    @app_dest_unreachable_timeout_sec.setter
    def app_dest_unreachable_timeout_sec(self, app_dest_unreachable_timeout_sec):
        """Sets the app_dest_unreachable_timeout_sec of this TsoaPartialAppObject_.


        :param app_dest_unreachable_timeout_sec: The app_dest_unreachable_timeout_sec of this TsoaPartialAppObject_.  # noqa: E501
        :type: float
        """

        self._app_dest_unreachable_timeout_sec = app_dest_unreachable_timeout_sec

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
        if issubclass(TsoaPartialAppObject_, dict):
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
        if not isinstance(other, TsoaPartialAppObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
