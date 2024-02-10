# ConfigFileRenderAndLoadDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** |  | 
**model** | [**ConfigObjectGetDTO**](ConfigObjectGetDTO.md) |  | 

## Example

```python
from dappserver_server_sdk.models.config_file_render_and_load_dto import ConfigFileRenderAndLoadDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFileRenderAndLoadDTO from a JSON string
config_file_render_and_load_dto_instance = ConfigFileRenderAndLoadDTO.from_json(json)
# print the JSON string representation of the object
print ConfigFileRenderAndLoadDTO.to_json()

# convert the object into a dict
config_file_render_and_load_dto_dict = config_file_render_and_load_dto_instance.to_dict()
# create an instance of ConfigFileRenderAndLoadDTO from a dict
config_file_render_and_load_dto_form_dict = config_file_render_and_load_dto.from_dict(config_file_render_and_load_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


