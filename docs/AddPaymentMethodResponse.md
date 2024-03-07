# AddPaymentMethodResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) |  | 
**error_validation** | **str** |  | [optional] 

## Example

```python
from raassdkpy.models.add_payment_method_response import AddPaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddPaymentMethodResponse from a JSON string
add_payment_method_response_instance = AddPaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print AddPaymentMethodResponse.to_json()

# convert the object into a dict
add_payment_method_response_dict = add_payment_method_response_instance.to_dict()
# create an instance of AddPaymentMethodResponse from a dict
add_payment_method_response_form_dict = add_payment_method_response.from_dict(add_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


