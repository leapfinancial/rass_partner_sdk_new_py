# QuickAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**is_most_frequent** | **bool** | This config is to display the most frequent quick amount in the UI | [optional] 
**exchange** | **float** |  | 
**currency_code_src** | **str** |  | 
**currency_code_dest** | **str** |  | 

## Example

```python
from raassdkpy.models.quick_amount import QuickAmount

# TODO update the JSON string below
json = "{}"
# create an instance of QuickAmount from a JSON string
quick_amount_instance = QuickAmount.from_json(json)
# print the JSON string representation of the object
print QuickAmount.to_json()

# convert the object into a dict
quick_amount_dict = quick_amount_instance.to_dict()
# create an instance of QuickAmount from a dict
quick_amount_form_dict = quick_amount.from_dict(quick_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


