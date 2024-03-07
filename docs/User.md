# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**second_last_name** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**place_id** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**address_description** | **str** | Here we save some description about direcction for example: Local 304, next to the grocery store | [optional] 
**gender** | **str** |  | [optional] 
**dob** | **datetime** |  | [optional] 
**country_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**phone_verified** | **bool** |  | [optional] 
**cip** | [**CIP**](CIP.md) |  | [optional] 
**first_time** | **bool** |  | [optional] 
**country_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**birth_state** | **str** |  | [optional] 
**place_detail** | **str** | Here we save the google maps places address details | [optional] 
**pincode** | **str** | Pincode - used to validate user in Raas | [optional] 
**has_pincode** | **bool** |  | [optional] 
**password** | **str** | Used to store Numi Plat pincode. It&#39;s not used to validate  user in Raas | [optional] 
**phone_info** | [**IPhoneInfo**](IPhoneInfo.md) |  | [optional] 
**tenant_id** | **str** |  | 
**tenant_code** | **str** |  | 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**profile_picture_url** | **str** |  | [optional] 
**custom_country_code** | **str** |  | [optional] 
**facebook_public_user_name** | **str** |  | [optional] 
**instagram_public_user_name** | **str** |  | [optional] 
**account_code** | **str** |  | [optional] 

## Example

```python
from raassdkpy.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


