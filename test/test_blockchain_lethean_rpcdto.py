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

from dappserver_server_sdk.models.blockchain_lethean_rpcdto import BlockchainLetheanRPCDTO

class TestBlockchainLetheanRPCDTO(unittest.TestCase):
    """BlockchainLetheanRPCDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlockchainLetheanRPCDTO:
        """Test BlockchainLetheanRPCDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockchainLetheanRPCDTO`
        """
        model = BlockchainLetheanRPCDTO()
        if include_optional:
            return BlockchainLetheanRPCDTO(
                url = '',
                req = ''
            )
        else:
            return BlockchainLetheanRPCDTO(
                url = '',
                req = '',
        )
        """

    def testBlockchainLetheanRPCDTO(self):
        """Test BlockchainLetheanRPCDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
