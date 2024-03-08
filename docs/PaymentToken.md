# PaymentToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**transaction_identifier** | **str** |  | [optional] 
**payment_network** | **str** |  | [optional] 
**data** | **str** |  | 

## Example

```python
from raassdkpyv2.models.payment_token import PaymentToken

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentToken from a JSON string
payment_token_instance = PaymentToken.from_json(json)
# print the JSON string representation of the object
print PaymentToken.to_json()

# convert the object into a dict
payment_token_dict = payment_token_instance.to_dict()
# create an instance of PaymentToken from a dict
payment_token_form_dict = payment_token.from_dict(payment_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


