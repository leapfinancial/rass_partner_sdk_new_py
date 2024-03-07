# UserUpdateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**second_last_name** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**place_id** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**dob** | **datetime** |  | [optional] 
**country_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**first_time** | **bool** |  | [optional] 

## Example

```python
from raassdkpy.models.user_update_params import UserUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateParams from a JSON string
user_update_params_instance = UserUpdateParams.from_json(json)
# print the JSON string representation of the object
print UserUpdateParams.to_json()

# convert the object into a dict
user_update_params_dict = user_update_params_instance.to_dict()
# create an instance of UserUpdateParams from a dict
user_update_params_form_dict = user_update_params.from_dict(user_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


