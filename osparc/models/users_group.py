# coding: utf-8

"""
    osparc public web api

    
    The version of the OpenAPI document: 0.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from osparc.configuration import Configuration


class UsersGroup(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'gid': 'str',
        'label': 'str',
        'description': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'label': 'label',
        'description': 'description'
    }

    def __init__(self, gid=None, label=None, description=None, local_vars_configuration=None):  # noqa: E501
        """UsersGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gid = None
        self._label = None
        self._description = None
        self.discriminator = None

        self.gid = gid
        self.label = label
        if description is not None:
            self.description = description

    @property
    def gid(self):
        """Gets the gid of this UsersGroup.  # noqa: E501


        :return: The gid of this UsersGroup.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this UsersGroup.


        :param gid: The gid of this UsersGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and gid is None:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must not be `None`")  # noqa: E501

        self._gid = gid

    @property
    def label(self):
        """Gets the label of this UsersGroup.  # noqa: E501


        :return: The label of this UsersGroup.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this UsersGroup.


        :param label: The label of this UsersGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def description(self):
        """Gets the description of this UsersGroup.  # noqa: E501


        :return: The description of this UsersGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UsersGroup.


        :param description: The description of this UsersGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UsersGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersGroup):
            return True

        return self.to_dict() != other.to_dict()
