# EventSystem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | 
**event_type** | **str** |  | 

## Example

```python
from raassdkpyv2.models.event_system import EventSystem

# TODO update the JSON string below
json = "{}"
# create an instance of EventSystem from a JSON string
event_system_instance = EventSystem.from_json(json)
# print the JSON string representation of the object
print EventSystem.to_json()

# convert the object into a dict
event_system_dict = event_system_instance.to_dict()
# create an instance of EventSystem from a dict
event_system_form_dict = event_system.from_dict(event_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


