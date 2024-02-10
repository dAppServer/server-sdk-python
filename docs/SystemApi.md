# dappserver-server-sdk.SystemApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_server**](SystemApi.md#check_server) | **GET** /system/check | 
[**get_server_certificate**](SystemApi.md#get_server_certificate) | **GET** /system/cert | 


# **check_server**
> check_server()



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:36911
# See configuration.py for a list of all supported configuration parameters.
configuration = dappserver-server-sdk.Configuration(
    host = "http://localhost:36911"
)


# Enter a context with an instance of the API client
with dappserver-server-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dappserver-server-sdk.SystemApi(api_client)

    try:
        api_instance.check_server()
    except Exception as e:
        print("Exception when calling SystemApi->check_server: %s\n" % e)
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

# **get_server_certificate**
> get_server_certificate()



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:36911
# See configuration.py for a list of all supported configuration parameters.
configuration = dappserver-server-sdk.Configuration(
    host = "http://localhost:36911"
)


# Enter a context with an instance of the API client
with dappserver-server-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dappserver-server-sdk.SystemApi(api_client)

    try:
        api_instance.get_server_certificate()
    except Exception as e:
        print("Exception when calling SystemApi->get_server_certificate: %s\n" % e)
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

