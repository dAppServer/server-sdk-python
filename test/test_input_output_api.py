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

from dappserver_server_sdk.api.input_output_api import InputOutputApi


class TestInputOutputApi(unittest.TestCase):
    """InputOutputApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InputOutputApi()

    def tearDown(self) -> None:
        pass

    def test_fetch_file(self) -> None:
        """Test case for fetch_file

        """
        pass

    def test_get_detailed_directory_list(self) -> None:
        """Test case for get_detailed_directory_list

        """
        pass

    def test_get_directory_list(self) -> None:
        """Test case for get_directory_list

        """
        pass

    def test_is_dir(self) -> None:
        """Test case for is_dir

        """
        pass

    def test_is_file(self) -> None:
        """Test case for is_file

        """
        pass

    def test_read_file(self) -> None:
        """Test case for read_file

        """
        pass

    def test_write_file(self) -> None:
        """Test case for write_file

        """
        pass


if __name__ == '__main__':
    unittest.main()
