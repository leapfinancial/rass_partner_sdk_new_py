# RaasQuoteTransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**source_currency** | **str** |  | 
**destination_currency** | **str** |  | 
**reason** | **str** |  | 
**reason_detail** | **object** |  | 
**source_amount** | **float** |  | 
**amount** | **float** |  | 
**destination_amount** | **float** |  | 
**exchange_rate** | **float** |  | 
**tax** | **float** |  | 
**source_fee** | **float** |  | 
**destination_fee** | **float** |  | 
**transaction_fee** | **float** |  | 
**sender_charge_back** | **float** |  | 
**recipient_charge_back** | **float** |  | 
**is_executable** | **bool** |  | 
**valid_time_in_minutes** | **float** |  | 
**tenant_fee** | **float** |  | 
**sender_user_id** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.raas_quote_transaction_response import RaasQuoteTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RaasQuoteTransactionResponse from a JSON string
raas_quote_transaction_response_instance = RaasQuoteTransactionResponse.from_json(json)
# print the JSON string representation of the object
print RaasQuoteTransactionResponse.to_json()

# convert the object into a dict
raas_quote_transaction_response_dict = raas_quote_transaction_response_instance.to_dict()
# create an instance of RaasQuoteTransactionResponse from a dict
raas_quote_transaction_response_form_dict = raas_quote_transaction_response.from_dict(raas_quote_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


