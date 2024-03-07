# ValidatePhoneNumberRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from raassdkpy.models.validate_phone_number_request import ValidatePhoneNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePhoneNumberRequest from a JSON string
validate_phone_number_request_instance = ValidatePhoneNumberRequest.from_json(json)
# print the JSON string representation of the object
print ValidatePhoneNumberRequest.to_json()

# convert the object into a dict
validate_phone_number_request_dict = validate_phone_number_request_instance.to_dict()
# create an instance of ValidatePhoneNumberRequest from a dict
validate_phone_number_request_form_dict = validate_phone_number_request.from_dict(validate_phone_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


