# OperationUserDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_picture_url** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone_number** | **str** |  | 
**last_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.operation_user_detail import OperationUserDetail

# TODO update the JSON string below
json = "{}"
# create an instance of OperationUserDetail from a JSON string
operation_user_detail_instance = OperationUserDetail.from_json(json)
# print the JSON string representation of the object
print OperationUserDetail.to_json()

# convert the object into a dict
operation_user_detail_dict = operation_user_detail_instance.to_dict()
# create an instance of OperationUserDetail from a dict
operation_user_detail_form_dict = operation_user_detail.from_dict(operation_user_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


