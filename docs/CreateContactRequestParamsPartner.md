# CreateContactRequestParamsPartner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**country_code** | [**CountryAlpha2Code**](CountryAlpha2Code.md) |  | 
**phone** | **str** |  | 
**last_name** | **str** |  | 
**first_name** | **str** |  | 
**email** | **str** |  | [optional] 

## Example

```python
from raassdkpy.models.create_contact_request_params_partner import CreateContactRequestParamsPartner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactRequestParamsPartner from a JSON string
create_contact_request_params_partner_instance = CreateContactRequestParamsPartner.from_json(json)
# print the JSON string representation of the object
print CreateContactRequestParamsPartner.to_json()

# convert the object into a dict
create_contact_request_params_partner_dict = create_contact_request_params_partner_instance.to_dict()
# create an instance of CreateContactRequestParamsPartner from a dict
create_contact_request_params_partner_form_dict = create_contact_request_params_partner.from_dict(create_contact_request_params_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


