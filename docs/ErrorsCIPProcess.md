# ErrorsCIPProcess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_id_scan_date_expired** | **str** |  | [optional] 
**error_ofac_not_valid** | **str** |  | [optional] 
**error_face_match_not_valid** | **str** |  | [optional] 
**error_photo_scan_id_required** | **str** |  | [optional] 
**error_ocr_profile_match_not_valid** | **str** |  | [optional] 

## Example

```python
from raassdkpy.models.errors_cip_process import ErrorsCIPProcess

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsCIPProcess from a JSON string
errors_cip_process_instance = ErrorsCIPProcess.from_json(json)
# print the JSON string representation of the object
print ErrorsCIPProcess.to_json()

# convert the object into a dict
errors_cip_process_dict = errors_cip_process_instance.to_dict()
# create an instance of ErrorsCIPProcess from a dict
errors_cip_process_form_dict = errors_cip_process.from_dict(errors_cip_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


