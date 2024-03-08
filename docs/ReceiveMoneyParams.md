# ReceiveMoneyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_payment_method** | **object** |  | 
**correlation_id** | **str** |  | 

## Example

```python
from raassdkpyv2.models.receive_money_params import ReceiveMoneyParams

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiveMoneyParams from a JSON string
receive_money_params_instance = ReceiveMoneyParams.from_json(json)
# print the JSON string representation of the object
print ReceiveMoneyParams.to_json()

# convert the object into a dict
receive_money_params_dict = receive_money_params_instance.to_dict()
# create an instance of ReceiveMoneyParams from a dict
receive_money_params_form_dict = receive_money_params.from_dict(receive_money_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


