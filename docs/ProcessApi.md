# dappserver-server-sdk.ProcessApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_process**](ProcessApi.md#add_process) | **POST** /process/add | 
[**kill_process**](ProcessApi.md#kill_process) | **POST** /process/kill | 
[**run_process**](ProcessApi.md#run_process) | **POST** /process/run | 
[**start_process**](ProcessApi.md#start_process) | **POST** /process/start | 
[**stop_process**](ProcessApi.md#stop_process) | **POST** /process/stop | 


# **add_process**
> add_process(process_add_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.process_add_dto import ProcessAddDTO
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
    api_instance = dappserver-server-sdk.ProcessApi(api_client)
    process_add_dto = dappserver-server-sdk.ProcessAddDTO() # ProcessAddDTO | 

    try:
        api_instance.add_process(process_add_dto)
    except Exception as e:
        print("Exception when calling ProcessApi->add_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_add_dto** | [**ProcessAddDTO**](ProcessAddDTO.md)|  | 

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

# **kill_process**
> kill_process(process_kill_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.process_kill_dto import ProcessKillDTO
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
    api_instance = dappserver-server-sdk.ProcessApi(api_client)
    process_kill_dto = dappserver-server-sdk.ProcessKillDTO() # ProcessKillDTO | 

    try:
        api_instance.kill_process(process_kill_dto)
    except Exception as e:
        print("Exception when calling ProcessApi->kill_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_kill_dto** | [**ProcessKillDTO**](ProcessKillDTO.md)|  | 

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

# **run_process**
> run_process(process_run_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.process_run_dto import ProcessRunDTO
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
    api_instance = dappserver-server-sdk.ProcessApi(api_client)
    process_run_dto = dappserver-server-sdk.ProcessRunDTO() # ProcessRunDTO | 

    try:
        api_instance.run_process(process_run_dto)
    except Exception as e:
        print("Exception when calling ProcessApi->run_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_run_dto** | [**ProcessRunDTO**](ProcessRunDTO.md)|  | 

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

# **start_process**
> start_process(process_start_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.process_start_dto import ProcessStartDTO
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
    api_instance = dappserver-server-sdk.ProcessApi(api_client)
    process_start_dto = dappserver-server-sdk.ProcessStartDTO() # ProcessStartDTO | 

    try:
        api_instance.start_process(process_start_dto)
    except Exception as e:
        print("Exception when calling ProcessApi->start_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_start_dto** | [**ProcessStartDTO**](ProcessStartDTO.md)|  | 

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

# **stop_process**
> stop_process(process_stop_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.process_stop_dto import ProcessStopDTO
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
    api_instance = dappserver-server-sdk.ProcessApi(api_client)
    process_stop_dto = dappserver-server-sdk.ProcessStopDTO() # ProcessStopDTO | 

    try:
        api_instance.stop_process(process_stop_dto)
    except Exception as e:
        print("Exception when calling ProcessApi->stop_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_stop_dto** | [**ProcessStopDTO**](ProcessStopDTO.md)|  | 

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

