# SendMoneyPartnerParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotation_id** | **str** |  | 
**currency** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**destination_payment_method_id** | **str** |  | [optional] 
**source_payment_method_id** | **str** |  | [optional] 
**correlation_id** | **str** |  | 
**send_to** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.send_money_partner_params import SendMoneyPartnerParams

# TODO update the JSON string below
json = "{}"
# create an instance of SendMoneyPartnerParams from a JSON string
send_money_partner_params_instance = SendMoneyPartnerParams.from_json(json)
# print the JSON string representation of the object
print SendMoneyPartnerParams.to_json()

# convert the object into a dict
send_money_partner_params_dict = send_money_partner_params_instance.to_dict()
# create an instance of SendMoneyPartnerParams from a dict
send_money_partner_params_form_dict = send_money_partner_params.from_dict(send_money_partner_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


