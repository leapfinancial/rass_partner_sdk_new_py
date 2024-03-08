# LevelOneParamsRequst


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zip_code** | **str** |  | 
**place_detail** | **str** |  | [optional] 
**city** | **str** |  | 
**address4** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address1** | **str** |  | 
**call_location_longitude** | **float** |  | 
**call_location_latitude** | **float** |  | 
**country_code** | **str** |  | 
**state** | **str** |  | 
**date_of_birth** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**birth_state** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from raassdkpyv2.models.level_one_params_requst import LevelOneParamsRequst

# TODO update the JSON string below
json = "{}"
# create an instance of LevelOneParamsRequst from a JSON string
level_one_params_requst_instance = LevelOneParamsRequst.from_json(json)
# print the JSON string representation of the object
print LevelOneParamsRequst.to_json()

# convert the object into a dict
level_one_params_requst_dict = level_one_params_requst_instance.to_dict()
# create an instance of LevelOneParamsRequst from a dict
level_one_params_requst_form_dict = level_one_params_requst.from_dict(level_one_params_requst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


