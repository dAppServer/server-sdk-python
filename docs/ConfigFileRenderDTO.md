# ConfigFileRenderDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** |  | 
**model** | **object** |  | 

## Example

```python
from dappserver-server-sdk.models.config_file_render_dto import ConfigFileRenderDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFileRenderDTO from a JSON string
config_file_render_dto_instance = ConfigFileRenderDTO.from_json(json)
# print the JSON string representation of the object
print ConfigFileRenderDTO.to_json()

# convert the object into a dict
config_file_render_dto_dict = config_file_render_dto_instance.to_dict()
# create an instance of ConfigFileRenderDTO from a dict
config_file_render_dto_form_dict = config_file_render_dto.from_dict(config_file_render_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


