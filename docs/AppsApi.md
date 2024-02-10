# dappserver_server_sdk.AppsApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_market_place_apps**](AppsApi.md#get_market_place_apps) | **GET** /apps/marketplace | 
[**install_app**](AppsApi.md#install_app) | **POST** /apps/install | 
[**list_apps**](AppsApi.md#list_apps) | **GET** /apps/installed | 
[**remove_app**](AppsApi.md#remove_app) | **POST** /apps/remove | 


# **get_market_place_apps**
> str get_market_place_apps()



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
    api_instance = dappserver_server_sdk.AppsApi(api_client)

    try:
        api_response = api_instance.get_market_place_apps()
        print("The response of AppsApi->get_market_place_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_market_place_apps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_app**
> ServerResponse install_app()



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.server_response import ServerResponse
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
    api_instance = dappserver_server_sdk.AppsApi(api_client)

    try:
        api_response = api_instance.install_app()
        print("The response of AppsApi->install_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->install_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerResponse**](ServerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> str list_apps()



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
    api_instance = dappserver_server_sdk.AppsApi(api_client)

    try:
        api_response = api_instance.list_apps()
        print("The response of AppsApi->list_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->list_apps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_app**
> object remove_app()



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
    api_instance = dappserver_server_sdk.AppsApi(api_client)

    try:
        api_response = api_instance.remove_app()
        print("The response of AppsApi->remove_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->remove_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

