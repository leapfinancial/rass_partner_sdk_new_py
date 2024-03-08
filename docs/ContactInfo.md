# ContactInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.contact_info import ContactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContactInfo from a JSON string
contact_info_instance = ContactInfo.from_json(json)
# print the JSON string representation of the object
print ContactInfo.to_json()

# convert the object into a dict
contact_info_dict = contact_info_instance.to_dict()
# create an instance of ContactInfo from a dict
contact_info_form_dict = contact_info.from_dict(contact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


