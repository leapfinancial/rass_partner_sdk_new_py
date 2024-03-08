# RequestMoneyPartnerParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_to** | **str** |  | 
**correlation_id** | **str** |  | 
**destination_payment_method_id** | **str** |  | 
**recipient_amount** | **float** |  | 
**recipient_currency** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.request_money_partner_params import RequestMoneyPartnerParams

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMoneyPartnerParams from a JSON string
request_money_partner_params_instance = RequestMoneyPartnerParams.from_json(json)
# print the JSON string representation of the object
print RequestMoneyPartnerParams.to_json()

# convert the object into a dict
request_money_partner_params_dict = request_money_partner_params_instance.to_dict()
# create an instance of RequestMoneyPartnerParams from a dict
request_money_partner_params_form_dict = request_money_partner_params.from_dict(request_money_partner_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


