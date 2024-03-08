# raassdkpyv2.DefaultApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_card**](DefaultApi.md#add_card) | **POST** /user/funding/source/card/add/{userToken} | 
[**create_contact**](DefaultApi.md#create_contact) | **POST** /user/contacts/{userToken} | 
[**delete_payment_method**](DefaultApi.md#delete_payment_method) | **POST** /user/funding/source/delete/{userToken} | 
[**get_cip_info**](DefaultApi.md#get_cip_info) | **GET** /cip/process/{phoneNumber} | 
[**get_destination_sof_for_requet_money_operation**](DefaultApi.md#get_destination_sof_for_requet_money_operation) | **GET** /user/funding/source/request-money/{userToken} | 
[**get_operation**](DefaultApi.md#get_operation) | **GET** /user/operations/detail/{id} | 
[**get_operation_status**](DefaultApi.md#get_operation_status) | **GET** /user/operations/status/{userToken}/{operationId} | 
[**get_payment_method**](DefaultApi.md#get_payment_method) | **GET** /user/funding/source/get-payment-method/{userToken} | 
[**get_payment_method_v2**](DefaultApi.md#get_payment_method_v2) | **GET** /user/funding/source/get-payment-method-v2/{userToken} | 
[**get_user_token**](DefaultApi.md#get_user_token) | **POST** /auth/get-user-token | 
[**list_contacts**](DefaultApi.md#list_contacts) | **GET** /user/contacts/{userToken} | 
[**register_user_v2**](DefaultApi.md#register_user_v2) | **POST** /auth/register-user-v2 | 
[**request_v2**](DefaultApi.md#request_v2) | **POST** /user/operations/request-money-v2/{userToken} | 
[**updated_contact**](DefaultApi.md#updated_contact) | **PUT** /user/contacts/{userToken} | 


# **add_card**
> AddPaymentMethodResponse add_card(user_token, add_card_partner_params)



adds a card to subscriber's source of funding

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.add_card_partner_params import AddCardPartnerParams
from raassdkpyv2.models.add_payment_method_response import AddPaymentMethodResponse
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    add_card_partner_params = raassdkpyv2.AddCardPartnerParams() # AddCardPartnerParams | 

    try:
        api_response = api_instance.add_card(user_token, add_card_partner_params)
        print("The response of DefaultApi->add_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_card: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **add_card_partner_params** | [**AddCardPartnerParams**](AddCardPartnerParams.md)|  | 

### Return type

[**AddPaymentMethodResponse**](AddPaymentMethodResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> create_contact(user_token, create_contact_request_params_partner)



Create a contact for a user  SCOPES:       - partner:      ASK partners only.      - partner_send: SEND partners only.      - partner_dual: ASK+SEND partners only.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.create_contact_request_params_partner import CreateContactRequestParamsPartner
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.
    create_contact_request_params_partner = raassdkpyv2.CreateContactRequestParamsPartner() # CreateContactRequestParamsPartner | 

    try:
        api_instance.create_contact(user_token, create_contact_request_params_partner)
    except Exception as e:
        print("Exception when calling DefaultApi->create_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. | 
 **create_contact_request_params_partner** | [**CreateContactRequestParamsPartner**](CreateContactRequestParamsPartner.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  |  -  |
**422** | Validation Failed |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> delete_payment_method(user_token, payment_method_id)



removes a payment method

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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | 

    try:
        api_instance.delete_payment_method(user_token, payment_method_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **payment_method_id** | **str**|  | 

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
**204** | No content |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cip_info**
> PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC get_cip_info(phone_number)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac import PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_response = api_instance.get_cip_info(phone_number)
        print("The response of DefaultApi->get_cip_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_cip_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 

### Return type

[**PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC**](PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC.md)

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

# **get_destination_sof_for_requet_money_operation**
> List[SourceOfFunding] get_destination_sof_for_requet_money_operation(user_token, source_country=source_country, destination_country=destination_country)



gets destination sources of funding for request funds

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.source_of_funding import SourceOfFunding
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    source_country = 'source_country_example' # str |  (optional)
    destination_country = 'destination_country_example' # str |  (optional)

    try:
        api_response = api_instance.get_destination_sof_for_requet_money_operation(user_token, source_country=source_country, destination_country=destination_country)
        print("The response of DefaultApi->get_destination_sof_for_requet_money_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_destination_sof_for_requet_money_operation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **source_country** | **str**|  | [optional] 
 **destination_country** | **str**|  | [optional] 

### Return type

[**List[SourceOfFunding]**](SourceOfFunding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation**
> OperationDetail get_operation(id)



Gets operation detail by id

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.operation_detail import OperationDetail
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    id = 'id_example' # str | Operation Id

    try:
        api_response = api_instance.get_operation(id)
        print("The response of DefaultApi->get_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_operation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Operation Id | 

### Return type

[**OperationDetail**](OperationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_status**
> str get_operation_status(user_token, operation_id)



Gets operation status

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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    operation_id = 'operation_id_example' # str | 

    try:
        api_response = api_instance.get_operation_status(user_token, operation_id)
        print("The response of DefaultApi->get_operation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_operation_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **operation_id** | **str**|  | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> RaaSPaymentMethod get_payment_method(user_token, number=number)



Retrieve a payment method by number

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.raa_s_payment_method import RaaSPaymentMethod
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    number = '' # str |  (optional) (default to '')

    try:
        api_response = api_instance.get_payment_method(user_token, number=number)
        print("The response of DefaultApi->get_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **number** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**RaaSPaymentMethod**](RaaSPaymentMethod.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link PaymentMethod} |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_v2**
> RaaSPartnerPaymentMethod get_payment_method_v2(user_token, id=id)



Retrieve a payment method by ID

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.raa_s_partner_payment_method import RaaSPartnerPaymentMethod
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    id = '' # str |  (optional) (default to '')

    try:
        api_response = api_instance.get_payment_method_v2(user_token, id=id)
        print("The response of DefaultApi->get_payment_method_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_payment_method_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**RaaSPartnerPaymentMethod**](RaaSPartnerPaymentMethod.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link PaymentMethod} |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_token**
> UserTokenResponse get_user_token(get_user_token_params)



Partner API Token.  User ID.  SCOPES:       - partner:      ASK partners only.      - partner_send: SEND partners only.      - partner_dual: ASK+SEND partners only.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.get_user_token_params import GetUserTokenParams
from raassdkpyv2.models.user_token_response import UserTokenResponse
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    get_user_token_params = raassdkpyv2.GetUserTokenParams() # GetUserTokenParams | {@link GetUserTokenParams}

    try:
        api_response = api_instance.get_user_token(get_user_token_params)
        print("The response of DefaultApi->get_user_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_user_token_params** | [**GetUserTokenParams**](GetUserTokenParams.md)| {@link GetUserTokenParams} | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> List[ContactInfo] list_contacts(user_token)



Retrieve all contacts for a user  SCOPES:       - partner:      ASK partners only.      - partner_send: SEND partners only.      - partner_dual: ASK+SEND partners only.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.contact_info import ContactInfo
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.

    try:
        api_response = api_instance.list_contacts(user_token)
        print("The response of DefaultApi->list_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_contacts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. | 

### Return type

[**List[ContactInfo]**](ContactInfo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact List |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user_v2**
> UserTokenResponse register_user_v2(register_user_params)



Registers Partner user. If user exists, return its id.  SCOPES:   - partner:      ASK partners only.  - partner_dual: ASK+SEND partners only.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.register_user_params import RegisterUserParams
from raassdkpyv2.models.user_token_response import UserTokenResponse
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    register_user_params = raassdkpyv2.RegisterUserParams() # RegisterUserParams | {@link RegisterUserParams}

    try:
        api_response = api_instance.register_user_v2(register_user_params)
        print("The response of DefaultApi->register_user_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->register_user_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_params** | [**RegisterUserParams**](RegisterUserParams.md)| {@link RegisterUserParams} | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_v2**
> PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen request_v2(user_token, request_money_partner_params)



Request money to a contact

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen import PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen
from raassdkpyv2.models.request_money_partner_params import RequestMoneyPartnerParams
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    request_money_partner_params = raassdkpyv2.RequestMoneyPartnerParams() # RequestMoneyPartnerParams | {@link RequestMoneyParams}

    try:
        api_response = api_instance.request_v2(user_token, request_money_partner_params)
        print("The response of DefaultApi->request_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->request_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **request_money_partner_params** | [**RequestMoneyPartnerParams**](RequestMoneyPartnerParams.md)| {@link RequestMoneyParams} | 

### Return type

[**PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen**](PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link RequestMoneyResponse} |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updated_contact**
> updated_contact(user_token, update_contact_request_params)



Update a contact for a user  SCOPES:       - partner:      ASK partners only.      - partner_send: SEND partners only.      - partner_dual: ASK+SEND partners only.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.update_contact_request_params import UpdateContactRequestParams
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
    api_instance = raassdkpyv2.DefaultApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.
    update_contact_request_params = raassdkpyv2.UpdateContactRequestParams() # UpdateContactRequestParams | 

    try:
        api_instance.updated_contact(user_token, update_contact_request_params)
    except Exception as e:
        print("Exception when calling DefaultApi->updated_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. | 
 **update_contact_request_params** | [**UpdateContactRequestParams**](UpdateContactRequestParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**422** | Validation Failed |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

