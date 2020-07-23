# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen, especially when using code generation. The order of JSON attributes is not guaranteed.   # noqa: E501

    OpenAPI spec version: 0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from kimai_python.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_users_get(self, **kwargs):  # noqa: E501
        """Returns the collection of all registered users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str visible: Visibility status to filter users. Allowed values: 1=visible, 2=hidden, 3=all (default: 1)
        :param str order_by: The field by which results will be ordered. Allowed values: id, username, alias, email (default: username)
        :param str order: The result order. Allowed values: ASC, DESC (default: ASC)
        :param str term: Free search term
        :return: list[UserCollection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns the collection of all registered users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str visible: Visibility status to filter users. Allowed values: 1=visible, 2=hidden, 3=all (default: 1)
        :param str order_by: The field by which results will be ordered. Allowed values: id, username, alias, email (default: username)
        :param str order: The result order. Allowed values: ASC, DESC (default: ASC)
        :param str term: Free search term
        :return: list[UserCollection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['visible', 'order_by', 'order', 'term']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_users_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'visible' in params and not re.match(r'1|2|3', params['visible']):  # noqa: E501
            raise ValueError("Invalid value for parameter `visible` when calling `api_users_get`, must conform to the pattern `/1|2|3/`")  # noqa: E501
        if 'order_by' in params and not re.match(r'id|username|alias|email', params['order_by']):  # noqa: E501
            raise ValueError("Invalid value for parameter `order_by` when calling `api_users_get`, must conform to the pattern `/id|username|alias|email/`")  # noqa: E501
        if 'order' in params and not re.match(r'ASC|DESC', params['order']):  # noqa: E501
            raise ValueError("Invalid value for parameter `order` when calling `api_users_get`, must conform to the pattern `/ASC|DESC/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'visible' in params:
            query_params.append(('visible', params['visible']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'term' in params:
            query_params.append(('term', params['term']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserCollection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_users_id_get(self, id, **kwargs):  # noqa: E501
        """Return one user entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: User ID to fetch (required)
        :return: UserEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_users_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_users_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_users_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Return one user entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: User ID to fetch (required)
        :return: UserEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_users_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_users_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_users_id_patch(self, body, id, **kwargs):  # noqa: E501
        """Update an existing user  # noqa: E501

        Update an existing user, you can pass all or just a subset of all attributes (passing roles will replace all existing ones)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_id_patch(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserEditForm body: (required)
        :param int id: User ID to update (required)
        :return: UserEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_users_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_users_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def api_users_id_patch_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update an existing user  # noqa: E501

        Update an existing user, you can pass all or just a subset of all attributes (passing roles will replace all existing ones)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_id_patch_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserEditForm body: (required)
        :param int id: User ID to update (required)
        :return: UserEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_users_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_users_id_patch`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_users_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_users_me_get(self, **kwargs):  # noqa: E501
        """Return the current user entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_me_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_users_me_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_users_me_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_users_me_get_with_http_info(self, **kwargs):  # noqa: E501
        """Return the current user entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_me_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_users_me_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/me', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_users_post(self, body, **kwargs):  # noqa: E501
        """Creates a new user  # noqa: E501

        Creates a new user and returns it afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCreateForm body: (required)
        :return: UserEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_users_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_users_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_users_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a new user  # noqa: E501

        Creates a new user and returns it afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_users_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCreateForm body: (required)
        :return: UserEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_users_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_users_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
