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

from dappserver-server-sdk.models.open_pgp_verify_byiddto import OpenPGPVerifyBYIDDTO

class TestOpenPGPVerifyBYIDDTO(unittest.TestCase):
    """OpenPGPVerifyBYIDDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenPGPVerifyBYIDDTO:
        """Test OpenPGPVerifyBYIDDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenPGPVerifyBYIDDTO`
        """
        model = OpenPGPVerifyBYIDDTO()
        if include_optional:
            return OpenPGPVerifyBYIDDTO(
                id = '',
                message = ''
            )
        else:
            return OpenPGPVerifyBYIDDTO(
                id = '',
                message = '',
        )
        """

    def testOpenPGPVerifyBYIDDTO(self):
        """Test OpenPGPVerifyBYIDDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
