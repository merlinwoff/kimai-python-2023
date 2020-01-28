# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen, but we try to avoid them.   # noqa: E501

    OpenAPI spec version: 0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Version(object):
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
        'version': 'str',
        'candidate': 'str',
        'semver': 'str',
        'name': 'str',
        'copyright': 'str'
    }

    attribute_map = {
        'version': 'version',
        'candidate': 'candidate',
        'semver': 'semver',
        'name': 'name',
        'copyright': 'copyright'
    }

    def __init__(self, version=None, candidate=None, semver=None, name=None, copyright=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._candidate = None
        self._semver = None
        self._name = None
        self._copyright = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if candidate is not None:
            self.candidate = candidate
        if semver is not None:
            self.semver = semver
        if name is not None:
            self.name = name
        if copyright is not None:
            self.copyright = copyright

    @property
    def version(self):
        """Gets the version of this Version.  # noqa: E501


        :return: The version of this Version.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Version.


        :param version: The version of this Version.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def candidate(self):
        """Gets the candidate of this Version.  # noqa: E501


        :return: The candidate of this Version.  # noqa: E501
        :rtype: str
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """Sets the candidate of this Version.


        :param candidate: The candidate of this Version.  # noqa: E501
        :type: str
        """

        self._candidate = candidate

    @property
    def semver(self):
        """Gets the semver of this Version.  # noqa: E501


        :return: The semver of this Version.  # noqa: E501
        :rtype: str
        """
        return self._semver

    @semver.setter
    def semver(self, semver):
        """Sets the semver of this Version.


        :param semver: The semver of this Version.  # noqa: E501
        :type: str
        """

        self._semver = semver

    @property
    def name(self):
        """Gets the name of this Version.  # noqa: E501


        :return: The name of this Version.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Version.


        :param name: The name of this Version.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def copyright(self):
        """Gets the copyright of this Version.  # noqa: E501


        :return: The copyright of this Version.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this Version.


        :param copyright: The copyright of this Version.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Version, dict):
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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other