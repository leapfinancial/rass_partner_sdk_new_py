# RequestMoneyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**destination_payment_method** | [**RaaSPaymentMethod**](RaaSPaymentMethod.md) |  | 
**reason** | **str** |  | 
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**sender_currency** | **str** |  | [optional] 
**sender_amount** | **float** |  | [optional] 
**recipient_amount** | **float** |  | 
**recipient_currency** | **str** |  | 
**bonus_amount** | **float** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_tenant_id** | **str** |  | [optional] 
**application** | **str** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**request_to** | **str** |  | 

## Example

```python
from raassdkpyv2.models.request_money_params import RequestMoneyParams

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMoneyParams from a JSON string
request_money_params_instance = RequestMoneyParams.from_json(json)
# print the JSON string representation of the object
print RequestMoneyParams.to_json()

# convert the object into a dict
request_money_params_dict = request_money_params_instance.to_dict()
# create an instance of RequestMoneyParams from a dict
request_money_params_form_dict = request_money_params.from_dict(request_money_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


