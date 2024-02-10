# CreateFileDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**data** | **str** |  | 

## Example

```python
from dappserver_server_sdk.models.create_file_dto import CreateFileDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileDTO from a JSON string
create_file_dto_instance = CreateFileDTO.from_json(json)
# print the JSON string representation of the object
print CreateFileDTO.to_json()

# convert the object into a dict
create_file_dto_dict = create_file_dto_instance.to_dict()
# create an instance of CreateFileDTO from a dict
create_file_dto_form_dict = create_file_dto.from_dict(create_file_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


