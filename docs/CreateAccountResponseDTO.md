# CreateAccountResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userhash** | **str** |  | 
**pubkey** | **str** |  | 

## Example

```python
from dappserver-server-sdk.models.create_account_response_dto import CreateAccountResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountResponseDTO from a JSON string
create_account_response_dto_instance = CreateAccountResponseDTO.from_json(json)
# print the JSON string representation of the object
print CreateAccountResponseDTO.to_json()

# convert the object into a dict
create_account_response_dto_dict = create_account_response_dto_instance.to_dict()
# create an instance of CreateAccountResponseDTO from a dict
create_account_response_dto_form_dict = create_account_response_dto.from_dict(create_account_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


