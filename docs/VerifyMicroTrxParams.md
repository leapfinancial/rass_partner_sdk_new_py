# VerifyMicroTrxParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**card_id** | **str** |  | 

## Example

```python
from raassdkpy.models.verify_micro_trx_params import VerifyMicroTrxParams

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyMicroTrxParams from a JSON string
verify_micro_trx_params_instance = VerifyMicroTrxParams.from_json(json)
# print the JSON string representation of the object
print VerifyMicroTrxParams.to_json()

# convert the object into a dict
verify_micro_trx_params_dict = verify_micro_trx_params_instance.to_dict()
# create an instance of VerifyMicroTrxParams from a dict
verify_micro_trx_params_form_dict = verify_micro_trx_params.from_dict(verify_micro_trx_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


