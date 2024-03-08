# ReplaceCardPartnerParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | 
**name** | **str** |  | 
**cardtype** | **str** |  | 
**is_primary** | **bool** |  | 
**name_on_card** | **str** |  | 
**expiration_date** | **str** |  | 
**security_code** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**country** | **str** |  | 
**card_network** | **str** |  | 
**operation_id** | **str** |  | 

## Example

```python
from raassdkpyv2.models.replace_card_partner_params import ReplaceCardPartnerParams

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceCardPartnerParams from a JSON string
replace_card_partner_params_instance = ReplaceCardPartnerParams.from_json(json)
# print the JSON string representation of the object
print ReplaceCardPartnerParams.to_json()

# convert the object into a dict
replace_card_partner_params_dict = replace_card_partner_params_instance.to_dict()
# create an instance of ReplaceCardPartnerParams from a dict
replace_card_partner_params_form_dict = replace_card_partner_params.from_dict(replace_card_partner_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


