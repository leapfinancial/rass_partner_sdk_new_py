# IgnoredOperationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**var_date** | **datetime** |  | 
**notify_support** | **bool** |  | 
**reason** | [**IgnoredOperationReason**](IgnoredOperationReason.md) |  | 
**responsible_user_id** | **str** |  | 

## Example

```python
from raassdkpy.models.ignored_operation_data import IgnoredOperationData

# TODO update the JSON string below
json = "{}"
# create an instance of IgnoredOperationData from a JSON string
ignored_operation_data_instance = IgnoredOperationData.from_json(json)
# print the JSON string representation of the object
print IgnoredOperationData.to_json()

# convert the object into a dict
ignored_operation_data_dict = ignored_operation_data_instance.to_dict()
# create an instance of IgnoredOperationData from a dict
ignored_operation_data_form_dict = ignored_operation_data.from_dict(ignored_operation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


