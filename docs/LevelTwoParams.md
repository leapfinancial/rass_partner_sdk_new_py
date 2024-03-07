# LevelTwoParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssn** | **str** |  | [optional] 
**call_location_longitude** | **float** |  | 
**call_location_latitude** | **float** |  | 

## Example

```python
from raassdkpy.models.level_two_params import LevelTwoParams

# TODO update the JSON string below
json = "{}"
# create an instance of LevelTwoParams from a JSON string
level_two_params_instance = LevelTwoParams.from_json(json)
# print the JSON string representation of the object
print LevelTwoParams.to_json()

# convert the object into a dict
level_two_params_dict = level_two_params_instance.to_dict()
# create an instance of LevelTwoParams from a dict
level_two_params_form_dict = level_two_params.from_dict(level_two_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


