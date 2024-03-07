# ExchangeRateDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**currency_code_dest** | **str** |  | 
**currency_code_src** | **str** |  | 
**exchange_rate** | **float** |  | 
**exchange_rate_updated_at** | **str** |  | 

## Example

```python
from raassdkpy.models.exchange_rate_dto import ExchangeRateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRateDTO from a JSON string
exchange_rate_dto_instance = ExchangeRateDTO.from_json(json)
# print the JSON string representation of the object
print ExchangeRateDTO.to_json()

# convert the object into a dict
exchange_rate_dto_dict = exchange_rate_dto_instance.to_dict()
# create an instance of ExchangeRateDTO from a dict
exchange_rate_dto_form_dict = exchange_rate_dto.from_dict(exchange_rate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


