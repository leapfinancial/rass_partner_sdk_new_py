# QuoteTransactionBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_user_id** | **str** |  | [optional] 
**sender_country_code** | **str** |  | 
**recipient_user_id** | **str** |  | 
**recipient_country_code** | **str** |  | 
**recipient_currency** | **str** |  | 
**recipient_amount** | **float** |  | 
**is_sender_amount** | **bool** |  | 
**amount_currency** | **str** |  | 
**amount** | **float** |  | 
**operation_type** | **object** | \&quot;SendFunds\&quot;|\&quot;RequestFunds\&quot;|\&quot;WalletLoad\&quot;|\&quot;WalletTransferOut\&quot;|\&quot;TopUp\&quot;|\&quot;RequestTopUp\&quot;|\&quot;SendFundsVirtualAgent\&quot;|\&quot;RequestFundsVirtualAgent\&quot;|\&quot;StorePayment\&quot; | 
**source_payment_method** | **object** |  | 
**destination_payment_method** | **object** |  | [optional] 
**tennant_fee** | **float** |  | [optional] 

## Example

```python
from raassdkpy.models.quote_transaction_base import QuoteTransactionBase

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteTransactionBase from a JSON string
quote_transaction_base_instance = QuoteTransactionBase.from_json(json)
# print the JSON string representation of the object
print QuoteTransactionBase.to_json()

# convert the object into a dict
quote_transaction_base_dict = quote_transaction_base_instance.to_dict()
# create an instance of QuoteTransactionBase from a dict
quote_transaction_base_form_dict = quote_transaction_base.from_dict(quote_transaction_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


