# RequestOTPParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | [**Language**](Language.md) |  | [optional] 
**phone** | **str** | Mobile phone number in international format (e.g. +11234567890) | 

## Example

```python
from raassdkpy.models.request_otp_params import RequestOTPParams

# TODO update the JSON string below
json = "{}"
# create an instance of RequestOTPParams from a JSON string
request_otp_params_instance = RequestOTPParams.from_json(json)
# print the JSON string representation of the object
print RequestOTPParams.to_json()

# convert the object into a dict
request_otp_params_dict = request_otp_params_instance.to_dict()
# create an instance of RequestOTPParams from a dict
request_otp_params_form_dict = request_otp_params.from_dict(request_otp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


