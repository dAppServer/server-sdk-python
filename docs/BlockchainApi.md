# dappserver-server-sdk.BlockchainApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_daemon**](BlockchainApi.md#download_daemon) | **POST** /blockchain/lethean/daemon/downloadDaemon | 
[**export_blockchain**](BlockchainApi.md#export_blockchain) | **POST** /blockchain/lethean/daemon/export | 
[**import_blockchain**](BlockchainApi.md#import_blockchain) | **POST** /blockchain/lethean/daemon/import | 
[**json_rpc**](BlockchainApi.md#json_rpc) | **POST** /blockchain/lethean/daemon/json_rpc | 
[**start_daemon**](BlockchainApi.md#start_daemon) | **POST** /blockchain/lethean/daemon/start | 
[**start_wallet**](BlockchainApi.md#start_wallet) | **POST** /blockchain/lethean/wallet/start | 
[**wallet_json_rpc**](BlockchainApi.md#wallet_json_rpc) | **POST** /blockchain/lethean/wallet/json_rpc | 


# **download_daemon**
> download_daemon(body)



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
    api_instance = dappserver-server-sdk.BlockchainApi(api_client)
    body = None # object | 

    try:
        api_instance.download_daemon(body)
    except Exception as e:
        print("Exception when calling BlockchainApi->download_daemon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_blockchain**
> export_blockchain(body)



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
    api_instance = dappserver-server-sdk.BlockchainApi(api_client)
    body = None # object | 

    try:
        api_instance.export_blockchain(body)
    except Exception as e:
        print("Exception when calling BlockchainApi->export_blockchain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_blockchain**
> import_blockchain(body)



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
    api_instance = dappserver-server-sdk.BlockchainApi(api_client)
    body = None # object | 

    try:
        api_instance.import_blockchain(body)
    except Exception as e:
        print("Exception when calling BlockchainApi->import_blockchain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **json_rpc**
> str json_rpc(blockchain_lethean_rpcdto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.blockchain_lethean_rpcdto import BlockchainLetheanRPCDTO
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
    api_instance = dappserver-server-sdk.BlockchainApi(api_client)
    blockchain_lethean_rpcdto = dappserver-server-sdk.BlockchainLetheanRPCDTO() # BlockchainLetheanRPCDTO | 

    try:
        api_response = api_instance.json_rpc(blockchain_lethean_rpcdto)
        print("The response of BlockchainApi->json_rpc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->json_rpc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_lethean_rpcdto** | [**BlockchainLetheanRPCDTO**](BlockchainLetheanRPCDTO.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_daemon**
> ServerResponse start_daemon(blockchain_lethean_daemon_start_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.blockchain_lethean_daemon_start_dto import BlockchainLetheanDaemonStartDTO
from dappserver-server-sdk.models.server_response import ServerResponse
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
    api_instance = dappserver-server-sdk.BlockchainApi(api_client)
    blockchain_lethean_daemon_start_dto = dappserver-server-sdk.BlockchainLetheanDaemonStartDTO() # BlockchainLetheanDaemonStartDTO | 

    try:
        api_response = api_instance.start_daemon(blockchain_lethean_daemon_start_dto)
        print("The response of BlockchainApi->start_daemon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->start_daemon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_lethean_daemon_start_dto** | [**BlockchainLetheanDaemonStartDTO**](BlockchainLetheanDaemonStartDTO.md)|  | 

### Return type

[**ServerResponse**](ServerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_wallet**
> start_wallet(blockchain_lethean_wallet_start_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.blockchain_lethean_wallet_start_dto import BlockchainLetheanWalletStartDTO
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
    api_instance = dappserver-server-sdk.BlockchainApi(api_client)
    blockchain_lethean_wallet_start_dto = dappserver-server-sdk.BlockchainLetheanWalletStartDTO() # BlockchainLetheanWalletStartDTO | 

    try:
        api_instance.start_wallet(blockchain_lethean_wallet_start_dto)
    except Exception as e:
        print("Exception when calling BlockchainApi->start_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_lethean_wallet_start_dto** | [**BlockchainLetheanWalletStartDTO**](BlockchainLetheanWalletStartDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_json_rpc**
> str wallet_json_rpc(body)



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
    api_instance = dappserver-server-sdk.BlockchainApi(api_client)
    body = None # object | 

    try:
        api_response = api_instance.wallet_json_rpc(body)
        print("The response of BlockchainApi->wallet_json_rpc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->wallet_json_rpc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

