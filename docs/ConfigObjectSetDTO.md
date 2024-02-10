# ConfigObjectSetDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**object** | **str** |  | 
**data** | **str** |  | 

## Example

```python
from dappserver-server-sdk.models.config_object_set_dto import ConfigObjectSetDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigObjectSetDTO from a JSON string
config_object_set_dto_instance = ConfigObjectSetDTO.from_json(json)
# print the JSON string representation of the object
print ConfigObjectSetDTO.to_json()

# convert the object into a dict
config_object_set_dto_dict = config_object_set_dto_instance.to_dict()
# create an instance of ConfigObjectSetDTO from a dict
config_object_set_dto_form_dict = config_object_set_dto.from_dict(config_object_set_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


