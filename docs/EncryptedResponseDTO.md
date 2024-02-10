# EncryptedResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | 
**signature** | **str** |  | [optional] 

## Example

```python
from dappserver_server_sdk.models.encrypted_response_dto import EncryptedResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptedResponseDTO from a JSON string
encrypted_response_dto_instance = EncryptedResponseDTO.from_json(json)
# print the JSON string representation of the object
print EncryptedResponseDTO.to_json()

# convert the object into a dict
encrypted_response_dto_dict = encrypted_response_dto_instance.to_dict()
# create an instance of EncryptedResponseDTO from a dict
encrypted_response_dto_form_dict = encrypted_response_dto.from_dict(encrypted_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


