# RaaSPaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_token** | [**PaymentToken**](PaymentToken.md) |  | [optional] 
**status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) |  | [optional] 
**application** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**latitude** | **float** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**country** | **str** |  | 
**zip_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**card_network** | **str** |  | [optional] 
**cardtype** | **str** |  | [optional] 
**security_code** | **str** |  | [optional] 
**expiration_month** | **str** |  | [optional] 
**expiration_year** | **str** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**name_on_card** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**beneficiary_account_id** | **str** |  | [optional] 
**token_data** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**bank_entity_number** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_account_type** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**is_primary** | **bool** |  | [optional] 
**type** | [**AvailablePaymentMethods**](AvailablePaymentMethods.md) |  | 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.raa_s_payment_method import RaaSPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of RaaSPaymentMethod from a JSON string
raa_s_payment_method_instance = RaaSPaymentMethod.from_json(json)
# print the JSON string representation of the object
print RaaSPaymentMethod.to_json()

# convert the object into a dict
raa_s_payment_method_dict = raa_s_payment_method_instance.to_dict()
# create an instance of RaaSPaymentMethod from a dict
raa_s_payment_method_form_dict = raa_s_payment_method.from_dict(raa_s_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


