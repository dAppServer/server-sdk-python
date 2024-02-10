# OpenPGPEncryptBYIDDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**message** | **str** |  | 
**passphrase** | **str** |  | [optional] 

## Example

```python
from dappserver-server-sdk.models.open_pgp_encrypt_byiddto import OpenPGPEncryptBYIDDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPGPEncryptBYIDDTO from a JSON string
open_pgp_encrypt_byiddto_instance = OpenPGPEncryptBYIDDTO.from_json(json)
# print the JSON string representation of the object
print OpenPGPEncryptBYIDDTO.to_json()

# convert the object into a dict
open_pgp_encrypt_byiddto_dict = open_pgp_encrypt_byiddto_instance.to_dict()
# create an instance of OpenPGPEncryptBYIDDTO from a dict
open_pgp_encrypt_byiddto_form_dict = open_pgp_encrypt_byiddto.from_dict(open_pgp_encrypt_byiddto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


