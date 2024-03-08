# raassdkpyv2.PartnerSendApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bank_account**](PartnerSendApi.md#add_bank_account) | **POST** /user/funding/source/bank/add/{userToken} | 
[**add_card**](PartnerSendApi.md#add_card) | **POST** /user/funding/source/card/add/{userToken} | 
[**create_contact**](PartnerSendApi.md#create_contact) | **POST** /user/contacts/{userToken} | 
[**delete_payment_method**](PartnerSendApi.md#delete_payment_method) | **POST** /user/funding/source/delete/{userToken} | 
[**get_cash_operators**](PartnerSendApi.md#get_cash_operators) | **POST** /user/funding/cash/operators/{userToken} | 
[**get_cip_info**](PartnerSendApi.md#get_cip_info) | **GET** /cip/process/{phoneNumber} | 
[**get_operation**](PartnerSendApi.md#get_operation) | **GET** /user/operations/detail/{id} | 
[**get_operation_status**](PartnerSendApi.md#get_operation_status) | **GET** /user/operations/status/{userToken}/{operationId} | 
[**get_payment_method**](PartnerSendApi.md#get_payment_method) | **GET** /user/funding/source/get-payment-method/{userToken} | 
[**get_payment_method_v2**](PartnerSendApi.md#get_payment_method_v2) | **GET** /user/funding/source/get-payment-method-v2/{userToken} | 
[**get_sof_for_send_money_operation**](PartnerSendApi.md#get_sof_for_send_money_operation) | **GET** /user/funding/source/send-money/{userToken} | 
[**get_user_token**](PartnerSendApi.md#get_user_token) | **POST** /auth/get-user-token | 
[**is_phone_available**](PartnerSendApi.md#is_phone_available) | **POST** /auth/is-phone-available | 
[**list_contacts**](PartnerSendApi.md#list_contacts) | **GET** /user/contacts/{userToken} | 
[**operation_quote**](PartnerSendApi.md#operation_quote) | **POST** /user/operations/operation-quote/{userToken} | 
[**register_receiver**](PartnerSendApi.md#register_receiver) | **POST** /auth/register-receiver/{userToken} | 
[**register_sender**](PartnerSendApi.md#register_sender) | **POST** /auth/register-sender | 
[**send_funds**](PartnerSendApi.md#send_funds) | **POST** /user/operations/send-funds/{userToken} | 
[**set_reference_code**](PartnerSendApi.md#set_reference_code) | **POST** /user/funding/cash/reference-code/{userToken} | 
[**updated_contact**](PartnerSendApi.md#updated_contact) | **PUT** /user/contacts/{userToken} | 
[**verify_card**](PartnerSendApi.md#verify_card) | **POST** /user/funding/source/card/verify-micro-trx/{userToken} | 


# **add_bank_account**
> add_bank_account(user_token, add_bank_account_params_base)



adds bank account to subscriber's source of funding

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.add_bank_account_params_base import AddBankAccountParamsBase
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    add_bank_account_params_base = raassdkpyv2.AddBankAccountParamsBase() # AddBankAccountParamsBase | 

    try:
        api_instance.add_bank_account(user_token, add_bank_account_params_base)
    except Exception as e:
        print("Exception when calling PartnerSendApi->add_bank_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **add_bank_account_params_base** | [**AddBankAccountParamsBase**](AddBankAccountParamsBase.md)|  | 

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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    add_card_partner_params = raassdkpyv2.AddCardPartnerParams() # AddCardPartnerParams | 

    try:
        api_response = api_instance.add_card(user_token, add_card_partner_params)
        print("The response of PartnerSendApi->add_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->add_card: %s\n" % e)
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.
    create_contact_request_params_partner = raassdkpyv2.CreateContactRequestParamsPartner() # CreateContactRequestParamsPartner | 

    try:
        api_instance.create_contact(user_token, create_contact_request_params_partner)
    except Exception as e:
        print("Exception when calling PartnerSendApi->create_contact: %s\n" % e)
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | 

    try:
        api_instance.delete_payment_method(user_token, payment_method_id)
    except Exception as e:
        print("Exception when calling PartnerSendApi->delete_payment_method: %s\n" % e)
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

# **get_cash_operators**
> List[CashOperators] get_cash_operators(user_token, cash_operators_params_base)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.cash_operators import CashOperators
from raassdkpyv2.models.cash_operators_params_base import CashOperatorsParamsBase
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    cash_operators_params_base = raassdkpyv2.CashOperatorsParamsBase() # CashOperatorsParamsBase | 

    try:
        api_response = api_instance.get_cash_operators(user_token, cash_operators_params_base)
        print("The response of PartnerSendApi->get_cash_operators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->get_cash_operators: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **cash_operators_params_base** | [**CashOperatorsParamsBase**](CashOperatorsParamsBase.md)|  | 

### Return type

[**List[CashOperators]**](CashOperators.md)

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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_response = api_instance.get_cip_info(phone_number)
        print("The response of PartnerSendApi->get_cip_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->get_cip_info: %s\n" % e)
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    id = 'id_example' # str | Operation Id

    try:
        api_response = api_instance.get_operation(id)
        print("The response of PartnerSendApi->get_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->get_operation: %s\n" % e)
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    operation_id = 'operation_id_example' # str | 

    try:
        api_response = api_instance.get_operation_status(user_token, operation_id)
        print("The response of PartnerSendApi->get_operation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->get_operation_status: %s\n" % e)
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    number = '' # str |  (optional) (default to '')

    try:
        api_response = api_instance.get_payment_method(user_token, number=number)
        print("The response of PartnerSendApi->get_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->get_payment_method: %s\n" % e)
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    id = '' # str |  (optional) (default to '')

    try:
        api_response = api_instance.get_payment_method_v2(user_token, id=id)
        print("The response of PartnerSendApi->get_payment_method_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->get_payment_method_v2: %s\n" % e)
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

# **get_sof_for_send_money_operation**
> List[SourceOfFunding] get_sof_for_send_money_operation(user_token, source_country=source_country, destination_country=destination_country)



gets sources of funding for send funds

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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    source_country = 'source_country_example' # str |  (optional)
    destination_country = 'destination_country_example' # str |  (optional)

    try:
        api_response = api_instance.get_sof_for_send_money_operation(user_token, source_country=source_country, destination_country=destination_country)
        print("The response of PartnerSendApi->get_sof_for_send_money_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->get_sof_for_send_money_operation: %s\n" % e)
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    get_user_token_params = raassdkpyv2.GetUserTokenParams() # GetUserTokenParams | {@link GetUserTokenParams}

    try:
        api_response = api_instance.get_user_token(get_user_token_params)
        print("The response of PartnerSendApi->get_user_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->get_user_token: %s\n" % e)
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

# **is_phone_available**
> IsPhoneAvailableResponse is_phone_available(is_phone_available_request)



Verify is the phone number is available for registration.  It is used to check if the phone number is already registered. Returns true if the phone number is available.  SCOPES:       - partner:      ASK partners only.      - partner_send: SEND partners only.      - partner_dual: ASK+SEND partners only.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.is_phone_available_request import IsPhoneAvailableRequest
from raassdkpyv2.models.is_phone_available_response import IsPhoneAvailableResponse
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    is_phone_available_request = raassdkpyv2.IsPhoneAvailableRequest() # IsPhoneAvailableRequest | 

    try:
        api_response = api_instance.is_phone_available(is_phone_available_request)
        print("The response of PartnerSendApi->is_phone_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->is_phone_available: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_phone_available_request** | [**IsPhoneAvailableRequest**](IsPhoneAvailableRequest.md)|  | 

### Return type

[**IsPhoneAvailableResponse**](IsPhoneAvailableResponse.md)

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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.

    try:
        api_response = api_instance.list_contacts(user_token)
        print("The response of PartnerSendApi->list_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->list_contacts: %s\n" % e)
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

# **operation_quote**
> RaasQuoteTransactionResponse operation_quote(user_token, quote_transaction_partners_base)



 Retrieve quote for the operation

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.quote_transaction_partners_base import QuoteTransactionPartnersBase
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    quote_transaction_partners_base = raassdkpyv2.QuoteTransactionPartnersBase() # QuoteTransactionPartnersBase | {@link QuoteTransactionBase}

    try:
        api_response = api_instance.operation_quote(user_token, quote_transaction_partners_base)
        print("The response of PartnerSendApi->operation_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->operation_quote: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **quote_transaction_partners_base** | [**QuoteTransactionPartnersBase**](QuoteTransactionPartnersBase.md)| {@link QuoteTransactionBase} | 

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

# **register_receiver**
> UserTokenResponse register_receiver(user_token, register_user_params)



Registers Partner Receiver User for given Sender. Also, creates it as a contact  SCOPES:   - partner_send:      ASK partners only.  - partner_dual: ASK+SEND partners only.

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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    register_user_params = raassdkpyv2.RegisterUserParams() # RegisterUserParams | {@link RegisterUserParams}

    try:
        api_response = api_instance.register_receiver(user_token, register_user_params)
        print("The response of PartnerSendApi->register_receiver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->register_receiver: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
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

# **register_sender**
> UserTokenResponse register_sender(register_user_params)



Registers Partner sender user. If user exists, return its id.  SCOPES:       - partner_send: SEND partners only.      - partner_dual: ASK+SEND partners only.

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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    register_user_params = raassdkpyv2.RegisterUserParams() # RegisterUserParams | {@link RegisterUserParams}

    try:
        api_response = api_instance.register_sender(register_user_params)
        print("The response of PartnerSendApi->register_sender:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->register_sender: %s\n" % e)
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

# **send_funds**
> PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen send_funds(user_token, send_money_partner_params)



Send funds for partners

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen import PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen
from raassdkpyv2.models.send_money_partner_params import SendMoneyPartnerParams
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    send_money_partner_params = raassdkpyv2.SendMoneyPartnerParams() # SendMoneyPartnerParams | 

    try:
        api_response = api_instance.send_funds(user_token, send_money_partner_params)
        print("The response of PartnerSendApi->send_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->send_funds: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **send_money_partner_params** | [**SendMoneyPartnerParams**](SendMoneyPartnerParams.md)|  | 

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
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_reference_code**
> GetReferenceCodeResponse set_reference_code(user_token, set_reference_code_params_base)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.get_reference_code_response import GetReferenceCodeResponse
from raassdkpyv2.models.set_reference_code_params_base import SetReferenceCodeParamsBase
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    set_reference_code_params_base = raassdkpyv2.SetReferenceCodeParamsBase() # SetReferenceCodeParamsBase | 

    try:
        api_response = api_instance.set_reference_code(user_token, set_reference_code_params_base)
        print("The response of PartnerSendApi->set_reference_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerSendApi->set_reference_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **set_reference_code_params_base** | [**SetReferenceCodeParamsBase**](SetReferenceCodeParamsBase.md)|  | 

### Return type

[**GetReferenceCodeResponse**](GetReferenceCodeResponse.md)

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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.
    update_contact_request_params = raassdkpyv2.UpdateContactRequestParams() # UpdateContactRequestParams | 

    try:
        api_instance.updated_contact(user_token, update_contact_request_params)
    except Exception as e:
        print("Exception when calling PartnerSendApi->updated_contact: %s\n" % e)
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

# **verify_card**
> verify_card(user_token, verify_micro_trx_params)



Verifies microtransaction generated while adding card.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import raassdkpyv2
from raassdkpyv2.models.verify_micro_trx_params import VerifyMicroTrxParams
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
    api_instance = raassdkpyv2.PartnerSendApi(api_client)
    user_token = 'user_token_example' # str | 
    verify_micro_trx_params = raassdkpyv2.VerifyMicroTrxParams() # VerifyMicroTrxParams | 

    try:
        api_instance.verify_card(user_token, verify_micro_trx_params)
    except Exception as e:
        print("Exception when calling PartnerSendApi->verify_card: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **verify_micro_trx_params** | [**VerifyMicroTrxParams**](VerifyMicroTrxParams.md)|  | 

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

