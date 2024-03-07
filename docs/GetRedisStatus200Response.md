# GetRedisStatus200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**status** | **bool** |  | 

## Example

```python
from raassdkpy.models.get_redis_status200_response import GetRedisStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRedisStatus200Response from a JSON string
get_redis_status200_response_instance = GetRedisStatus200Response.from_json(json)
# print the JSON string representation of the object
print GetRedisStatus200Response.to_json()

# convert the object into a dict
get_redis_status200_response_dict = get_redis_status200_response_instance.to_dict()
# create an instance of GetRedisStatus200Response from a dict
get_redis_status200_response_form_dict = get_redis_status200_response.from_dict(get_redis_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


