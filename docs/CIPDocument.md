# CIPDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**sides** | **float** |  | [optional] 
**has_mrz** | **bool** |  | [optional] 
**data** | [**CIPData**](CIPData.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from raassdkpyv2.models.cip_document import CIPDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CIPDocument from a JSON string
cip_document_instance = CIPDocument.from_json(json)
# print the JSON string representation of the object
print CIPDocument.to_json()

# convert the object into a dict
cip_document_dict = cip_document_instance.to_dict()
# create an instance of CIPDocument from a dict
cip_document_form_dict = cip_document.from_dict(cip_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


