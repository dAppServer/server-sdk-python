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

from dappserver_server_sdk.models.open_pgp_get_public_key_dto import OpenPGPGetPublicKeyDTO

class TestOpenPGPGetPublicKeyDTO(unittest.TestCase):
    """OpenPGPGetPublicKeyDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenPGPGetPublicKeyDTO:
        """Test OpenPGPGetPublicKeyDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenPGPGetPublicKeyDTO`
        """
        model = OpenPGPGetPublicKeyDTO()
        if include_optional:
            return OpenPGPGetPublicKeyDTO(
                id = ''
            )
        else:
            return OpenPGPGetPublicKeyDTO(
                id = '',
        )
        """

    def testOpenPGPGetPublicKeyDTO(self):
        """Test OpenPGPGetPublicKeyDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
