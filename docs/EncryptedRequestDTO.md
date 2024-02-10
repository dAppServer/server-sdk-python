# EncryptedRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | 
**signature** | **str** |  | [optional] 

## Example

```python
from dappserver-server-sdk.models.encrypted_request_dto import EncryptedRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptedRequestDTO from a JSON string
encrypted_request_dto_instance = EncryptedRequestDTO.from_json(json)
# print the JSON string representation of the object
print EncryptedRequestDTO.to_json()

# convert the object into a dict
encrypted_request_dto_dict = encrypted_request_dto_instance.to_dict()
# create an instance of EncryptedRequestDTO from a dict
encrypted_request_dto_form_dict = encrypted_request_dto.from_dict(encrypted_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


