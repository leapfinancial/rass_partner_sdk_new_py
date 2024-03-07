# SessionLinkParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | 
**last_name** | **str** |  | 
**last_name2** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**dob** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | 
**middle_name** | **str** |  | [optional] 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**country_code** | [**CountryAlpha2Code**](CountryAlpha2Code.md) |  | 
**city** | **str** |  | 
**zip_code** | **str** |  | [optional] 
**state** | **str** |  | 
**birth_state** | **str** |  | [optional] 
**add_card_params** | [**AddCardSessionParams**](AddCardSessionParams.md) |  | [optional] 

## Example

```python
from raassdkpy.models.session_link_params import SessionLinkParams

# TODO update the JSON string below
json = "{}"
# create an instance of SessionLinkParams from a JSON string
session_link_params_instance = SessionLinkParams.from_json(json)
# print the JSON string representation of the object
print SessionLinkParams.to_json()

# convert the object into a dict
session_link_params_dict = session_link_params_instance.to_dict()
# create an instance of SessionLinkParams from a dict
session_link_params_form_dict = session_link_params.from_dict(session_link_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


