# coding: utf-8

"""
    syntropy-auth-service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from syntropy_sdk.api_client import ApiClient


class AuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_contact(self, body, **kwargs):  # noqa: E501
        """Update user contacts  # noqa: E501

        Update contacts information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_contact(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContactRequest body: (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.add_contact_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_contact_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_contact_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update user contacts  # noqa: E501

        Update contacts information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_contact_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContactRequest body: (required)
        :return: Object
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
                    " to method add_contact" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `add_contact`"
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
            "/auth/authorization/contact",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Object",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def auth_access_token_list(self, **kwargs):  # noqa: E501
        """Get access tokens  # noqa: E501

        List access tokens.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float skip:
        :param float take:
        :param AccessTokenOrder order:
        :return: list[AccessTokenReadData]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.auth_access_token_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.auth_access_token_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def auth_access_token_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get access tokens  # noqa: E501

        List access tokens.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float skip:
        :param float take:
        :param AccessTokenOrder order:
        :return: list[AccessTokenReadData]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["skip", "take", "order"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_access_token_list" % key
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
            "/auth/authorization/access-token",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[AccessTokenReadData]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def auth_access_token_login(self, body, **kwargs):  # noqa: E501
        """Login (access token)  # noqa: E501

        Retrieve JWT from access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_login(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessTokenData body: (required)
        :return: AzureUserTokenDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.auth_access_token_login_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.auth_access_token_login_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def auth_access_token_login_with_http_info(self, body, **kwargs):  # noqa: E501
        """Login (access token)  # noqa: E501

        Retrieve JWT from access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_login_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessTokenData body: (required)
        :return: AzureUserTokenDto
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
                    " to method auth_access_token_login" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `auth_access_token_login`"
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/auth/authorization/access-token/login",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="AzureUserTokenDto",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def auth_access_token_permissions_list(self, **kwargs):  # noqa: E501
        """Get access token permissions  # noqa: E501

        Entire list of available permissions access tokens can have.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_permissions_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[PermissionObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.auth_access_token_permissions_list_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.auth_access_token_permissions_list_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def auth_access_token_permissions_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get access token permissions  # noqa: E501

        Entire list of available permissions access tokens can have.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_permissions_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[PermissionObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_access_token_permissions_list" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

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
            "/auth/authorization/permissions/access-token",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[PermissionObject]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def auth_access_token_user_create(self, body, **kwargs):  # noqa: E501
        """Create access token  # noqa: E501

        Create scopes access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_user_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessTokenWriteData body: (required)
        :return: AccessTokenData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.auth_access_token_user_create_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.auth_access_token_user_create_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def auth_access_token_user_create_with_http_info(
        self, body, **kwargs
    ):  # noqa: E501
        """Create access token  # noqa: E501

        Create scopes access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_user_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessTokenWriteData body: (required)
        :return: AccessTokenData
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
                    " to method auth_access_token_user_create" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `auth_access_token_user_create`"
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
            "/auth/authorization/access-token",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="AccessTokenData",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def auth_access_token_user_delete(self, id, **kwargs):  # noqa: E501
        """Delete access token  # noqa: E501

        Delete scopes access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_user_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.auth_access_token_user_delete_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.auth_access_token_user_delete_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def auth_access_token_user_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete access token  # noqa: E501

        Delete scopes access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_access_token_user_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_access_token_user_delete" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `auth_access_token_user_delete`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

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
            "/auth/authorization/access-token/{id}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Object",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def auth_logout(self, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        Deletes session cookies.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_logout(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.auth_logout_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.auth_logout_with_http_info(**kwargs)  # noqa: E501
            return data

    def auth_logout_with_http_info(self, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        Deletes session cookies.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_logout_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_logout" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["jwt"]  # noqa: E501

        return self.api_client.call_api(
            "/auth/authorization/logout",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def auth_show_user(self, **kwargs):  # noqa: E501
        """Get user info  # noqa: E501

        Returns authorized user data. This is recommended way to get the latest user's information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_show_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.auth_show_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.auth_show_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def auth_show_user_with_http_info(self, **kwargs):  # noqa: E501
        """Get user info  # noqa: E501

        Returns authorized user data. This is recommended way to get the latest user's information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_show_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_show_user" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

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
            "/auth/authorization/user",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UserDataResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def auth_verify_email(self, code, **kwargs):  # noqa: E501
        """Verify email  # noqa: E501

        Verifies user's email address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_verify_email(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Email verification code (received by mail). (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.auth_verify_email_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.auth_verify_email_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def auth_verify_email_with_http_info(self, code, **kwargs):  # noqa: E501
        """Verify email  # noqa: E501

        Verifies user's email address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_verify_email_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Email verification code (received by mail). (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["code"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_verify_email" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'code' is set
        if "code" not in params or params["code"] is None:
            raise ValueError(
                "Missing the required parameter `code` when calling `auth_verify_email`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "code" in params:
            path_params["code"] = params["code"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/auth/authorization/verify-email/{code}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Object",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_settings(self, body, **kwargs):  # noqa: E501
        """Update user settings  # noqa: E501

        Update user settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserSettingsObject body: (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_settings_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_settings_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_settings_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update user settings  # noqa: E501

        Update user settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserSettingsObject body: (required)
        :return: Object
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
                    " to method update_settings" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `update_settings`"
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
            "/auth/authorization/settings",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Object",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
