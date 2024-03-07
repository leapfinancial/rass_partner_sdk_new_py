# CIPData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**county** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**dob** | **datetime** |  | [optional] 
**dob_raw** | **str** |  | [optional] 
**doc_type** | **str** |  | [optional] 
**exp_date** | **datetime** |  | [optional] 
**exp_date_raw** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**id_country** | **str** |  | [optional] 
**id_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**names** | **str** |  | [optional] 
**nationality** | **str** |  | [optional] 
**second_lastname** | **str** |  | [optional] 
**second_name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 

## Example

```python
from raassdkpy.models.cip_data import CIPData

# TODO update the JSON string below
json = "{}"
# create an instance of CIPData from a JSON string
cip_data_instance = CIPData.from_json(json)
# print the JSON string representation of the object
print CIPData.to_json()

# convert the object into a dict
cip_data_dict = cip_data_instance.to_dict()
# create an instance of CIPData from a dict
cip_data_form_dict = cip_data.from_dict(cip_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


