# coding: utf-8

"""
    Lethean Server

    Lethean dAppServer

    The version of the OpenAPI document: 3.1.1
    Contact: hello@lt.hn
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "dappserver_server_sdk"
VERSION = "3.1.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Lethean Server",
    author="Lethean",
    author_email="hello@lt.hn",
    url="https://github.com/dappserver/server-sdk-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Lethean Server"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="EUPL-1.2",
    long_description_content_type='text/markdown',
    long_description="""\
    Lethean dAppServer
    """,  # noqa: E501
    package_data={"dappserver_server_sdk": ["py.typed"]},
)
