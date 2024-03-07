# RequestOtp404Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**reason** | **str** |  | 

## Example

```python
from raassdkpy.models.request_otp404_response import RequestOtp404Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestOtp404Response from a JSON string
request_otp404_response_instance = RequestOtp404Response.from_json(json)
# print the JSON string representation of the object
print RequestOtp404Response.to_json()

# convert the object into a dict
request_otp404_response_dict = request_otp404_response_instance.to_dict()
# create an instance of RequestOtp404Response from a dict
request_otp404_response_form_dict = request_otp404_response.from_dict(request_otp404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


