# CashLocation

id: Unique Identifier of CashLocation  enable: Identify if location is enabled  cashOperatorId: Id of operator associated  name: Name of Location  addressLine1: Address  addressLine2: Address  state: State code  city:  City Code  longitude: Expression to include longitude value  latitude: Expression to include latitude value  phone: Telephone number  image: URL of image to identify this Location

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**enable** | **str** |  | 
**cash_operator_id** | **str** |  | 
**name** | **str** |  | 
**address_line1** | **str** |  | 
**address_line2** | **str** |  | 
**state** | **str** |  | 
**city** | **str** |  | 
**longitude** | **str** |  | 
**latitude** | **str** |  | 
**phone** | **str** |  | 
**image** | **str** |  | 

## Example

```python
from raassdkpyv2.models.cash_location import CashLocation

# TODO update the JSON string below
json = "{}"
# create an instance of CashLocation from a JSON string
cash_location_instance = CashLocation.from_json(json)
# print the JSON string representation of the object
print CashLocation.to_json()

# convert the object into a dict
cash_location_dict = cash_location_instance.to_dict()
# create an instance of CashLocation from a dict
cash_location_form_dict = cash_location.from_dict(cash_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


