# coding: utf-8

"""
    Lethean Server

    Lethean dAppServer

    The version of the OpenAPI document: 3.1.1
    Contact: hello@lt.hn
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dappserver_server_sdk.models.config_object_remove_dto import ConfigObjectRemoveDTO

class TestConfigObjectRemoveDTO(unittest.TestCase):
    """ConfigObjectRemoveDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigObjectRemoveDTO:
        """Test ConfigObjectRemoveDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigObjectRemoveDTO`
        """
        model = ConfigObjectRemoveDTO()
        if include_optional:
            return ConfigObjectRemoveDTO(
                group = '',
                object = ''
            )
        else:
            return ConfigObjectRemoveDTO(
                group = '',
                object = '',
        )
        """

    def testConfigObjectRemoveDTO(self):
        """Test ConfigObjectRemoveDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
