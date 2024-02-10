# dappserver-server-sdk.InputOutputApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_file**](InputOutputApi.md#fetch_file) | **POST** /io/download/fetch | 
[**get_detailed_directory_list**](InputOutputApi.md#get_detailed_directory_list) | **POST** /io/filesystem/list-detailed | 
[**get_directory_list**](InputOutputApi.md#get_directory_list) | **POST** /io/filesystem/list | 
[**is_dir**](InputOutputApi.md#is_dir) | **POST** /io/filesystem/is-dir | 
[**is_file**](InputOutputApi.md#is_file) | **POST** /io/filesystem/is-file | 
[**read_file**](InputOutputApi.md#read_file) | **POST** /io/filesystem/read | 
[**write_file**](InputOutputApi.md#write_file) | **POST** /io/filesystem/write | 


# **fetch_file**
> fetch_file(file_download_request)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.file_download_request import FileDownloadRequest
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
    api_instance = dappserver-server-sdk.InputOutputApi(api_client)
    file_download_request = dappserver-server-sdk.FileDownloadRequest() # FileDownloadRequest | 

    try:
        api_instance.fetch_file(file_download_request)
    except Exception as e:
        print("Exception when calling InputOutputApi->fetch_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_download_request** | [**FileDownloadRequest**](FileDownloadRequest.md)|  | 

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

# **get_detailed_directory_list**
> get_detailed_directory_list(file_path_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.file_path_dto import FilePathDTO
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
    api_instance = dappserver-server-sdk.InputOutputApi(api_client)
    file_path_dto = dappserver-server-sdk.FilePathDTO() # FilePathDTO | 

    try:
        api_instance.get_detailed_directory_list(file_path_dto)
    except Exception as e:
        print("Exception when calling InputOutputApi->get_detailed_directory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path_dto** | [**FilePathDTO**](FilePathDTO.md)|  | 

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

# **get_directory_list**
> get_directory_list(file_path_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.file_path_dto import FilePathDTO
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
    api_instance = dappserver-server-sdk.InputOutputApi(api_client)
    file_path_dto = dappserver-server-sdk.FilePathDTO() # FilePathDTO | 

    try:
        api_instance.get_directory_list(file_path_dto)
    except Exception as e:
        print("Exception when calling InputOutputApi->get_directory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path_dto** | [**FilePathDTO**](FilePathDTO.md)|  | 

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

# **is_dir**
> FilePathCheckDTO is_dir(file_path_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.file_path_check_dto import FilePathCheckDTO
from dappserver-server-sdk.models.file_path_dto import FilePathDTO
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
    api_instance = dappserver-server-sdk.InputOutputApi(api_client)
    file_path_dto = dappserver-server-sdk.FilePathDTO() # FilePathDTO | 

    try:
        api_response = api_instance.is_dir(file_path_dto)
        print("The response of InputOutputApi->is_dir:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InputOutputApi->is_dir: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path_dto** | [**FilePathDTO**](FilePathDTO.md)|  | 

### Return type

[**FilePathCheckDTO**](FilePathCheckDTO.md)

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

# **is_file**
> FilePathCheckDTO is_file(file_path_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.file_path_check_dto import FilePathCheckDTO
from dappserver-server-sdk.models.file_path_dto import FilePathDTO
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
    api_instance = dappserver-server-sdk.InputOutputApi(api_client)
    file_path_dto = dappserver-server-sdk.FilePathDTO() # FilePathDTO | 

    try:
        api_response = api_instance.is_file(file_path_dto)
        print("The response of InputOutputApi->is_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InputOutputApi->is_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path_dto** | [**FilePathDTO**](FilePathDTO.md)|  | 

### Return type

[**FilePathCheckDTO**](FilePathCheckDTO.md)

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

# **read_file**
> read_file(file_path_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.file_path_dto import FilePathDTO
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
    api_instance = dappserver-server-sdk.InputOutputApi(api_client)
    file_path_dto = dappserver-server-sdk.FilePathDTO() # FilePathDTO | 

    try:
        api_instance.read_file(file_path_dto)
    except Exception as e:
        print("Exception when calling InputOutputApi->read_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path_dto** | [**FilePathDTO**](FilePathDTO.md)|  | 

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

# **write_file**
> write_file(create_file_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.create_file_dto import CreateFileDTO
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
    api_instance = dappserver-server-sdk.InputOutputApi(api_client)
    create_file_dto = dappserver-server-sdk.CreateFileDTO() # CreateFileDTO | 

    try:
        api_instance.write_file(create_file_dto)
    except Exception as e:
        print("Exception when calling InputOutputApi->write_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_file_dto** | [**CreateFileDTO**](CreateFileDTO.md)|  | 

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

