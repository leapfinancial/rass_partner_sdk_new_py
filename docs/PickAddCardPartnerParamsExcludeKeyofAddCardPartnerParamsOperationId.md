# PickAddCardPartnerParamsExcludeKeyofAddCardPartnerParamsOperationId

From T, pick a set of properties whose keys are in the union K

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

## Example

```python
from raassdkpyv2.models.pick_add_card_partner_params_exclude_keyof_add_card_partner_params_operation_id import PickAddCardPartnerParamsExcludeKeyofAddCardPartnerParamsOperationId

# TODO update the JSON string below
json = "{}"
# create an instance of PickAddCardPartnerParamsExcludeKeyofAddCardPartnerParamsOperationId from a JSON string
pick_add_card_partner_params_exclude_keyof_add_card_partner_params_operation_id_instance = PickAddCardPartnerParamsExcludeKeyofAddCardPartnerParamsOperationId.from_json(json)
# print the JSON string representation of the object
print PickAddCardPartnerParamsExcludeKeyofAddCardPartnerParamsOperationId.to_json()

# convert the object into a dict
pick_add_card_partner_params_exclude_keyof_add_card_partner_params_operation_id_dict = pick_add_card_partner_params_exclude_keyof_add_card_partner_params_operation_id_instance.to_dict()
# create an instance of PickAddCardPartnerParamsExcludeKeyofAddCardPartnerParamsOperationId from a dict
pick_add_card_partner_params_exclude_keyof_add_card_partner_params_operation_id_form_dict = pick_add_card_partner_params_exclude_keyof_add_card_partner_params_operation_id.from_dict(pick_add_card_partner_params_exclude_keyof_add_card_partner_params_operation_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


