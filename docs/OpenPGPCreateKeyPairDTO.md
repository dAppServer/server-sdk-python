# OpenPGPCreateKeyPairDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passphrase** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from dappserver_server_sdk.models.open_pgp_create_key_pair_dto import OpenPGPCreateKeyPairDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPGPCreateKeyPairDTO from a JSON string
open_pgp_create_key_pair_dto_instance = OpenPGPCreateKeyPairDTO.from_json(json)
# print the JSON string representation of the object
print OpenPGPCreateKeyPairDTO.to_json()

# convert the object into a dict
open_pgp_create_key_pair_dto_dict = open_pgp_create_key_pair_dto_instance.to_dict()
# create an instance of OpenPGPCreateKeyPairDTO from a dict
open_pgp_create_key_pair_dto_form_dict = open_pgp_create_key_pair_dto.from_dict(open_pgp_create_key_pair_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


