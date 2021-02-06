# coding: utf-8

"""
    osparc.io web API

    osparc-simcore public web API specifications  # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from osparc.configuration import Configuration


class JobOutput(object):
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
        'name': 'str',
        'type': 'str',
        'title': 'str',
        'value': 'PortValue',
        'job_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'title': 'title',
        'value': 'value',
        'job_id': 'job_id'
    }

    def __init__(self, name=None, type=None, title=None, value=None, job_id=None, local_vars_configuration=None):  # noqa: E501
        """JobOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._title = None
        self._value = None
        self._job_id = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        self.value = value
        self.job_id = job_id

    @property
    def name(self):
        """Gets the name of this JobOutput.  # noqa: E501

        Name given to the input/output in solver specs (see solver metadata.yml)  # noqa: E501

        :return: The name of this JobOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobOutput.

        Name given to the input/output in solver specs (see solver metadata.yml)  # noqa: E501

        :param name: The name of this JobOutput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this JobOutput.  # noqa: E501

        Data type expected on this input/ouput  # noqa: E501

        :return: The type of this JobOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobOutput.

        Data type expected on this input/ouput  # noqa: E501

        :param type: The type of this JobOutput.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^(number|integer|boolean|string|data:([^\/\s,]+\/[^\/\s,]+|\[[^\/\s,]+\/[^\/\s,]+(,[^\/\s]+\/[^\/,\s]+)*\]))$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^(number|integer|boolean|string|data:([^\/\s,]+\/[^\/\s,]+|\[[^\/\s,]+\/[^\/\s,]+(,[^\/\s]+\/[^\/,\s]+)*\]))$/`")  # noqa: E501

        self._type = type

    @property
    def title(self):
        """Gets the title of this JobOutput.  # noqa: E501

        Short human readable name to identify input/output  # noqa: E501

        :return: The title of this JobOutput.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this JobOutput.

        Short human readable name to identify input/output  # noqa: E501

        :param title: The title of this JobOutput.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def value(self):
        """Gets the value of this JobOutput.  # noqa: E501


        :return: The value of this JobOutput.  # noqa: E501
        :rtype: PortValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JobOutput.


        :param value: The value of this JobOutput.  # noqa: E501
        :type: PortValue
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def job_id(self):
        """Gets the job_id of this JobOutput.  # noqa: E501

        Job that produced this output  # noqa: E501

        :return: The job_id of this JobOutput.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobOutput.

        Job that produced this output  # noqa: E501

        :param job_id: The job_id of this JobOutput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and job_id is None:  # noqa: E501
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

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
        if not isinstance(other, JobOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobOutput):
            return True

        return self.to_dict() != other.to_dict()
