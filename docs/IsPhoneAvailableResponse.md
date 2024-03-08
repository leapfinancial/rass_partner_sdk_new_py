# IsPhoneAvailableResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | If the phone is already in use, this field will be set to false. | 
**verified** | **bool** | If the phone is verified by SMS, this field will be set to true. | 
**has_pincode** | **bool** | If the user already set a pincode for this phone, this field will be set to true. | 

## Example

```python
from raassdkpyv2.models.is_phone_available_response import IsPhoneAvailableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IsPhoneAvailableResponse from a JSON string
is_phone_available_response_instance = IsPhoneAvailableResponse.from_json(json)
# print the JSON string representation of the object
print IsPhoneAvailableResponse.to_json()

# convert the object into a dict
is_phone_available_response_dict = is_phone_available_response_instance.to_dict()
# create an instance of IsPhoneAvailableResponse from a dict
is_phone_available_response_form_dict = is_phone_available_response.from_dict(is_phone_available_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


