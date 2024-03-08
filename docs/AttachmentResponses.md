# AttachmentResponses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_document** | **object** |  | [optional] 
**selfies** | **object** |  | [optional] 
**photo_id_file_name** | **object** |  | [optional] 

## Example

```python
from raassdkpyv2.models.attachment_responses import AttachmentResponses

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentResponses from a JSON string
attachment_responses_instance = AttachmentResponses.from_json(json)
# print the JSON string representation of the object
print AttachmentResponses.to_json()

# convert the object into a dict
attachment_responses_dict = attachment_responses_instance.to_dict()
# create an instance of AttachmentResponses from a dict
attachment_responses_form_dict = attachment_responses.from_dict(attachment_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


