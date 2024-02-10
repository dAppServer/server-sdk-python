# DeleteAccountDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from dappserver-server-sdk.models.delete_account_dto import DeleteAccountDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAccountDTO from a JSON string
delete_account_dto_instance = DeleteAccountDTO.from_json(json)
# print the JSON string representation of the object
print DeleteAccountDTO.to_json()

# convert the object into a dict
delete_account_dto_dict = delete_account_dto_instance.to_dict()
# create an instance of DeleteAccountDTO from a dict
delete_account_dto_form_dict = delete_account_dto.from_dict(delete_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


