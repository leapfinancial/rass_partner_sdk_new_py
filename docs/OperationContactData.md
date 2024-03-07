# OperationContactData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**contact_id** | **str** |  | 
**country_code** | **str** |  | 
**mobile_phone** | **str** |  | 
**first_name** | **str** |  | 
**middle_name** | **str** |  | 
**last_name** | **str** |  | 
**last_name2** | **str** |  | 
**email** | **str** |  | 
**relationship** | **str** |  | 

## Example

```python
from raassdkpy.models.operation_contact_data import OperationContactData

# TODO update the JSON string below
json = "{}"
# create an instance of OperationContactData from a JSON string
operation_contact_data_instance = OperationContactData.from_json(json)
# print the JSON string representation of the object
print OperationContactData.to_json()

# convert the object into a dict
operation_contact_data_dict = operation_contact_data_instance.to_dict()
# create an instance of OperationContactData from a dict
operation_contact_data_form_dict = operation_contact_data.from_dict(operation_contact_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


