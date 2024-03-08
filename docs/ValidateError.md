# ValidateError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**message** | **str** |  | 
**stack** | **str** |  | [optional] 
**status** | **float** |  | 
**fields** | [**Dict[str, FieldErrorsValue]**](FieldErrorsValue.md) |  | 

## Example

```python
from raassdkpyv2.models.validate_error import ValidateError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateError from a JSON string
validate_error_instance = ValidateError.from_json(json)
# print the JSON string representation of the object
print ValidateError.to_json()

# convert the object into a dict
validate_error_dict = validate_error_instance.to_dict()
# create an instance of ValidateError from a dict
validate_error_form_dict = validate_error.from_dict(validate_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


