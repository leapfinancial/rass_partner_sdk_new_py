# raassdkpyv2.PartnerFullApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pin**](PartnerFullApi.md#create_pin) | **POST** /user/pin | 
[**get_available_operation_type**](PartnerFullApi.md#get_available_operation_type) | **GET** /user/corridors/available-operations/{userToken} | 
[**get_available_payment_methods**](PartnerFullApi.md#get_available_payment_methods) | **GET** /user/corridors/available-methods/{userToken} | 
[**get_cip_info**](PartnerFullApi.md#get_cip_info) | **GET** /cip/process/{phoneNumber} | 
[**get_corridors**](PartnerFullApi.md#get_corridors) | **GET** /user/corridors | 
[**get_exchange_rates**](PartnerFullApi.md#get_exchange_rates) | **GET** /user/exchange-rates/exchange-rates | 
[**get_in_and_out_operations**](PartnerFullApi.md#get_in_and_out_operations) | **GET** /user/operations/in-out/{userToken} | 
[**get_operation_quote**](PartnerFullApi.md#get_operation_quote) | **POST** /user/operations/quotation/{userToken} | 
[**get_profile**](PartnerFullApi.md#get_profile) | **GET** /user/profile/{phone} | 
[**perform_level_one**](PartnerFullApi.md#perform_level_one) | **POST** /cip/level/one/{phoneNumber} | 
[**perform_resubmit_upgrade_level**](PartnerFullApi.md#perform_resubmit_upgrade_level) | **POST** /cip/level/resubmit-upgrade | 
[**pre_quote**](PartnerFullApi.md#pre_quote) | **POST** /user/operations/pre-quote/{userToken} | 
[**receive**](PartnerFullApi.md#receive) | **POST** /user/operations/receive-money/{userToken} | 
[**replace_payment_method**](PartnerFullApi.md#replace_payment_method) | **POST** /user/operations/replace-payment-method/{userId} | 
[**request_otp**](PartnerFullApi.md#request_otp) | **POST** /auth/request-otp | 
[**send**](PartnerFullApi.md#send) | **POST** /user/operations/send-money/{userToken} | 
[**set_alternate_cip**](PartnerFullApi.md#set_alternate_cip) | **POST** /cip/alternate/{phoneNumber} | 
[**set_level_two**](PartnerFullApi.md#set_level_two) | **POST** /cip/level/two/{phoneNumber} | 
[**set_trusted_level_two**](PartnerFullApi.md#set_trusted_level_two) | **POST** /cip/level/two/{phoneNumber}/trusted | 
[**update_profile**](PartnerFullApi.md#update_profile) | **PUT** /user/profile/{phone} | 
[**upload_documents**](PartnerFullApi.md#upload_documents) | **POST** /cip/documents/{phoneNumber} | 
[**upload_proof_of_life**](PartnerFullApi.md#upload_proof_of_life) | **POST** /cip/proof-of-life/{phoneNumber} | 
[**validate_otp**](PartnerFullApi.md#validate_otp) | **POST** /auth/validate-otp | 
[**validate_pin_code**](PartnerFullApi.md#validate_pin_code) | **POST** /user/validate-pincode | 


# **create_pin**
> create_pin(set_pincode_params_partner)



Creates a pincode for the user.  The pincode must be 6 digits long and only numeric characters are allowed.  If the user already has a pincode, an error will be returned.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.set_pincode_params_partner import SetPincodeParamsPartner
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    set_pincode_params_partner = raassdkpyv2.SetPincodeParamsPartner() # SetPincodeParamsPartner | 

    try:
        api_instance.create_pin(set_pincode_params_partner)
    except Exception as e:
        print("Exception when calling PartnerFullApi->create_pin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_pincode_params_partner** | [**SetPincodeParamsPartner**](SetPincodeParamsPartner.md)|  | 

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
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_operation_type**
> List[str] get_available_operation_type(user_token, destination_country=destination_country)



Gets available operation types by user country (as source country) and destination country. A corridor is a way to configure available operation between two subscribers.  NOTICE: if an operation is RequestFunds from A to B, you may search for a SendFunds from B to A to determine if operation is available. Probabily you'll not find a RequestFunds option as such.

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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    user_token = 'user_token_example' # str | 
    destination_country = 'destination_country_example' # str | ISO 3166 2-alpha (optional)

    try:
        api_response = api_instance.get_available_operation_type(user_token, destination_country=destination_country)
        print("The response of PartnerFullApi->get_available_operation_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->get_available_operation_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **destination_country** | **str**| ISO 3166 2-alpha | [optional] 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | string[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_payment_methods**
> List[str] get_available_payment_methods(user_token, destination_country=destination_country, operation_type=operation_type)



Gets available payment method types by source country, destination country and operation type. A corridor is a way to configure available operation between two subscribers.

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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    user_token = 'user_token_example' # str | 
    destination_country = 'destination_country_example' # str | ISO 3166 2-alpha (optional)
    operation_type = 'SendFunds' # str | SendFunds | RequestFunds (optional) (default to 'SendFunds')

    try:
        api_response = api_instance.get_available_payment_methods(user_token, destination_country=destination_country, operation_type=operation_type)
        print("The response of PartnerFullApi->get_available_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->get_available_payment_methods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **destination_country** | **str**| ISO 3166 2-alpha | [optional] 
 **operation_type** | **str**| SendFunds | RequestFunds | [optional] [default to &#39;SendFunds&#39;]

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | string[] |  -  |
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_response = api_instance.get_cip_info(phone_number)
        print("The response of PartnerFullApi->get_cip_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->get_cip_info: %s\n" % e)
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

# **get_corridors**
> List[CorridorDTO] get_corridors(source_country=source_country, destination_country=destination_country, operation_type=operation_type)



Gets corridors by source country, destination country and operation type. A corridor is a way to configure available operation between two subscribers.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.corridor_dto import CorridorDTO
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    source_country = 'source_country_example' # str | ISO 3166 2-alpha (optional)
    destination_country = 'destination_country_example' # str | ISO 3166 2-alpha (optional)
    operation_type = 'SendFunds' # str | SendFunds | RequestFunds (optional) (default to 'SendFunds')

    try:
        api_response = api_instance.get_corridors(source_country=source_country, destination_country=destination_country, operation_type=operation_type)
        print("The response of PartnerFullApi->get_corridors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->get_corridors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_country** | **str**| ISO 3166 2-alpha | [optional] 
 **destination_country** | **str**| ISO 3166 2-alpha | [optional] 
 **operation_type** | **str**| SendFunds | RequestFunds | [optional] [default to &#39;SendFunds&#39;]

### Return type

[**List[CorridorDTO]**](CorridorDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CorridorDTO[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_rates**
> List[ExchangeRateDTO] get_exchange_rates(currency_code_src=currency_code_src, currency_code_dest=currency_code_dest)



Gets exchange rates between currencies

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.exchange_rate_dto import ExchangeRateDTO
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    currency_code_src = 'currency_code_src_example' # str | ISO 4217 3-alpha (optional)
    currency_code_dest = 'currency_code_dest_example' # str | ISO 4217 3-alpha (optional)

    try:
        api_response = api_instance.get_exchange_rates(currency_code_src=currency_code_src, currency_code_dest=currency_code_dest)
        print("The response of PartnerFullApi->get_exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->get_exchange_rates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code_src** | **str**| ISO 4217 3-alpha | [optional] 
 **currency_code_dest** | **str**| ISO 4217 3-alpha | [optional] 

### Return type

[**List[ExchangeRateDTO]**](ExchangeRateDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExchangeRate[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_in_and_out_operations**
> List[OperationDetailResponse] get_in_and_out_operations(user_token, to_phone_number=to_phone_number)



Return all the in and outs operations for an user given his userId

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.operation_detail_response import OperationDetailResponse
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    user_token = 'user_token_example' # str | 
    to_phone_number = 'to_phone_number_example' # str |  (optional)

    try:
        api_response = api_instance.get_in_and_out_operations(user_token, to_phone_number=to_phone_number)
        print("The response of PartnerFullApi->get_in_and_out_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->get_in_and_out_operations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **to_phone_number** | **str**|  | [optional] 

### Return type

[**List[OperationDetailResponse]**](OperationDetailResponse.md)

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

# **get_operation_quote**
> RaasQuoteTransactionResponse get_operation_quote(user_token, quote_transaction_base)



 Retrieve quote for the operation

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.quote_transaction_base import QuoteTransactionBase
from raassdkpyv2.models.raas_quote_transaction_response import RaasQuoteTransactionResponse
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    user_token = 'user_token_example' # str | 
    quote_transaction_base = raassdkpyv2.QuoteTransactionBase() # QuoteTransactionBase | {@link QuoteTransactionBase}

    try:
        api_response = api_instance.get_operation_quote(user_token, quote_transaction_base)
        print("The response of PartnerFullApi->get_operation_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->get_operation_quote: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **quote_transaction_base** | [**QuoteTransactionBase**](QuoteTransactionBase.md)| {@link QuoteTransactionBase} | 

### Return type

[**RaasQuoteTransactionResponse**](RaasQuoteTransactionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | quotation data |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> User get_profile(phone)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.user import User
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    phone = 'phone_example' # str | 

    try:
        api_response = api_instance.get_profile(phone)
        print("The response of PartnerFullApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->get_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**404** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_level_one**
> perform_level_one(phone_number, perform_level_one_params)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.perform_level_one_params import PerformLevelOneParams
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    phone_number = 'phone_number_example' # str | 
    perform_level_one_params = raassdkpyv2.PerformLevelOneParams() # PerformLevelOneParams | 

    try:
        api_instance.perform_level_one(phone_number, perform_level_one_params)
    except Exception as e:
        print("Exception when calling PartnerFullApi->perform_level_one: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 
 **perform_level_one_params** | [**PerformLevelOneParams**](PerformLevelOneParams.md)|  | 

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
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_resubmit_upgrade_level**
> perform_resubmit_upgrade_level(perform_resubmit_upgrade_level_params)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.perform_resubmit_upgrade_level_params import PerformResubmitUpgradeLevelParams
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    perform_resubmit_upgrade_level_params = raassdkpyv2.PerformResubmitUpgradeLevelParams() # PerformResubmitUpgradeLevelParams | 

    try:
        api_instance.perform_resubmit_upgrade_level(perform_resubmit_upgrade_level_params)
    except Exception as e:
        print("Exception when calling PartnerFullApi->perform_resubmit_upgrade_level: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perform_resubmit_upgrade_level_params** | [**PerformResubmitUpgradeLevelParams**](PerformResubmitUpgradeLevelParams.md)|  | 

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
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_quote**
> RaasPreQuoteResponse pre_quote(user_token, raas_pre_quote_request)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.raas_pre_quote_request import RaasPreQuoteRequest
from raassdkpyv2.models.raas_pre_quote_response import RaasPreQuoteResponse
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    user_token = 'user_token_example' # str | 
    raas_pre_quote_request = raassdkpyv2.RaasPreQuoteRequest() # RaasPreQuoteRequest | 

    try:
        api_response = api_instance.pre_quote(user_token, raas_pre_quote_request)
        print("The response of PartnerFullApi->pre_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->pre_quote: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **raas_pre_quote_request** | [**RaasPreQuoteRequest**](RaasPreQuoteRequest.md)|  | 

### Return type

[**RaasPreQuoteResponse**](RaasPreQuoteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive**
> receive(user_token, receive_money_params)



Receive funds

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.receive_money_params import ReceiveMoneyParams
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    user_token = 'user_token_example' # str | 
    receive_money_params = raassdkpyv2.ReceiveMoneyParams() # ReceiveMoneyParams | {@link ReceiveMoneyParams}

    try:
        api_instance.receive(user_token, receive_money_params)
    except Exception as e:
        print("Exception when calling PartnerFullApi->receive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **receive_money_params** | [**ReceiveMoneyParams**](ReceiveMoneyParams.md)| {@link ReceiveMoneyParams} | 

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
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_payment_method**
> replace_payment_method(user_id, replace_card_params)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.replace_card_params import ReplaceCardParams
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    user_id = 'user_id_example' # str | 
    replace_card_params = raassdkpyv2.ReplaceCardParams() # ReplaceCardParams | 

    try:
        api_instance.replace_payment_method(user_id, replace_card_params)
    except Exception as e:
        print("Exception when calling PartnerFullApi->replace_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **replace_card_params** | [**ReplaceCardParams**](ReplaceCardParams.md)|  | 

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
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_otp**
> request_otp(request_otp_params)



Request OTP for phone number. The phone number must be registered. Using /register endpoint.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.request_otp_params import RequestOTPParams
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    request_otp_params = raassdkpyv2.RequestOTPParams() # RequestOTPParams | 

    try:
        api_instance.request_otp(request_otp_params)
    except Exception as e:
        print("Exception when calling PartnerFullApi->request_otp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_otp_params** | [**RequestOTPParams**](RequestOTPParams.md)|  | 

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
**200** | Code Sent |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> SendMoneyResponse send(user_token, send_money_params)



Send funds to a requester

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.send_money_params import SendMoneyParams
from raassdkpyv2.models.send_money_response import SendMoneyResponse
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    user_token = 'user_token_example' # str | 
    send_money_params = raassdkpyv2.SendMoneyParams() # SendMoneyParams | {@link SendMoneyParams}

    try:
        api_response = api_instance.send(user_token, send_money_params)
        print("The response of PartnerFullApi->send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->send: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **send_money_params** | [**SendMoneyParams**](SendMoneyParams.md)| {@link SendMoneyParams} | 

### Return type

[**SendMoneyResponse**](SendMoneyResponse.md)

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

# **set_alternate_cip**
> set_alternate_cip(type, phone_number)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.alternate_flow import AlternateFlow
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    type = raassdkpyv2.AlternateFlow() # AlternateFlow | 
    phone_number = 'phone_number_example' # str | 

    try:
        api_instance.set_alternate_cip(type, phone_number)
    except Exception as e:
        print("Exception when calling PartnerFullApi->set_alternate_cip: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**AlternateFlow**](.md)|  | 
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

# **set_level_two**
> set_level_two(phone_number, level_two_params)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.level_two_params import LevelTwoParams
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    phone_number = 'phone_number_example' # str | 
    level_two_params = raassdkpyv2.LevelTwoParams() # LevelTwoParams | 

    try:
        api_instance.set_level_two(phone_number, level_two_params)
    except Exception as e:
        print("Exception when calling PartnerFullApi->set_level_two: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 
 **level_two_params** | [**LevelTwoParams**](LevelTwoParams.md)|  | 

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
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_trusted_level_two**
> set_trusted_level_two(phone_number)



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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_instance.set_trusted_level_two(phone_number)
    except Exception as e:
        print("Exception when calling PartnerFullApi->set_trusted_level_two: %s\n" % e)
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

# **update_profile**
> update_profile(phone, user_update_params)



Updates user profile

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.user_update_params import UserUpdateParams
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    phone = 'phone_example' # str | 
    user_update_params = raassdkpyv2.UserUpdateParams() # UserUpdateParams | 

    try:
        api_instance.update_profile(phone, user_update_params)
    except Exception as e:
        print("Exception when calling PartnerFullApi->update_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **user_update_params** | [**UserUpdateParams**](UserUpdateParams.md)|  | 

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
**404** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_response = api_instance.upload_documents(phone_number)
        print("The response of PartnerFullApi->upload_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerFullApi->upload_documents: %s\n" % e)
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_instance.upload_proof_of_life(phone_number)
    except Exception as e:
        print("Exception when calling PartnerFullApi->upload_proof_of_life: %s\n" % e)
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

# **validate_otp**
> validate_otp(body)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.pick_validate_otp_params_exclude_keyof_validate_otp_params_device_id import PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    body = raassdkpyv2.PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId() # PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId | 

    try:
        api_instance.validate_otp(body)
    except Exception as e:
        print("Exception when calling PartnerFullApi->validate_otp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId**|  | 

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
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_pin_code**
> validate_pin_code(body)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.pick_validate_pin_code_params_exclude_keyof_validate_pin_code_params_device_id import PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId
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
    api_instance = raassdkpyv2.PartnerFullApi(api_client)
    body = raassdkpyv2.PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId() # PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId | 

    try:
        api_instance.validate_pin_code(body)
    except Exception as e:
        print("Exception when calling PartnerFullApi->validate_pin_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId**|  | 

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
**200** |  |  -  |
**400** | Invalid pincode |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

