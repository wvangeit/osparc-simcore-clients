# coding: utf-8

"""
    osparc public web api

    
    The version of the OpenAPI document: 0.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import osparc
from osparc.models.task_states import TaskStates  # noqa: E501
from osparc.rest import ApiException

class TestTaskStates(unittest.TestCase):
    """TaskStates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskStates
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = osparc.models.task_states.TaskStates()  # noqa: E501
        if include_optional :
            return TaskStates(
            )
        else :
            return TaskStates(
        )

    def testTaskStates(self):
        """Test TaskStates"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
