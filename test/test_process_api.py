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

from dappserver-server-sdk.api.process_api import ProcessApi


class TestProcessApi(unittest.TestCase):
    """ProcessApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProcessApi()

    def tearDown(self) -> None:
        pass

    def test_add_process(self) -> None:
        """Test case for add_process

        """
        pass

    def test_kill_process(self) -> None:
        """Test case for kill_process

        """
        pass

    def test_run_process(self) -> None:
        """Test case for run_process

        """
        pass

    def test_start_process(self) -> None:
        """Test case for start_process

        """
        pass

    def test_stop_process(self) -> None:
        """Test case for stop_process

        """
        pass


if __name__ == '__main__':
    unittest.main()