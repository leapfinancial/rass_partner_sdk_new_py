# raassdkpyv2.FileApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_documents**](FileApi.md#upload_documents) | **POST** /cip/documents/{phoneNumber} | 
[**upload_proof_of_life**](FileApi.md#upload_proof_of_life) | **POST** /cip/proof-of-life/{phoneNumber} | 


# **upload_documents**
> ScanIdentityResponse upload_documents(phone_number)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.scan_identity_response import ScanIdentityResponse
from raassdkpyv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = raassdkpyv2.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with raassdkpyv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = raassdkpyv2.FileApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_response = api_instance.upload_documents(phone_number)
        print("The response of FileApi->upload_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->upload_documents: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 

### Return type

[**ScanIdentityResponse**](ScanIdentityResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_proof_of_life**
> upload_proof_of_life(phone_number)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = raassdkpyv2.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with raassdkpyv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = raassdkpyv2.FileApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_instance.upload_proof_of_life(phone_number)
    except Exception as e:
        print("Exception when calling FileApi->upload_proof_of_life: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

