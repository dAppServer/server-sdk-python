# ProcessRunDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | 
**args** | **str** |  | 
**options** | [**ProcessAddDTO**](ProcessAddDTO.md) |  | 

## Example

```python
from dappserver-server-sdk.models.process_run_dto import ProcessRunDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessRunDTO from a JSON string
process_run_dto_instance = ProcessRunDTO.from_json(json)
# print the JSON string representation of the object
print ProcessRunDTO.to_json()

# convert the object into a dict
process_run_dto_dict = process_run_dto_instance.to_dict()
# create an instance of ProcessRunDTO from a dict
process_run_dto_form_dict = process_run_dto.from_dict(process_run_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


