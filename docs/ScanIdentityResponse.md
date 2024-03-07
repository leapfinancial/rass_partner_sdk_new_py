# ScanIdentityResponse

After scan using an non sync engine, API will return this object A client has to pull the data from this object's pull_url  until the status is a ScanIdentityResponse or \"error\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** | If it&#39;s async the client has to pull the data from this url | 
**estimated_time** | **float** | Estimated time in seconds. | [optional] 
**method** | **str** | What scan engine was used | [optional] 
**pull_url** | **str** | Url to pull the data. If the type&#x3D;sync you have perform interval pulls to this url in order to monitor the status | [optional] 
**data** | [**BaseIdentity**](BaseIdentity.md) |  | [optional] 
**attachment_responses** | [**AttachmentResponses**](AttachmentResponses.md) |  | [optional] 

## Example

```python
from raassdkpy.models.scan_identity_response import ScanIdentityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScanIdentityResponse from a JSON string
scan_identity_response_instance = ScanIdentityResponse.from_json(json)
# print the JSON string representation of the object
print ScanIdentityResponse.to_json()

# convert the object into a dict
scan_identity_response_dict = scan_identity_response_instance.to_dict()
# create an instance of ScanIdentityResponse from a dict
scan_identity_response_form_dict = scan_identity_response.from_dict(scan_identity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


