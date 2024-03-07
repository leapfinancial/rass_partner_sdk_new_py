# PerformResubmitUpgradeLevelParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** |  | 
**level_status_detail** | **str** |  | 
**call_location_longitude** | **float** |  | 
**call_location_latitude** | **float** |  | 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**address4** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**place_detail** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**date_of_birth** | **str** |  | [optional] 
**nationality** | **str** |  | [optional] 
**birth_state** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**documents** | [**List[UserDocument]**](UserDocument.md) |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**last_name2** | **str** |  | [optional] 
**is_id_address_different** | **bool** |  | [optional] 

## Example

```python
from raassdkpy.models.perform_resubmit_upgrade_level_params import PerformResubmitUpgradeLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of PerformResubmitUpgradeLevelParams from a JSON string
perform_resubmit_upgrade_level_params_instance = PerformResubmitUpgradeLevelParams.from_json(json)
# print the JSON string representation of the object
print PerformResubmitUpgradeLevelParams.to_json()

# convert the object into a dict
perform_resubmit_upgrade_level_params_dict = perform_resubmit_upgrade_level_params_instance.to_dict()
# create an instance of PerformResubmitUpgradeLevelParams from a dict
perform_resubmit_upgrade_level_params_form_dict = perform_resubmit_upgrade_level_params.from_dict(perform_resubmit_upgrade_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


