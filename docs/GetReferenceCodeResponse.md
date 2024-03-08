# GetReferenceCodeResponse

Code: string with Code Reference Id, will be used for Get Reference Information  ExpirationDate: date ultil Code expires (YYYY/MM/DD)  CodeType: Barcode or QR

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**expiration_date** | **str** |  | 
**code_type** | **object** |  | 
**status** | **str** |  | 
**status_message** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.get_reference_code_response import GetReferenceCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferenceCodeResponse from a JSON string
get_reference_code_response_instance = GetReferenceCodeResponse.from_json(json)
# print the JSON string representation of the object
print GetReferenceCodeResponse.to_json()

# convert the object into a dict
get_reference_code_response_dict = get_reference_code_response_instance.to_dict()
# create an instance of GetReferenceCodeResponse from a dict
get_reference_code_response_form_dict = get_reference_code_response.from_dict(get_reference_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


