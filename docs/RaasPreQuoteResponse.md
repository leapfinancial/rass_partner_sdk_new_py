# RaasPreQuoteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotes** | [**List[RaasPreQuoteValues]**](RaasPreQuoteValues.md) |  | 

## Example

```python
from raassdkpy.models.raas_pre_quote_response import RaasPreQuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RaasPreQuoteResponse from a JSON string
raas_pre_quote_response_instance = RaasPreQuoteResponse.from_json(json)
# print the JSON string representation of the object
print RaasPreQuoteResponse.to_json()

# convert the object into a dict
raas_pre_quote_response_dict = raas_pre_quote_response_instance.to_dict()
# create an instance of RaasPreQuoteResponse from a dict
raas_pre_quote_response_form_dict = raas_pre_quote_response.from_dict(raas_pre_quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


