# CashOperators

id: Unique Identifier of CashOperator  networkId: Unique Identifier of the CashOperator’s Store Chain.  ExternalId??  network: List of Networks associated to this operator  country: Country code of this Operator  name: Name of this operator  imageUrl: URL of image to identify this operator  location: List of Locatios associated to this operator  cashAccountType:  Enum that identifies the type of network {CREDIT, PREPAID}   imageCircleUrl: URL of image to identify this operator (circle shape)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**external_id** | **str** |  | 
**network** | [**List[CashNetwork]**](CashNetwork.md) |  | 
**country** | **str** |  | 
**name** | **str** |  | 
**image_url** | **str** |  | 
**location** | [**List[CashLocation]**](CashLocation.md) |  | 
**cash_account_type** | **object** |  | 
**image_circle_url** | **str** |  | 

## Example

```python
from raassdkpy.models.cash_operators import CashOperators

# TODO update the JSON string below
json = "{}"
# create an instance of CashOperators from a JSON string
cash_operators_instance = CashOperators.from_json(json)
# print the JSON string representation of the object
print CashOperators.to_json()

# convert the object into a dict
cash_operators_dict = cash_operators_instance.to_dict()
# create an instance of CashOperators from a dict
cash_operators_form_dict = cash_operators.from_dict(cash_operators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


