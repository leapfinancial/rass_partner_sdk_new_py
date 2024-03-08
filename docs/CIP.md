# CIP


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **bool** |  | [optional] 
**touched** | **bool** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**manual_required** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**documents** | [**List[CIPDocument]**](CIPDocument.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**facematch_sent** | **bool** |  | [optional] 
**facematch_ok** | **bool** |  | [optional] 
**facematch_msg** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.cip import CIP

# TODO update the JSON string below
json = "{}"
# create an instance of CIP from a JSON string
cip_instance = CIP.from_json(json)
# print the JSON string representation of the object
print CIP.to_json()

# convert the object into a dict
cip_dict = cip_instance.to_dict()
# create an instance of CIP from a dict
cip_form_dict = cip.from_dict(cip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


