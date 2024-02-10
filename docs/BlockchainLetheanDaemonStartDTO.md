# BlockchainLetheanDaemonStartDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_file** | **str** |  | 
**data_dir** | **str** |  | 
**log_dir** | **str** |  | 

## Example

```python
from dappserver_server_sdk.models.blockchain_lethean_daemon_start_dto import BlockchainLetheanDaemonStartDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainLetheanDaemonStartDTO from a JSON string
blockchain_lethean_daemon_start_dto_instance = BlockchainLetheanDaemonStartDTO.from_json(json)
# print the JSON string representation of the object
print BlockchainLetheanDaemonStartDTO.to_json()

# convert the object into a dict
blockchain_lethean_daemon_start_dto_dict = blockchain_lethean_daemon_start_dto_instance.to_dict()
# create an instance of BlockchainLetheanDaemonStartDTO from a dict
blockchain_lethean_daemon_start_dto_form_dict = blockchain_lethean_daemon_start_dto.from_dict(blockchain_lethean_daemon_start_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


