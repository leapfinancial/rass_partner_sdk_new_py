# RaaSPartnerPaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**bank_account_type** | **str** |  | [optional] 
**cardtype** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**bank_entity_number** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**is_primary** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.raa_s_partner_payment_method import RaaSPartnerPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of RaaSPartnerPaymentMethod from a JSON string
raa_s_partner_payment_method_instance = RaaSPartnerPaymentMethod.from_json(json)
# print the JSON string representation of the object
print RaaSPartnerPaymentMethod.to_json()

# convert the object into a dict
raa_s_partner_payment_method_dict = raa_s_partner_payment_method_instance.to_dict()
# create an instance of RaaSPartnerPaymentMethod from a dict
raa_s_partner_payment_method_form_dict = raa_s_partner_payment_method.from_dict(raa_s_partner_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


