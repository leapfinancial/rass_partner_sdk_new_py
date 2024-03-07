# ReplaceCardParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** |  | 
**op_plat_id** | **str** |  | 

## Example

```python
from raassdkpy.models.replace_card_params import ReplaceCardParams

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceCardParams from a JSON string
replace_card_params_instance = ReplaceCardParams.from_json(json)
# print the JSON string representation of the object
print ReplaceCardParams.to_json()

# convert the object into a dict
replace_card_params_dict = replace_card_params_instance.to_dict()
# create an instance of ReplaceCardParams from a dict
replace_card_params_form_dict = replace_card_params.from_dict(replace_card_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


