# IPhoneInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** |  | [optional] 
**caller_name** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**phone_number** | **str** |  | 
**carrier** | [**IPhoneInfoCarrier**](IPhoneInfoCarrier.md) |  | [optional] 

## Example

```python
from raassdkpyv2.models.i_phone_info import IPhoneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IPhoneInfo from a JSON string
i_phone_info_instance = IPhoneInfo.from_json(json)
# print the JSON string representation of the object
print IPhoneInfo.to_json()

# convert the object into a dict
i_phone_info_dict = i_phone_info_instance.to_dict()
# create an instance of IPhoneInfo from a dict
i_phone_info_form_dict = i_phone_info.from_dict(i_phone_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


