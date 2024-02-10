# BlockchainLetheanWalletStartDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_dir** | **str** |  | 
**rpc_bind_port** | **float** |  | 
**disable_rpc_login** | **bool** |  | 

## Example

```python
from dappserver_server_sdk.models.blockchain_lethean_wallet_start_dto import BlockchainLetheanWalletStartDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainLetheanWalletStartDTO from a JSON string
blockchain_lethean_wallet_start_dto_instance = BlockchainLetheanWalletStartDTO.from_json(json)
# print the JSON string representation of the object
print BlockchainLetheanWalletStartDTO.to_json()

# convert the object into a dict
blockchain_lethean_wallet_start_dto_dict = blockchain_lethean_wallet_start_dto_instance.to_dict()
# create an instance of BlockchainLetheanWalletStartDTO from a dict
blockchain_lethean_wallet_start_dto_form_dict = blockchain_lethean_wallet_start_dto.from_dict(blockchain_lethean_wallet_start_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


