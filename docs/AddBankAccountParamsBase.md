# AddBankAccountParamsBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | payment method name: p.e. HSBC-1111 | 
**account_number** | **str** |  | 
**bank_account_type** | **str** | Bank account type | 
**bank_entity_number** | **str** |  | 
**is_primary** | **bool** | Main payment method? | 
**country** | **str** |  | 
**currency** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.add_bank_account_params_base import AddBankAccountParamsBase

# TODO update the JSON string below
json = "{}"
# create an instance of AddBankAccountParamsBase from a JSON string
add_bank_account_params_base_instance = AddBankAccountParamsBase.from_json(json)
# print the JSON string representation of the object
print AddBankAccountParamsBase.to_json()

# convert the object into a dict
add_bank_account_params_base_dict = add_bank_account_params_base_instance.to_dict()
# create an instance of AddBankAccountParamsBase from a dict
add_bank_account_params_base_form_dict = add_bank_account_params_base.from_dict(add_bank_account_params_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


