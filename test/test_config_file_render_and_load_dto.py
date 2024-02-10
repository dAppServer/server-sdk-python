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

from dappserver_server_sdk.models.config_file_render_and_load_dto import ConfigFileRenderAndLoadDTO

class TestConfigFileRenderAndLoadDTO(unittest.TestCase):
    """ConfigFileRenderAndLoadDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigFileRenderAndLoadDTO:
        """Test ConfigFileRenderAndLoadDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigFileRenderAndLoadDTO`
        """
        model = ConfigFileRenderAndLoadDTO()
        if include_optional:
            return ConfigFileRenderAndLoadDTO(
                file = '',
                model = dappserver_server_sdk.models.config_object_get_dto.ConfigObjectGetDTO(
                    group = '', 
                    object = '', )
            )
        else:
            return ConfigFileRenderAndLoadDTO(
                file = '',
                model = dappserver_server_sdk.models.config_object_get_dto.ConfigObjectGetDTO(
                    group = '', 
                    object = '', ),
        )
        """

    def testConfigFileRenderAndLoadDTO(self):
        """Test ConfigFileRenderAndLoadDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
