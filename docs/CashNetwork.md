# CashNetwork

id: Unique Identifier of CashNetwork  name: Name of Network  cashProvider: Enum that identifies the type of provider use {Numi, Greendot, Inpamex, NumiCashDelivery, Incomm}   imageUrl: URL of image to identify this network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**cash_provider** | **object** |  | 
**image_url** | **str** |  | 

## Example

```python
from raassdkpy.models.cash_network import CashNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of CashNetwork from a JSON string
cash_network_instance = CashNetwork.from_json(json)
# print the JSON string representation of the object
print CashNetwork.to_json()

# convert the object into a dict
cash_network_dict = cash_network_instance.to_dict()
# create an instance of CashNetwork from a dict
cash_network_form_dict = cash_network.from_dict(cash_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


