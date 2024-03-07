# OperationDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**created_at** | **datetime** |  | 
**status** | **str** |  | 
**reason** | **str** |  | [optional] 
**code** | **str** |  | 
**amount** | **float** |  | 
**sender_amount** | **float** |  | 
**recipient_amout** | **float** |  | 
**currency** | **str** |  | [optional] 
**sender_currency** | **str** |  | [optional] 
**recipient_currency** | **str** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**from_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**to_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**attribution_link** | **str** |  | [optional] 
**is_ignored** | **bool** |  | [optional] 
**ignored_data** | **object** |  | [optional] 

## Example

```python
from raassdkpy.models.operation_detail import OperationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDetail from a JSON string
operation_detail_instance = OperationDetail.from_json(json)
# print the JSON string representation of the object
print OperationDetail.to_json()

# convert the object into a dict
operation_detail_dict = operation_detail_instance.to_dict()
# create an instance of OperationDetail from a dict
operation_detail_form_dict = operation_detail.from_dict(operation_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


