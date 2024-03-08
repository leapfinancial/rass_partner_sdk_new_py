# RegisterUserParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | 
**last_name** | **str** |  | 
**last_name2** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**dob** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | 
**middle_name** | **str** |  | [optional] 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**country_code** | [**CountryAlpha2Code**](CountryAlpha2Code.md) |  | 
**city** | **str** |  | 
**zip_code** | **str** |  | [optional] 
**state** | **str** |  | 
**birth_state** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.register_user_params import RegisterUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterUserParams from a JSON string
register_user_params_instance = RegisterUserParams.from_json(json)
# print the JSON string representation of the object
print RegisterUserParams.to_json()

# convert the object into a dict
register_user_params_dict = register_user_params_instance.to_dict()
# create an instance of RegisterUserParams from a dict
register_user_params_form_dict = register_user_params.from_dict(register_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


