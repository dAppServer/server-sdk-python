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

from dappserver-server-sdk.models.file_path_check_dto import FilePathCheckDTO

class TestFilePathCheckDTO(unittest.TestCase):
    """FilePathCheckDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FilePathCheckDTO:
        """Test FilePathCheckDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FilePathCheckDTO`
        """
        model = FilePathCheckDTO()
        if include_optional:
            return FilePathCheckDTO(
                path = '',
                result = True
            )
        else:
            return FilePathCheckDTO(
                path = '',
                result = True,
        )
        """

    def testFilePathCheckDTO(self):
        """Test FilePathCheckDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
