# AddCardPartnerParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cardtype** | **str** |  | 
**number** | **str** |  | 
**is_primary** | **bool** |  | 
**name_on_card** | **str** |  | 
**expiration_date** | **str** |  | 
**security_code** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**country** | **str** |  | 
**operation_id** | **str** |  | [optional] 
**card_network** | **str** |  | 

## Example

```python
from raassdkpy.models.add_card_partner_params import AddCardPartnerParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddCardPartnerParams from a JSON string
add_card_partner_params_instance = AddCardPartnerParams.from_json(json)
# print the JSON string representation of the object
print AddCardPartnerParams.to_json()

# convert the object into a dict
add_card_partner_params_dict = add_card_partner_params_instance.to_dict()
# create an instance of AddCardPartnerParams from a dict
add_card_partner_params_form_dict = add_card_partner_params.from_dict(add_card_partner_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


