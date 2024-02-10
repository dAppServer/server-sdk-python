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

from dappserver-server-sdk.models.blockchain_lethean_wallet_start_dto import BlockchainLetheanWalletStartDTO

class TestBlockchainLetheanWalletStartDTO(unittest.TestCase):
    """BlockchainLetheanWalletStartDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlockchainLetheanWalletStartDTO:
        """Test BlockchainLetheanWalletStartDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockchainLetheanWalletStartDTO`
        """
        model = BlockchainLetheanWalletStartDTO()
        if include_optional:
            return BlockchainLetheanWalletStartDTO(
                wallet_dir = '',
                rpc_bind_port = 1.337,
                disable_rpc_login = True
            )
        else:
            return BlockchainLetheanWalletStartDTO(
                wallet_dir = '',
                rpc_bind_port = 1.337,
                disable_rpc_login = True,
        )
        """

    def testBlockchainLetheanWalletStartDTO(self):
        """Test BlockchainLetheanWalletStartDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
