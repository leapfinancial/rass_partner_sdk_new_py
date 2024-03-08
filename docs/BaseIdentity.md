# BaseIdentity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surname** | **str** |  | [optional] 
**names** | **str** |  | [optional] 
**dob** | **datetime** |  | [optional] 
**dob_raw** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**id_country** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**county** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**exp_date** | **datetime** |  | [optional] 
**exp_date_raw** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**doc_type** | **str** |  | [optional] 
**nationality** | **str** |  | [optional] 
**id_validated** | **str** |  | [optional] 
**id_name** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**county_code** | **str** |  | [optional] 
**section_code** | **str** |  | [optional] 
**locality_code** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**second_lastname** | **str** |  | [optional] 
**second_name** | **object** |  | [optional] 
**marital_status** | **str** |  | [optional] 
**maiden_name** | **str** |  | [optional] 
**third_name** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 

## Example

```python
from raassdkpyv2.models.base_identity import BaseIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of BaseIdentity from a JSON string
base_identity_instance = BaseIdentity.from_json(json)
# print the JSON string representation of the object
print BaseIdentity.to_json()

# convert the object into a dict
base_identity_dict = base_identity_instance.to_dict()
# create an instance of BaseIdentity from a dict
base_identity_form_dict = base_identity.from_dict(base_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


