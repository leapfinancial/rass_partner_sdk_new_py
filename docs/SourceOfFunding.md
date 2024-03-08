# SourceOfFunding

simplifies delivered response for sources of funding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_primary** | **bool** | Subscriber&#39;s main source of funding | [optional] 
**account_number** | **str** | Bank account number | 
**bank_entity_number** | **str** |  | 
**type** | **str** | Source of funding type: MobileWallet|BankAccount|DebitCard|CreditCard|CashLoadLocaion|CashPayoutLocation|MTOLoad|None|StorePay\&quot; | 
**expiration_date** | **str** | Credit/Debit card expiration date | 
**expiration_month** | **str** | Credit/Debit card expiration month | 
**expiration_year** | **str** | Credit/Debit card expiration year | 
**card_type** | **str** | Card type: Credit|Debit | 
**number** | **str** | Credit/Debit card number | 
**name** | **str** | Credit/Debit card holder name. Account name. | [optional] 
**token_data** | **str** | Tokenized card data. | 
**card_network** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.source_of_funding import SourceOfFunding

# TODO update the JSON string below
json = "{}"
# create an instance of SourceOfFunding from a JSON string
source_of_funding_instance = SourceOfFunding.from_json(json)
# print the JSON string representation of the object
print SourceOfFunding.to_json()

# convert the object into a dict
source_of_funding_dict = source_of_funding_instance.to_dict()
# create an instance of SourceOfFunding from a dict
source_of_funding_form_dict = source_of_funding.from_dict(source_of_funding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


