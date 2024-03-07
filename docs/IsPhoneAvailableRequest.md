# IsPhoneAvailableRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Phone number to check. Phone number must be in E.164 format. e.g. \&quot;+12223334444\&quot; | 

## Example

```python
from raassdkpy.models.is_phone_available_request import IsPhoneAvailableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IsPhoneAvailableRequest from a JSON string
is_phone_available_request_instance = IsPhoneAvailableRequest.from_json(json)
# print the JSON string representation of the object
print IsPhoneAvailableRequest.to_json()

# convert the object into a dict
is_phone_available_request_dict = is_phone_available_request_instance.to_dict()
# create an instance of IsPhoneAvailableRequest from a dict
is_phone_available_request_form_dict = is_phone_available_request.from_dict(is_phone_available_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


