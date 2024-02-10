# ServerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **float** |  | 
**data** | **str** |  | 
**signature** | **str** |  | [optional] 

## Example

```python
from dappserver-server-sdk.models.server_response import ServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServerResponse from a JSON string
server_response_instance = ServerResponse.from_json(json)
# print the JSON string representation of the object
print ServerResponse.to_json()

# convert the object into a dict
server_response_dict = server_response_instance.to_dict()
# create an instance of ServerResponse from a dict
server_response_form_dict = server_response.from_dict(server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


