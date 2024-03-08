# SetReferenceCodeParamsBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** | internal Id of operation | 
**operation_code** | **str** | short id of operation | 
**amount** | **float** |  | 
**currency** | **str** | Iso 3 for Curency (USD,MXN) | 
**sender_name** | **str** | sender full name | 
**receiver_name** | **str** | receiver full name | 
**network_id** | **str** | ID of cash operator. This can be obtained from Cash Operator | 
**operation_type** | **str** |  | 
**cash_provider** | **str** | can be (Numi, Greendot, Inpamex, NumiCashDelivery, Incomm) and it&#39;s obtained from Cash Network. | 

## Example

```python
from raassdkpyv2.models.set_reference_code_params_base import SetReferenceCodeParamsBase

# TODO update the JSON string below
json = "{}"
# create an instance of SetReferenceCodeParamsBase from a JSON string
set_reference_code_params_base_instance = SetReferenceCodeParamsBase.from_json(json)
# print the JSON string representation of the object
print SetReferenceCodeParamsBase.to_json()

# convert the object into a dict
set_reference_code_params_base_dict = set_reference_code_params_base_instance.to_dict()
# create an instance of SetReferenceCodeParamsBase from a dict
set_reference_code_params_base_form_dict = set_reference_code_params_base.from_dict(set_reference_code_params_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


