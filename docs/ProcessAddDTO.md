# ProcessAddDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**command** | **str** |  | 
**std_out** | **object** |  | 
**std_in** | **object** |  | 
**std_err** | **object** |  | 

## Example

```python
from dappserver-server-sdk.models.process_add_dto import ProcessAddDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessAddDTO from a JSON string
process_add_dto_instance = ProcessAddDTO.from_json(json)
# print the JSON string representation of the object
print ProcessAddDTO.to_json()

# convert the object into a dict
process_add_dto_dict = process_add_dto_instance.to_dict()
# create an instance of ProcessAddDTO from a dict
process_add_dto_form_dict = process_add_dto.from_dict(process_add_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


