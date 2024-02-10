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

from dappserver_server_sdk.models.open_pgp_sign_byiddto import OpenPGPSignBYIDDTO

class TestOpenPGPSignBYIDDTO(unittest.TestCase):
    """OpenPGPSignBYIDDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenPGPSignBYIDDTO:
        """Test OpenPGPSignBYIDDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenPGPSignBYIDDTO`
        """
        model = OpenPGPSignBYIDDTO()
        if include_optional:
            return OpenPGPSignBYIDDTO(
                id = '',
                message = '',
                passphrase = ''
            )
        else:
            return OpenPGPSignBYIDDTO(
                id = '',
                message = '',
                passphrase = '',
        )
        """

    def testOpenPGPSignBYIDDTO(self):
        """Test OpenPGPSignBYIDDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
