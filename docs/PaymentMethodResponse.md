# PaymentMethodResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**is_primary** | **bool** |  | [optional] 
**account_number** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.payment_method_response import PaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodResponse from a JSON string
payment_method_response_instance = PaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print PaymentMethodResponse.to_json()

# convert the object into a dict
payment_method_response_dict = payment_method_response_instance.to_dict()
# create an instance of PaymentMethodResponse from a dict
payment_method_response_form_dict = payment_method_response.from_dict(payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


