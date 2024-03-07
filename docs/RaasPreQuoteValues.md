# RaasPreQuoteValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_rate** | **float** |  | 
**source_fee** | **float** |  | 
**transaction_fee** | **float** |  | 
**destination_fee** | **float** |  | 
**tenant_fee** | **float** |  | 
**type** | [**AvailablePaymentMethods**](AvailablePaymentMethods.md) |  | 

## Example

```python
from raassdkpy.models.raas_pre_quote_values import RaasPreQuoteValues

# TODO update the JSON string below
json = "{}"
# create an instance of RaasPreQuoteValues from a JSON string
raas_pre_quote_values_instance = RaasPreQuoteValues.from_json(json)
# print the JSON string representation of the object
print RaasPreQuoteValues.to_json()

# convert the object into a dict
raas_pre_quote_values_dict = raas_pre_quote_values_instance.to_dict()
# create an instance of RaasPreQuoteValues from a dict
raas_pre_quote_values_form_dict = raas_pre_quote_values.from_dict(raas_pre_quote_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


