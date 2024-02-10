# dappserver_server_sdk.CryptographyApi

All URIs are relative to *http://localhost:36911*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quasi_salt**](CryptographyApi.md#create_quasi_salt) | **POST** /crypto/hash/quasi-salted-hash | 
[**decrypt**](CryptographyApi.md#decrypt) | **POST** /crypto/openpgp/decrypt | 
[**encrypt**](CryptographyApi.md#encrypt) | **POST** /crypto/openpgp/encrypt | 
[**generate_key_pair**](CryptographyApi.md#generate_key_pair) | **POST** /crypto/openpgp/generate-key-pair | 
[**get_public_key**](CryptographyApi.md#get_public_key) | **POST** /crypto/openpgp/get-public-key | 
[**sha256**](CryptographyApi.md#sha256) | **POST** /crypto/hash/sha256 | 
[**sha384**](CryptographyApi.md#sha384) | **POST** /crypto/hash/sha384 | 
[**sha512**](CryptographyApi.md#sha512) | **POST** /crypto/hash/sha512 | 
[**sign**](CryptographyApi.md#sign) | **POST** /crypto/openpgp/sign | 
[**verify**](CryptographyApi.md#verify) | **POST** /crypto/openpgp/verify | 
[**verify_quasi_salt**](CryptographyApi.md#verify_quasi_salt) | **POST** /crypto/hash/quasi-salted-hash-verify | 


# **create_quasi_salt**
> create_quasi_salt(quasi_salt_hash_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.quasi_salt_hash_dto import QuasiSaltHashDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    quasi_salt_hash_dto = dappserver_server_sdk.QuasiSaltHashDTO() # QuasiSaltHashDTO | 

    try:
        api_instance.create_quasi_salt(quasi_salt_hash_dto)
    except Exception as e:
        print("Exception when calling CryptographyApi->create_quasi_salt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quasi_salt_hash_dto** | [**QuasiSaltHashDTO**](QuasiSaltHashDTO.md)|  | 

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

# **decrypt**
> decrypt(open_pgp_decrypt_byiddto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.open_pgp_decrypt_byiddto import OpenPGPDecryptBYIDDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    open_pgp_decrypt_byiddto = dappserver_server_sdk.OpenPGPDecryptBYIDDTO() # OpenPGPDecryptBYIDDTO | 

    try:
        api_instance.decrypt(open_pgp_decrypt_byiddto)
    except Exception as e:
        print("Exception when calling CryptographyApi->decrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_pgp_decrypt_byiddto** | [**OpenPGPDecryptBYIDDTO**](OpenPGPDecryptBYIDDTO.md)|  | 

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

# **encrypt**
> encrypt(open_pgp_encrypt_byiddto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.open_pgp_encrypt_byiddto import OpenPGPEncryptBYIDDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    open_pgp_encrypt_byiddto = dappserver_server_sdk.OpenPGPEncryptBYIDDTO() # OpenPGPEncryptBYIDDTO | 

    try:
        api_instance.encrypt(open_pgp_encrypt_byiddto)
    except Exception as e:
        print("Exception when calling CryptographyApi->encrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_pgp_encrypt_byiddto** | [**OpenPGPEncryptBYIDDTO**](OpenPGPEncryptBYIDDTO.md)|  | 

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

# **generate_key_pair**
> generate_key_pair(open_pgp_create_key_pair_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.open_pgp_create_key_pair_dto import OpenPGPCreateKeyPairDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    open_pgp_create_key_pair_dto = dappserver_server_sdk.OpenPGPCreateKeyPairDTO() # OpenPGPCreateKeyPairDTO | 

    try:
        api_instance.generate_key_pair(open_pgp_create_key_pair_dto)
    except Exception as e:
        print("Exception when calling CryptographyApi->generate_key_pair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_pgp_create_key_pair_dto** | [**OpenPGPCreateKeyPairDTO**](OpenPGPCreateKeyPairDTO.md)|  | 

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

# **get_public_key**
> get_public_key(open_pgp_get_public_key_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.open_pgp_get_public_key_dto import OpenPGPGetPublicKeyDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    open_pgp_get_public_key_dto = dappserver_server_sdk.OpenPGPGetPublicKeyDTO() # OpenPGPGetPublicKeyDTO | 

    try:
        api_instance.get_public_key(open_pgp_get_public_key_dto)
    except Exception as e:
        print("Exception when calling CryptographyApi->get_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_pgp_get_public_key_dto** | [**OpenPGPGetPublicKeyDTO**](OpenPGPGetPublicKeyDTO.md)|  | 

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

# **sha256**
> sha256(hash_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.hash_dto import HashDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    hash_dto = dappserver_server_sdk.HashDTO() # HashDTO | 

    try:
        api_instance.sha256(hash_dto)
    except Exception as e:
        print("Exception when calling CryptographyApi->sha256: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_dto** | [**HashDTO**](HashDTO.md)|  | 

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

# **sha384**
> sha384(hash_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.hash_dto import HashDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    hash_dto = dappserver_server_sdk.HashDTO() # HashDTO | 

    try:
        api_instance.sha384(hash_dto)
    except Exception as e:
        print("Exception when calling CryptographyApi->sha384: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_dto** | [**HashDTO**](HashDTO.md)|  | 

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

# **sha512**
> sha512(hash_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.hash_dto import HashDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    hash_dto = dappserver_server_sdk.HashDTO() # HashDTO | 

    try:
        api_instance.sha512(hash_dto)
    except Exception as e:
        print("Exception when calling CryptographyApi->sha512: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_dto** | [**HashDTO**](HashDTO.md)|  | 

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

# **sign**
> sign(open_pgp_sign_byiddto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.open_pgp_sign_byiddto import OpenPGPSignBYIDDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    open_pgp_sign_byiddto = dappserver_server_sdk.OpenPGPSignBYIDDTO() # OpenPGPSignBYIDDTO | 

    try:
        api_instance.sign(open_pgp_sign_byiddto)
    except Exception as e:
        print("Exception when calling CryptographyApi->sign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_pgp_sign_byiddto** | [**OpenPGPSignBYIDDTO**](OpenPGPSignBYIDDTO.md)|  | 

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

# **verify**
> verify(open_pgp_verify_byiddto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.open_pgp_verify_byiddto import OpenPGPVerifyBYIDDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    open_pgp_verify_byiddto = dappserver_server_sdk.OpenPGPVerifyBYIDDTO() # OpenPGPVerifyBYIDDTO | 

    try:
        api_instance.verify(open_pgp_verify_byiddto)
    except Exception as e:
        print("Exception when calling CryptographyApi->verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_pgp_verify_byiddto** | [**OpenPGPVerifyBYIDDTO**](OpenPGPVerifyBYIDDTO.md)|  | 

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

# **verify_quasi_salt**
> verify_quasi_salt(quasi_salt_hash_verify_dto)



### Example


```python
import dappserver_server_sdk
from dappserver_server_sdk.models.quasi_salt_hash_verify_dto import QuasiSaltHashVerifyDTO
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
    api_instance = dappserver_server_sdk.CryptographyApi(api_client)
    quasi_salt_hash_verify_dto = dappserver_server_sdk.QuasiSaltHashVerifyDTO() # QuasiSaltHashVerifyDTO | 

    try:
        api_instance.verify_quasi_salt(quasi_salt_hash_verify_dto)
    except Exception as e:
        print("Exception when calling CryptographyApi->verify_quasi_salt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quasi_salt_hash_verify_dto** | [**QuasiSaltHashVerifyDTO**](QuasiSaltHashVerifyDTO.md)|  | 

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

