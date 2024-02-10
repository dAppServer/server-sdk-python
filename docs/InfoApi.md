# dappserver_server_sdk.InfoApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**welcome_page**](InfoApi.md#welcome_page) | **GET** / | 


# **welcome_page**
> welcome_page()



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:36911
# See configuration.py for a list of all supported configuration parameters.
configuration = dappserver_server_sdk.Configuration(
    host = "http://localhost:36911"
)


# Enter a context with an instance of the API client
with dappserver_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dappserver_server_sdk.InfoApi(api_client)

    try:
        api_instance.welcome_page()
    except Exception as e:
        print("Exception when calling InfoApi->welcome_page: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

