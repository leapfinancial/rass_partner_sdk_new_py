# PlaidBankValidationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**access_token** | **str** |  | 
**item_id** | **str** |  | 
**account_type** | **str** |  | 
**account_sub_type** | **str** |  | 
**account_name** | **str** |  | 
**account_number** | **str** |  | 
**account_routing** | **str** |  | 
**bank_name** | **str** |  | 

## Example

```python
from raassdkpy.models.plaid_bank_validation_response import PlaidBankValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaidBankValidationResponse from a JSON string
plaid_bank_validation_response_instance = PlaidBankValidationResponse.from_json(json)
# print the JSON string representation of the object
print PlaidBankValidationResponse.to_json()

# convert the object into a dict
plaid_bank_validation_response_dict = plaid_bank_validation_response_instance.to_dict()
# create an instance of PlaidBankValidationResponse from a dict
plaid_bank_validation_response_form_dict = plaid_bank_validation_response.from_dict(plaid_bank_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


