# CorridorDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**source_payment_method_type** | [**AvailablePaymentMethods**](AvailablePaymentMethods.md) |  | 
**destination_payment_method_type** | [**AvailablePaymentMethods**](AvailablePaymentMethods.md) |  | 
**lower_limit** | **float** |  | 
**upper_limit** | **float** |  | 
**fees** | **object** |  | 
**corridor_requirements** | **object** |  | 
**is_active** | **bool** |  | 
**source_country** | **str** |  | 
**destination_country** | **str** |  | 

## Example

```python
from raassdkpy.models.corridor_dto import CorridorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CorridorDTO from a JSON string
corridor_dto_instance = CorridorDTO.from_json(json)
# print the JSON string representation of the object
print CorridorDTO.to_json()

# convert the object into a dict
corridor_dto_dict = corridor_dto_instance.to_dict()
# create an instance of CorridorDTO from a dict
corridor_dto_form_dict = corridor_dto.from_dict(corridor_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


