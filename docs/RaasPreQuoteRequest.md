# RaasPreQuoteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** |  | [optional] 
**subscriber_id** | **str** |  | [optional] 
**destination_payment_method** | **object** |  | 
**sender_country_code** | **str** |  | 
**is_sender_amount** | **bool** |  | 
**amount** | **float** |  | 
**operation_type** | **str** |  | 
**product_type** | **str** |  | 
**tennant_fee** | **float** |  | [optional] 

## Example

```python
from raassdkpyv2.models.raas_pre_quote_request import RaasPreQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RaasPreQuoteRequest from a JSON string
raas_pre_quote_request_instance = RaasPreQuoteRequest.from_json(json)
# print the JSON string representation of the object
print RaasPreQuoteRequest.to_json()

# convert the object into a dict
raas_pre_quote_request_dict = raas_pre_quote_request_instance.to_dict()
# create an instance of RaasPreQuoteRequest from a dict
raas_pre_quote_request_form_dict = raas_pre_quote_request.from_dict(raas_pre_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


