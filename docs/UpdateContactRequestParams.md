# UpdateContactRequestParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | 

## Example

```python
from raassdkpy.models.update_contact_request_params import UpdateContactRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactRequestParams from a JSON string
update_contact_request_params_instance = UpdateContactRequestParams.from_json(json)
# print the JSON string representation of the object
print UpdateContactRequestParams.to_json()

# convert the object into a dict
update_contact_request_params_dict = update_contact_request_params_instance.to_dict()
# create an instance of UpdateContactRequestParams from a dict
update_contact_request_params_form_dict = update_contact_request_params.from_dict(update_contact_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


