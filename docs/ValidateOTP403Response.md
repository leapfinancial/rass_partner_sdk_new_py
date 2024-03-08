# ValidateOTP403Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from raassdkpyv2.models.validate_otp403_response import ValidateOTP403Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateOTP403Response from a JSON string
validate_otp403_response_instance = ValidateOTP403Response.from_json(json)
# print the JSON string representation of the object
print ValidateOTP403Response.to_json()

# convert the object into a dict
validate_otp403_response_dict = validate_otp403_response_instance.to_dict()
# create an instance of ValidateOTP403Response from a dict
validate_otp403_response_form_dict = validate_otp403_response.from_dict(validate_otp403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


