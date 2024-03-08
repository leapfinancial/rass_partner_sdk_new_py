# OperationDetailResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenantfee** | **float** |  | [optional] 
**ignored_data** | [**IgnoredOperationData**](IgnoredOperationData.md) |  | [optional] 
**is_ignored** | **bool** |  | [optional] 
**attribution_link** | **str** |  | [optional] 
**to_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**from_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**has_reference_code** | **bool** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**destination_fee** | **float** |  | [optional] 
**transaction_fee** | **float** |  | [optional] 
**source_fee** | **float** |  | [optional] 
**destination_payment_method** | [**PaymentMethodResponse**](PaymentMethodResponse.md) |  | [optional] 
**source_payment_method** | [**PaymentMethodResponse**](PaymentMethodResponse.md) |  | [optional] 
**recipient_currency** | **str** |  | [optional] 
**sender_currency** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**show_warning_screen** | **bool** |  | 
**sender_amount** | **float** |  | [optional] 
**recipient_amout** | **float** |  | 
**code** | **str** |  | 
**reason** | **str** |  | [optional] 
**mobile_status** | **str** |  | [optional] 
**status_details** | **str** |  | [optional] 
**status** | **str** |  | 
**amount** | **float** |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**correlation_id** | **str** |  | 
**plat_id** | **str** |  | [optional] 
**id** | **str** |  | 

## Example

```python
from raassdkpyv2.models.operation_detail_response import OperationDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDetailResponse from a JSON string
operation_detail_response_instance = OperationDetailResponse.from_json(json)
# print the JSON string representation of the object
print OperationDetailResponse.to_json()

# convert the object into a dict
operation_detail_response_dict = operation_detail_response_instance.to_dict()
# create an instance of OperationDetailResponse from a dict
operation_detail_response_form_dict = operation_detail_response.from_dict(operation_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


