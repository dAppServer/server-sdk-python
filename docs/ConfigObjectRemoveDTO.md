# ConfigObjectRemoveDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**object** | **str** |  | 

## Example

```python
from dappserver-server-sdk.models.config_object_remove_dto import ConfigObjectRemoveDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigObjectRemoveDTO from a JSON string
config_object_remove_dto_instance = ConfigObjectRemoveDTO.from_json(json)
# print the JSON string representation of the object
print ConfigObjectRemoveDTO.to_json()

# convert the object into a dict
config_object_remove_dto_dict = config_object_remove_dto_instance.to_dict()
# create an instance of ConfigObjectRemoveDTO from a dict
config_object_remove_dto_form_dict = config_object_remove_dto.from_dict(config_object_remove_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


