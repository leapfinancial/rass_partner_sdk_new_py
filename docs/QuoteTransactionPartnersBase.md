# QuoteTransactionPartnersBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_user_id** | **str** |  | 
**currency** | **str** |  | 
**amount** | **float** |  | 
**source_payment_method_id** | **str** |  | 
**destination_payment_method_id** | **str** |  | [optional] 

## Example

```python
from raassdkpy.models.quote_transaction_partners_base import QuoteTransactionPartnersBase

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteTransactionPartnersBase from a JSON string
quote_transaction_partners_base_instance = QuoteTransactionPartnersBase.from_json(json)
# print the JSON string representation of the object
print QuoteTransactionPartnersBase.to_json()

# convert the object into a dict
quote_transaction_partners_base_dict = quote_transaction_partners_base_instance.to_dict()
# create an instance of QuoteTransactionPartnersBase from a dict
quote_transaction_partners_base_form_dict = quote_transaction_partners_base.from_dict(quote_transaction_partners_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


