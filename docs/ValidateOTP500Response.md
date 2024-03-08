# ValidateOTP500Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remaining_attempts** | **float** |  | 
**code** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from raassdkpyv2.models.validate_otp500_response import ValidateOTP500Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateOTP500Response from a JSON string
validate_otp500_response_instance = ValidateOTP500Response.from_json(json)
# print the JSON string representation of the object
print ValidateOTP500Response.to_json()

# convert the object into a dict
validate_otp500_response_dict = validate_otp500_response_instance.to_dict()
# create an instance of ValidateOTP500Response from a dict
validate_otp500_response_form_dict = validate_otp500_response.from_dict(validate_otp500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


