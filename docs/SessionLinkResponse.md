# SessionLinkResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | 
**status** | **str** |  | [optional] 
**status_detail** | **str** |  | [optional] 

## Example

```python
from raassdkpy.models.session_link_response import SessionLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionLinkResponse from a JSON string
session_link_response_instance = SessionLinkResponse.from_json(json)
# print the JSON string representation of the object
print SessionLinkResponse.to_json()

# convert the object into a dict
session_link_response_dict = session_link_response_instance.to_dict()
# create an instance of SessionLinkResponse from a dict
session_link_response_form_dict = session_link_response.from_dict(session_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


