# FileDownloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**file** | **str** |  | 
**dir** | **str** |  | 
**mode** | **float** |  | [optional] 

## Example

```python
from dappserver-server-sdk.models.file_download_request import FileDownloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileDownloadRequest from a JSON string
file_download_request_instance = FileDownloadRequest.from_json(json)
# print the JSON string representation of the object
print FileDownloadRequest.to_json()

# convert the object into a dict
file_download_request_dict = file_download_request_instance.to_dict()
# create an instance of FileDownloadRequest from a dict
file_download_request_form_dict = file_download_request.from_dict(file_download_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


