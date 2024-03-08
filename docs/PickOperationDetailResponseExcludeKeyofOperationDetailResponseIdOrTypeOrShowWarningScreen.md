# PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen

From T, pick a set of properties whose keys are in the union K

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**plat_id** | **str** |  | [optional] 
**correlation_id** | **str** |  | 
**created_at** | **datetime** |  | 
**amount** | **float** |  | 
**status** | **str** |  | 
**status_details** | **str** |  | [optional] 
**mobile_status** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**code** | **str** |  | 
**recipient_amout** | **float** |  | 
**sender_amount** | **float** |  | [optional] 
**sender_currency** | **str** |  | [optional] 
**recipient_currency** | **str** |  | [optional] 
**source_payment_method** | [**PaymentMethodResponse**](PaymentMethodResponse.md) |  | [optional] 
**destination_payment_method** | [**PaymentMethodResponse**](PaymentMethodResponse.md) |  | [optional] 
**source_fee** | **float** |  | [optional] 
**transaction_fee** | **float** |  | [optional] 
**destination_fee** | **float** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**has_reference_code** | **bool** |  | [optional] 
**from_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**to_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**attribution_link** | **str** |  | [optional] 
**is_ignored** | **bool** |  | [optional] 
**ignored_data** | [**IgnoredOperationData**](IgnoredOperationData.md) |  | [optional] 
**tenantfee** | **float** |  | [optional] 

## Example

```python
from raassdkpyv2.models.pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen import PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen

# TODO update the JSON string below
json = "{}"
# create an instance of PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen from a JSON string
pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen_instance = PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen.from_json(json)
# print the JSON string representation of the object
print PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen.to_json()

# convert the object into a dict
pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen_dict = pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen_instance.to_dict()
# create an instance of PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen from a dict
pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen_form_dict = pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen.from_dict(pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


