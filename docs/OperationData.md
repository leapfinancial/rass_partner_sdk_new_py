# OperationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**status** | **str** |  | 
**code** | **str** |  | 
**created_by** | **str** |  | 
**correlation_id** | **str** |  | 
**sender** | [**OperationContactData**](OperationContactData.md) |  | 
**recipient** | [**OperationContactData**](OperationContactData.md) |  | 
**source_payment_method** | **object** |  | 
**destination_payment_method** | **object** |  | 
**amount** | **float** |  | 
**currency** | **str** |  | 
**sender_amount** | **float** |  | 
**sender_currency** | **str** |  | 
**recipient_amount** | **float** |  | 
**recipient_currency** | **str** |  | 
**exchange_rate** | **float** |  | 
**fee_payer** | **str** |  | 

## Example

```python
from raassdkpy.models.operation_data import OperationData

# TODO update the JSON string below
json = "{}"
# create an instance of OperationData from a JSON string
operation_data_instance = OperationData.from_json(json)
# print the JSON string representation of the object
print OperationData.to_json()

# convert the object into a dict
operation_data_dict = operation_data_instance.to_dict()
# create an instance of OperationData from a dict
operation_data_form_dict = operation_data.from_dict(operation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


