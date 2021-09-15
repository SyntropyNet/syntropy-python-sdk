# coding: utf-8

"""
    syntropy-controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from syntropy_sdk.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def setting_create(self, body, **kwargs):  # noqa: E501
        """Update user settings  # noqa: E501

        Update user settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.setting_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingWriteObject body: (required)
        :return: SettingReadObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.setting_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.setting_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def setting_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update user settings  # noqa: E501

        Update user settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.setting_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingWriteObject body: (required)
        :return: SettingReadObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method setting_create" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `setting_create`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["jwt"]  # noqa: E501

        return self.api_client.call_api(
            "/api/settings",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SettingReadObject",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def setting_index(self, **kwargs):  # noqa: E501
        """Get user settings  # noqa: E501

        Get user settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.setting_index(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float skip:
        :param float take:
        :param str order:
        :param str filter:
        :return: list[SettingReadObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.setting_index_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.setting_index_with_http_info(**kwargs)  # noqa: E501
            return data

    def setting_index_with_http_info(self, **kwargs):  # noqa: E501
        """Get user settings  # noqa: E501

        Get user settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.setting_index_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float skip:
        :param float take:
        :param str order:
        :param str filter:
        :return: list[SettingReadObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["skip", "take", "order", "filter"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method setting_index" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "skip" in params:
            query_params.append(("skip", params["skip"]))  # noqa: E501
        if "take" in params:
            query_params.append(("take", params["take"]))  # noqa: E501
        if "order" in params:
            query_params.append(("order", params["order"]))  # noqa: E501
        if "filter" in params:
            query_params.append(("filter", params["filter"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["jwt"]  # noqa: E501

        return self.api_client.call_api(
            "/api/settings",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[SettingReadObject]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
