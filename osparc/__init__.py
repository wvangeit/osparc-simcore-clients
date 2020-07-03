# coding: utf-8

# flake8: noqa

"""
    Public API Server

    **osparc-simcore Public RESTful API Specifications** ## Python Client - Github [repo](https://github.com/ITISFoundation/osparc-simcore-python-client) - Quick install: ``pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git``   # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.3.6"

# import apis into sdk package
from osparc.api.meta_api import MetaApi
from osparc.api.users_api import UsersApi

# import ApiClient
from osparc.api_client import ApiClient
from osparc.configuration import Configuration
from osparc.exceptions import OpenApiException
from osparc.exceptions import ApiTypeError
from osparc.exceptions import ApiValueError
from osparc.exceptions import ApiKeyError
from osparc.exceptions import ApiException
# import models into sdk package
from osparc.models.groups import Groups
from osparc.models.http_validation_error import HTTPValidationError
from osparc.models.meta import Meta
from osparc.models.profile import Profile
from osparc.models.profile_update import ProfileUpdate
from osparc.models.users_group import UsersGroup
from osparc.models.validation_error import ValidationError

