# PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC

From T, pick a set of properties whose keys are in the union K

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cip_level** | **float** | this will updated  from event queue | 
**has_personal_info** | **bool** |  | 
**has_proof_of_l_ife** | **bool** |  | 
**has_scan_ids** | **bool** |  | 
**is_perform_level1** | **bool** |  | 
**is_perform_level2** | **bool** |  | 
**profile_and_ocr_similarity** | **float** |  | [optional] 
**errors_process** | [**ErrorsCIPProcess**](ErrorsCIPProcess.md) |  | 
**level1status** | [**LevelStatus**](LevelStatus.md) |  | 
**level1status_detail** | [**LevelStatusDetail**](LevelStatusDetail.md) |  | 
**level2status** | [**LevelStatus**](LevelStatus.md) |  | 
**level2status_detail** | [**LevelStatusDetail**](LevelStatusDetail.md) |  | 
**is_document_id_value_validated** | **bool** | This will be used when the document id value will be validated. For example The Nufi&#39;s CURP validation | [optional] 
**is_alternate_flow** | **bool** | This is for knowing the specific cip has an alternate flow | [optional] 
**lola_cip** | [**PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP**](PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP.md) |  | [optional] 

## Example

```python
from raassdkpyv2.models.pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac import PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC

# TODO update the JSON string below
json = "{}"
# create an instance of PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC from a JSON string
pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac_instance = PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC.from_json(json)
# print the JSON string representation of the object
print PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC.to_json()

# convert the object into a dict
pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac_dict = pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac_instance.to_dict()
# create an instance of PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC from a dict
pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac_form_dict = pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac.from_dict(pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


