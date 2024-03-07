# PerformLevelOneParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_description** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**call_location_longitude** | **float** |  | 
**call_location_latitude** | **float** |  | 
**city** | **str** |  | 
**birth_state** | **str** |  | [optional] 
**state** | **str** |  | 
**zip_code** | **str** |  | 
**gender** | **str** |  | [optional] 
**place_detail** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address1** | **str** |  | 
**date_of_birth** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**second_last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | 
**first_name** | **str** |  | 

## Example

```python
from raassdkpy.models.perform_level_one_params import PerformLevelOneParams

# TODO update the JSON string below
json = "{}"
# create an instance of PerformLevelOneParams from a JSON string
perform_level_one_params_instance = PerformLevelOneParams.from_json(json)
# print the JSON string representation of the object
print PerformLevelOneParams.to_json()

# convert the object into a dict
perform_level_one_params_dict = perform_level_one_params_instance.to_dict()
# create an instance of PerformLevelOneParams from a dict
perform_level_one_params_form_dict = perform_level_one_params.from_dict(perform_level_one_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


