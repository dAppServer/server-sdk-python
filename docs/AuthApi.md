# dappserver-server-sdk.AuthApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AuthApi.md#create) | **POST** /auth/lethean/create | 
[**delete**](AuthApi.md#delete) | **POST** /auth/lethean/delete | 
[**login**](AuthApi.md#login) | **POST** /auth/lethean/login | 


# **create**
> CreateAccountResponseDTO create(create_account_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.create_account_dto import CreateAccountDTO
from dappserver-server-sdk.models.create_account_response_dto import CreateAccountResponseDTO
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
    api_instance = dappserver-server-sdk.AuthApi(api_client)
    create_account_dto = dappserver-server-sdk.CreateAccountDTO() # CreateAccountDTO | 

    try:
        api_response = api_instance.create(create_account_dto)
        print("The response of AuthApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_account_dto** | [**CreateAccountDTO**](CreateAccountDTO.md)|  | 

### Return type

[**CreateAccountResponseDTO**](CreateAccountResponseDTO.md)

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

# **delete**
> delete(delete_account_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.delete_account_dto import DeleteAccountDTO
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
    api_instance = dappserver-server-sdk.AuthApi(api_client)
    delete_account_dto = dappserver-server-sdk.DeleteAccountDTO() # DeleteAccountDTO | 

    try:
        api_instance.delete(delete_account_dto)
    except Exception as e:
        print("Exception when calling AuthApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_account_dto** | [**DeleteAccountDTO**](DeleteAccountDTO.md)|  | 

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

# **login**
> EncryptedResponseDTO login(encrypted_request_dto)



### Example


```python
import dappserver-server-sdk
from dappserver-server-sdk.models.encrypted_request_dto import EncryptedRequestDTO
from dappserver-server-sdk.models.encrypted_response_dto import EncryptedResponseDTO
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
    api_instance = dappserver-server-sdk.AuthApi(api_client)
    encrypted_request_dto = dappserver-server-sdk.EncryptedRequestDTO() # EncryptedRequestDTO | 

    try:
        api_response = api_instance.login(encrypted_request_dto)
        print("The response of AuthApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypted_request_dto** | [**EncryptedRequestDTO**](EncryptedRequestDTO.md)|  | 

### Return type

[**EncryptedResponseDTO**](EncryptedResponseDTO.md)

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

