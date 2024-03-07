# RequestMoneyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**OperationData**](OperationData.md) |  | 
**link** | **str** |  | 

## Example

```python
from raassdkpy.models.request_money_response import RequestMoneyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMoneyResponse from a JSON string
request_money_response_instance = RequestMoneyResponse.from_json(json)
# print the JSON string representation of the object
print RequestMoneyResponse.to_json()

# convert the object into a dict
request_money_response_dict = request_money_response_instance.to_dict()
# create an instance of RequestMoneyResponse from a dict
request_money_response_form_dict = request_money_response.from_dict(request_money_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


