# SendMoneyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**source_payment_method** | [**RaaSPaymentMethod**](RaaSPaymentMethod.md) |  | 
**destination_payment_method** | [**RaaSPaymentMethod**](RaaSPaymentMethod.md) |  | [optional] 
**amount** | **float** |  | 
**currency** | **str** |  | 
**code** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**sender_amount** | **float** |  | 
**sender_currency** | **str** |  | 
**recipient_amount** | **float** |  | 
**recipient_currency** | **str** |  | 
**fee_type** | **str** |  | 
**source_fee** | **float** |  | 
**transaction_fee** | **float** |  | 
**destination_fee** | **float** |  | 
**exchange_rate** | **float** |  | 
**call_location_longitude** | **float** |  | 
**call_location_latitude** | **float** |  | 
**reason** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_tenant_id** | **str** |  | [optional] 
**tenant_fee** | **float** |  | [optional] 
**send_to** | **str** |  | 

## Example

```python
from raassdkpyv2.models.send_money_params import SendMoneyParams

# TODO update the JSON string below
json = "{}"
# create an instance of SendMoneyParams from a JSON string
send_money_params_instance = SendMoneyParams.from_json(json)
# print the JSON string representation of the object
print SendMoneyParams.to_json()

# convert the object into a dict
send_money_params_dict = send_money_params_instance.to_dict()
# create an instance of SendMoneyParams from a dict
send_money_params_form_dict = send_money_params.from_dict(send_money_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


