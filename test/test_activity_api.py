# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen.   # noqa: E501

    OpenAPI spec version: 0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.activity_api import ActivityApi  # noqa: E501
from swagger_client.rest import ApiException


class TestActivityApi(unittest.TestCase):
    """ActivityApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.activity_api.ActivityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_activities_get(self):
        """Test case for api_activities_get

        Returns a collection of activities  # noqa: E501
        """
        pass

    def test_api_activities_id_get(self):
        """Test case for api_activities_id_get

        Returns one activity  # noqa: E501
        """
        pass

    def test_api_activities_id_meta_patch(self):
        """Test case for api_activities_id_meta_patch

        Sets the value of a meta-field for an existing activity  # noqa: E501
        """
        pass

    def test_api_activities_id_patch(self):
        """Test case for api_activities_id_patch

        Update an existing activity  # noqa: E501
        """
        pass

    def test_api_activities_id_rates_get(self):
        """Test case for api_activities_id_rates_get

        Returns a collection of all rates for one activity  # noqa: E501
        """
        pass

    def test_api_activities_id_rates_post(self):
        """Test case for api_activities_id_rates_post

        Adds a new rate to an activity  # noqa: E501
        """
        pass

    def test_api_activities_id_rates_rate_id_delete(self):
        """Test case for api_activities_id_rates_rate_id_delete

        Deletes one rate for an activity  # noqa: E501
        """
        pass

    def test_api_activities_post(self):
        """Test case for api_activities_post

        Creates a new activity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()