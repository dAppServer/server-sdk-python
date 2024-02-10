# OpenPGPDecryptBYIDDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**message** | **str** |  | 
**passphrase** | **str** |  | 
**signed_by** | **str** |  | [optional] 

## Example

```python
from dappserver-server-sdk.models.open_pgp_decrypt_byiddto import OpenPGPDecryptBYIDDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPGPDecryptBYIDDTO from a JSON string
open_pgp_decrypt_byiddto_instance = OpenPGPDecryptBYIDDTO.from_json(json)
# print the JSON string representation of the object
print OpenPGPDecryptBYIDDTO.to_json()

# convert the object into a dict
open_pgp_decrypt_byiddto_dict = open_pgp_decrypt_byiddto_instance.to_dict()
# create an instance of OpenPGPDecryptBYIDDTO from a dict
open_pgp_decrypt_byiddto_form_dict = open_pgp_decrypt_byiddto.from_dict(open_pgp_decrypt_byiddto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


