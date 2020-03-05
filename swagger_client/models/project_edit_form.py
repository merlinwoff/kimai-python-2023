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


class ProjectEditForm(object):
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
        'name': 'str',
        'comment': 'str',
        'order_number': 'str',
        'order_date': 'datetime',
        'start': 'datetime',
        'end': 'datetime',
        'customer': 'int',
        'color': 'str',
        'visible': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'comment': 'comment',
        'order_number': 'orderNumber',
        'order_date': 'orderDate',
        'start': 'start',
        'end': 'end',
        'customer': 'customer',
        'color': 'color',
        'visible': 'visible'
    }

    def __init__(self, name=None, comment=None, order_number=None, order_date=None, start=None, end=None, customer=None, color=None, visible=None):  # noqa: E501
        """ProjectEditForm - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._comment = None
        self._order_number = None
        self._order_date = None
        self._start = None
        self._end = None
        self._customer = None
        self._color = None
        self._visible = None
        self.discriminator = None

        self.name = name
        if comment is not None:
            self.comment = comment
        if order_number is not None:
            self.order_number = order_number
        if order_date is not None:
            self.order_date = order_date
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        self.customer = customer
        self.color = color
        if visible is not None:
            self.visible = visible

    @property
    def name(self):
        """Gets the name of this ProjectEditForm.  # noqa: E501


        :return: The name of this ProjectEditForm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectEditForm.


        :param name: The name of this ProjectEditForm.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this ProjectEditForm.  # noqa: E501


        :return: The comment of this ProjectEditForm.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ProjectEditForm.


        :param comment: The comment of this ProjectEditForm.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def order_number(self):
        """Gets the order_number of this ProjectEditForm.  # noqa: E501


        :return: The order_number of this ProjectEditForm.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this ProjectEditForm.


        :param order_number: The order_number of this ProjectEditForm.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def order_date(self):
        """Gets the order_date of this ProjectEditForm.  # noqa: E501


        :return: The order_date of this ProjectEditForm.  # noqa: E501
        :rtype: datetime
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this ProjectEditForm.


        :param order_date: The order_date of this ProjectEditForm.  # noqa: E501
        :type: datetime
        """

        self._order_date = order_date

    @property
    def start(self):
        """Gets the start of this ProjectEditForm.  # noqa: E501


        :return: The start of this ProjectEditForm.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ProjectEditForm.


        :param start: The start of this ProjectEditForm.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this ProjectEditForm.  # noqa: E501


        :return: The end of this ProjectEditForm.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ProjectEditForm.


        :param end: The end of this ProjectEditForm.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def customer(self):
        """Gets the customer of this ProjectEditForm.  # noqa: E501

        Customer ID  # noqa: E501

        :return: The customer of this ProjectEditForm.  # noqa: E501
        :rtype: int
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ProjectEditForm.

        Customer ID  # noqa: E501

        :param customer: The customer of this ProjectEditForm.  # noqa: E501
        :type: int
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def color(self):
        """Gets the color of this ProjectEditForm.  # noqa: E501


        :return: The color of this ProjectEditForm.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ProjectEditForm.


        :param color: The color of this ProjectEditForm.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def visible(self):
        """Gets the visible of this ProjectEditForm.  # noqa: E501


        :return: The visible of this ProjectEditForm.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ProjectEditForm.


        :param visible: The visible of this ProjectEditForm.  # noqa: E501
        :type: bool
        """

        self._visible = visible

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
        if issubclass(ProjectEditForm, dict):
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
        if not isinstance(other, ProjectEditForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other