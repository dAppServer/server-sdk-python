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

from dappserver-server-sdk.models.config_file_render_dto import ConfigFileRenderDTO

class TestConfigFileRenderDTO(unittest.TestCase):
    """ConfigFileRenderDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigFileRenderDTO:
        """Test ConfigFileRenderDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigFileRenderDTO`
        """
        model = ConfigFileRenderDTO()
        if include_optional:
            return ConfigFileRenderDTO(
                file = '',
                model = None
            )
        else:
            return ConfigFileRenderDTO(
                file = '',
                model = None,
        )
        """

    def testConfigFileRenderDTO(self):
        """Test ConfigFileRenderDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
