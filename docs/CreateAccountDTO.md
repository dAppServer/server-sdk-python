# CreateAccountDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from dappserver-server-sdk.models.create_account_dto import CreateAccountDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountDTO from a JSON string
create_account_dto_instance = CreateAccountDTO.from_json(json)
# print the JSON string representation of the object
print CreateAccountDTO.to_json()

# convert the object into a dict
create_account_dto_dict = create_account_dto_instance.to_dict()
# create an instance of CreateAccountDTO from a dict
create_account_dto_form_dict = create_account_dto.from_dict(create_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


