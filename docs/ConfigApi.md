# dappserver_server_sdk.ConfigApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_config**](ConfigApi.md#clear_config) | **POST** /config/object/clear | 
[**count_config**](ConfigApi.md#count_config) | **POST** /config/object/count | 
[**get_config**](ConfigApi.md#get_config) | **POST** /config/object/get | 
[**load**](ConfigApi.md#load) | **POST** /config/file/load | 
[**parse**](ConfigApi.md#parse) | **POST** /config/ini/parseJSON | 
[**remove_config**](ConfigApi.md#remove_config) | **POST** /config/object/remove | 
[**render**](ConfigApi.md#render) | **POST** /config/file/render | 
[**render_and_load**](ConfigApi.md#render_and_load) | **POST** /config/file/renderAndLoad | 
[**render_string**](ConfigApi.md#render_string) | **POST** /config/file/renderString | 
[**set_config**](ConfigApi.md#set_config) | **POST** /config/object/set | 


# **clear_config**
> clear_config(config_object_clear_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_object_clear_dto import ConfigObjectClearDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_object_clear_dto = dappserver_server_sdk.ConfigObjectClearDTO() # ConfigObjectClearDTO | 

    try:
        api_instance.clear_config(config_object_clear_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->clear_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_object_clear_dto** | [**ConfigObjectClearDTO**](ConfigObjectClearDTO.md)|  | 

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

# **count_config**
> count_config(config_object_count_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_object_count_dto import ConfigObjectCountDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_object_count_dto = dappserver_server_sdk.ConfigObjectCountDTO() # ConfigObjectCountDTO | 

    try:
        api_instance.count_config(config_object_count_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->count_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_object_count_dto** | [**ConfigObjectCountDTO**](ConfigObjectCountDTO.md)|  | 

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

# **get_config**
> get_config(config_object_get_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_object_get_dto import ConfigObjectGetDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_object_get_dto = dappserver_server_sdk.ConfigObjectGetDTO() # ConfigObjectGetDTO | 

    try:
        api_instance.get_config(config_object_get_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_object_get_dto** | [**ConfigObjectGetDTO**](ConfigObjectGetDTO.md)|  | 

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

# **load**
> load(config_file_load_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_file_load_dto import ConfigFileLoadDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_file_load_dto = dappserver_server_sdk.ConfigFileLoadDTO() # ConfigFileLoadDTO | 

    try:
        api_instance.load(config_file_load_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_file_load_dto** | [**ConfigFileLoadDTO**](ConfigFileLoadDTO.md)|  | 

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

# **parse**
> parse(ini_object_parse_jsondto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.ini_object_parse_jsondto import INIObjectParseJSONDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    ini_object_parse_jsondto = dappserver_server_sdk.INIObjectParseJSONDTO() # INIObjectParseJSONDTO | 

    try:
        api_instance.parse(ini_object_parse_jsondto)
    except Exception as e:
        print("Exception when calling ConfigApi->parse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ini_object_parse_jsondto** | [**INIObjectParseJSONDTO**](INIObjectParseJSONDTO.md)|  | 

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

# **remove_config**
> remove_config(config_object_remove_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_object_remove_dto import ConfigObjectRemoveDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_object_remove_dto = dappserver_server_sdk.ConfigObjectRemoveDTO() # ConfigObjectRemoveDTO | 

    try:
        api_instance.remove_config(config_object_remove_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->remove_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_object_remove_dto** | [**ConfigObjectRemoveDTO**](ConfigObjectRemoveDTO.md)|  | 

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

# **render**
> render(config_file_render_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_file_render_dto import ConfigFileRenderDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_file_render_dto = dappserver_server_sdk.ConfigFileRenderDTO() # ConfigFileRenderDTO | 

    try:
        api_instance.render(config_file_render_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->render: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_file_render_dto** | [**ConfigFileRenderDTO**](ConfigFileRenderDTO.md)|  | 

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

# **render_and_load**
> render_and_load(config_file_render_and_load_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_file_render_and_load_dto import ConfigFileRenderAndLoadDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_file_render_and_load_dto = dappserver_server_sdk.ConfigFileRenderAndLoadDTO() # ConfigFileRenderAndLoadDTO | 

    try:
        api_instance.render_and_load(config_file_render_and_load_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->render_and_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_file_render_and_load_dto** | [**ConfigFileRenderAndLoadDTO**](ConfigFileRenderAndLoadDTO.md)|  | 

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

# **render_string**
> render_string(config_file_render_string_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_file_render_string_dto import ConfigFileRenderStringDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_file_render_string_dto = dappserver_server_sdk.ConfigFileRenderStringDTO() # ConfigFileRenderStringDTO | 

    try:
        api_instance.render_string(config_file_render_string_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->render_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_file_render_string_dto** | [**ConfigFileRenderStringDTO**](ConfigFileRenderStringDTO.md)|  | 

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

# **set_config**
> set_config(config_object_set_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.config_object_set_dto import ConfigObjectSetDTO
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
    api_instance = dappserver_server_sdk.ConfigApi(api_client)
    config_object_set_dto = dappserver_server_sdk.ConfigObjectSetDTO() # ConfigObjectSetDTO | 

    try:
        api_instance.set_config(config_object_set_dto)
    except Exception as e:
        print("Exception when calling ConfigApi->set_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_object_set_dto** | [**ConfigObjectSetDTO**](ConfigObjectSetDTO.md)|  | 

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

