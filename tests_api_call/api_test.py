from typing import List
import pytest
import raassdkpyv2
from raassdkpyv2.api.partner_send_api import PartnerSendApi
from raassdkpyv2.api.partner_full_api import PartnerFullApi 
from raassdkpyv2.api.partner_api import PartnerApi
from raassdkpyv2.api.default_api import DefaultApi

# MODELS
# models is_phone_available
from raassdkpyv2.models.is_phone_available_request import IsPhoneAvailableRequest
from raassdkpyv2.models.is_phone_available_response import IsPhoneAvailableResponse
from raassdkpyv2.models.exchange_rate_dto import ExchangeRateDTO
# models get_user_token
from raassdkpyv2.models.get_user_token_params import GetUserTokenParams
from raassdkpyv2.models.user_token_response import UserTokenResponse
# models pre_quote
from raassdkpyv2.models.raas_pre_quote_response import RaasPreQuoteResponse
from raassdkpyv2.models.raas_pre_quote_request import RaasPreQuoteRequest
#models get operation quote
from raassdkpyv2.models.quote_transaction_base import QuoteTransactionBase
from raassdkpyv2.models.raas_quote_transaction_response import RaasQuoteTransactionResponse
#models register Send
from raassdkpyv2.models.register_user_params import RegisterUserParams
from raassdkpyv2.models.country_alpha2_code import CountryAlpha2Code
from datetime import datetime
#models get_profile
from raassdkpyv2.models.user import User
# models update_profile
from raassdkpyv2.models.user_update_params import UserUpdateParams
#models get_cip_info PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC
from raassdkpyv2.models.pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac import PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC
#models add_card
from raassdkpyv2.models.add_card_partner_params import AddCardPartnerParams
from raassdkpyv2.models.add_payment_method_response import AddPaymentMethodResponse
#models verify_card
from raassdkpyv2.models.verify_micro_trx_params import VerifyMicroTrxParams
# models create pin
from raassdkpyv2.models.set_pincode_params_partner import SetPincodeParamsPartner
#model validate pin code
from raassdkpyv2.models.pick_validate_pin_code_params_exclude_keyof_validate_pin_code_params_device_id import PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId
# models list contacts
from raassdkpyv2.models.contact_info import ContactInfo
# models create contact
from raassdkpyv2.models.create_contact_request_params_partner import CreateContactRequestParamsPartner
# models level two
from raassdkpyv2.models.level_two_params import LevelTwoParams
# models send money
from raassdkpyv2.models.send_money_partner_params import SendMoneyPartnerParams
from raassdkpyv2.models.pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen import PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen
# models get_destination_sof_for_requet_money_operation
from raassdkpyv2.models.source_of_funding import SourceOfFunding
#Exceptions
from raassdkpyv2.exceptions import ApiException
#models send
from raassdkpyv2.models.send_money_params import SendMoneyParams
from raassdkpyv2.models.send_money_response import SendMoneyResponse
#models get_cash_operators
from raassdkpyv2.models.cash_operators_params_base import CashOperatorsParamsBase
from raassdkpyv2.models.cash_operators import CashOperators
#models set_reference_code
from raassdkpyv2.models.set_reference_code_params_base import SetReferenceCodeParamsBase
from raassdkpyv2.models.get_reference_code_response import GetReferenceCodeResponse
#models get_in_and_out_operations
from raassdkpyv2.models.operation_detail_response import OperationDetailResponse
#models receive
from raassdkpyv2.models.receive_money_params import ReceiveMoneyParams
#models set_alternate_cip
from raassdkpyv2.models.alternate_flow import AlternateFlow

"""Initial config for the test module. 
    this method is called before any test is executed
"""
def setup_module():
    global api_client
    configuration = raassdkpyv2.Configuration(
        host="https://raas-partner-cv.nomas.cash/v1",        
        api_key={'api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoibkJ1NkRWc0FnSjdzYUU3aWU5YWgiLCJuYW1lIjoiTnVtaSBTRU5EIiwiY291bnRyeSI6IlVTIiwiY29kZSI6Im51bWlfc2VuZCIsInNjb3BlcyI6WyJwYXJ0bmVyX2Z1bGwiXX0sImlhdCI6MTcxMDg2ODA5NywiZXhwIjoxNzQyNDA0MDk3fQ.RRljlIvcJFf0F8h702WWWlNqvu2ocy28fWPfVxPETh4'}
    )
    configuration.verify_ssl = False
    api_client = raassdkpyv2.ApiClient(configuration)
    print("SETUP DONE")

"""End config for the test module.
    this method is called after all tests have been executed
"""
def teardown_module():
    global api_client
    api_client.close()
    print("TEARDOWN DONE")
    
    
def test_is_phone_available():
    send_api : PartnerSendApi = PartnerSendApi(api_client=api_client)    

    try:
        request = IsPhoneAvailableRequest(phone=phone)
        
        response:IsPhoneAvailableResponse = send_api.is_phone_available(request)
        if isinstance(response, IsPhoneAvailableResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
        assert isinstance(response, IsPhoneAvailableResponse)
            
    except ApiException as e:
        print(f"Exception when calling DefaultApi->is_phone_available: {e}\n")
        assert False
        
def test_registerlevel2():
    default_api:DefaultApi = DefaultApi(api_client)
    request = RegisterUserParams(
        phoneNumber=phone,
        lastName='felix01',
        firstName='Harry01',        
        countryCode=CountryAlpha2Code('US'),
        city='Lakeland',
        state='FL',        
        gender='Male',
        dob = datetime.strptime('1996-03-27T00:00:00.00Z', "%Y-%m-%dT%H:%M:%S.%fZ"),
        email='ruben01@leap.com',
        middleName='middleName',
        address1='6860 Shadowcast Ln',
        address2='address',
        zipCode='zipCode',
        birthState='birthState',
    )
    
    try:
        response:UserTokenResponse = default_api.register_user_v2(register_user_params=request)
        if isinstance(response, UserTokenResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)            
            assert isinstance(response, UserTokenResponse)
            print(response)
    except ApiException as e:
        print(f"Exception when calling DefaultApi->register_user_v2: {e}\n")
        assert False
        
def test_set_level_two():
    full_api:PartnerFullApi = PartnerFullApi(api_client)
    request = LevelTwoParams(
        ssn="123456789",
        callLocationLatitude=0.0,
        callLocationLongitude=0.0,
    )
    try:
        response = full_api.set_level_two(phone_number=phone, level_two_params=request)        
        if response.status_code == 200:
            print("set level two successfull")
        assert response.status_code == 200
    except ApiException as e:
        print(f"Exception when calling DefaultApi->set_level_two: {e}\n")
        assert False

def test_register_sender():
    send_api : PartnerSendApi = PartnerSendApi(api_client)        
    
    request = RegisterUserParams(
        phoneNumber=phone,
        lastName='Gonzalez01',
        firstName='Ruben01',        
        countryCode=CountryAlpha2Code('US'),
        city='Lakeland',
        state='FL',
        lastName2='Melesio01',
        gender='Male',
        dob = datetime.strptime('1988-03-22T00:00:00.00Z', "%Y-%m-%dT%H:%M:%S.%fZ"),
        email='ruben01@leap.com',
        middleName='middleName',
        address1='6860 Shadowcast Ln',
        address2='address',
        zipCode='zipCode',
        birthState='birthState',
    )
    
    try:
        response : UserTokenResponse = send_api.register_sender(register_user_params=request)

        if isinstance(response, UserTokenResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
    except ApiException as e:        
        print(f"\033[91m Exception when calling PartnerSendApi -> register_sender:{e}\n\033[0m")
        assert False, "prueba de formato con texto"
           
               
    # resp: {'status': 'Completed','status_detail': 'None','user_id': '8x58C4MMuPS9xFjd5jv9FYwwLX93'}
    print('resp registerUser: '+str(response))      
        
def test_exchange_rate():  
    full_api : PartnerFullApi = PartnerFullApi(api_client)    
    current_code_src = "USD"
    current_code_dest = "MXN"
    
    try:
        response:ExchangeRateDTO = full_api.get_exchange_rates(currency_code_src = current_code_src, currency_code_dest = current_code_dest)[0]            
        if isinstance(response, ExchangeRateDTO):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, ExchangeRateDTO)
                
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi->get_exchange_rates: {e}\n")
        assert False, ""
  

def test_get_user_token()->str:
    partner_api = PartnerApi(api_client)
    phoneNumber = phone
                    
    user_token_params : GetUserTokenParams = {
        "phoneNumber":f"{phoneNumber}",
    }
    
    try:
        token: UserTokenResponse = partner_api.get_user_token( user_token_params )        
        if isinstance(token, UserTokenResponse):
            assert isinstance(token.to_dict(), dict)
            assert isinstance(token.to_json(), str)
            assert isinstance(token.to_str(), str)
            assert isinstance(token, UserTokenResponse)
        token = token.to_dict()
    except ApiException as e:
        print(f"\033[91m Exception when calling PartnerApi -> get_user_token:{e}\n\033[0m")
        assert False
    
    return token['userId']

def test_get_prequote_transaction():
    full_api : PartnerFullApi = PartnerFullApi(api_client)    
    request : RaasPreQuoteRequest = RaasPreQuoteRequest(        
        
        DestinationPaymentMethod={
            "type": "DebitCard",
            "country": "MX"
        },
        SenderCountryCode="US",
        IsSenderAmount=True,
        Amount=10,
        OperationType="SendFunds",
        ProductType="NumiService"
    )
    
    token = test_get_user_token()
    
    try:
        response:RaasPreQuoteResponse = full_api.pre_quote(token, raas_pre_quote_request=request)
        for quote in response.quotes:
            quote : RaasPreQuoteResponse
            quote = quote.to_dict()
            print(quote['type'])
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi->pre_quote: {e}\n")
        assert False
        
def test_operation_quote():
    full_api : PartnerFullApi = PartnerFullApi(api_client)    
    
    request = QuoteTransactionBase(
        senderUserId="",
        senderCountryCode="US",
        recipientUserId="",
        recipientCountryCode="MX",
        recipientAmount=10,
        isSenderAmount=True,
        amountCurrency="USD",
        amount=10,
        operationType="SendFunds",
        sourcePaymentMethod="DebitCard",
        destinationPaymentMethod="DebitCard",
        destinationCountryCode="MX",
    )
    token = test_get_user_token()
    try:
        response:RaasQuoteTransactionResponse = full_api.get_operation_quote(user_token=token, quote_transaction_base=request)
        if isinstance(response, RaasQuoteTransactionResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, RaasQuoteTransactionResponse)
            print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> get_operation_quote: {e}\n")
        assert False
            
def test_update_profile():
    full_api : PartnerFullApi = PartnerFullApi(api_client) 
    
    request = UserUpdateParams(
        email="updated@leap.com",
        firstName="HARRY",                
        gender="",
        dob=datetime.now().isoformat(),
        country_id="",        
        firstTime=True
    )
    try:
        response = full_api.update_profile(phone=phone, user_update_params=request)        
        if response.status_code == 200:
            print("test update profile successfull")
        assert response.status_code == 200
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> update_profile: {e}\n")
        assert False

def test_update_profile():
    full_api : PartnerFullApi = PartnerFullApi(api_client)    
    try:
        response:User = full_api.get_profile(phone="+526621057900")
        if isinstance(response, User):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, User)
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi->get_profile: {e}\n")
        assert False


def test_get_cip_info():
    default_api:DefaultApi  = DefaultApi(api_client)    
    try:
        response: PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC = default_api.get_cip_info(phone_number=phone)
        if isinstance(response, PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC)
            print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi-> get_cip_info: {e}\n")
        assert False
        
def test_set_alternate_cip():
    full_api : PartnerFullApi = PartnerFullApi(api_client)
    try:
        response = full_api.set_alternate_cip(phone_number=phone, type="OFAC")
        if response.status_code == 200:
            print("set alternate cip successfull")
            assert response.status_code == 200
        if response.status_code == 400:
            print("set alternate cip failed")
            assert False
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> set_alternate_cip: {e}\n")
        assert False
        
def test_add_card():
    send_api : PartnerSendApi = PartnerSendApi(api_client)    
    
    card:AddCardPartnerParams = AddCardPartnerParams(
        name="visa-1111",
        cardtype="CreditCard",
        number="tok_sandbox_9PNgfqqpdpyQpnD1jYkdw1_1111",
        isPrimary=True,
        nameOnCard="Andres Pinto",
        expirationDate="1224",
        country="US",
        cardNetwork="NotApplicable",
        securityCode="tok_sandbox_7YcvwXKE1jVLeEHofR3GiR"
    
    )
    token = test_get_user_token()
    
    try:
        response:AddPaymentMethodResponse = send_api.add_card(user_token=token, add_card_partner_params=card)
        if isinstance(response, AddPaymentMethodResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, AddPaymentMethodResponse)
            print(response.to_dict())
            cardId = response.id
    except ApiException as e:
        print(f"Exception when calling PartnerSendApi-> add_card: {e}\n")
        assert False
        
def test_verify_card(amount:str):
    send_api : PartnerSendApi = PartnerSendApi(api_client)
    token = test_get_user_token()
    
    micro = VerifyMicroTrxParams(
        cardId=cardId,
        amount=amount,
    )
    try:
        response = send_api.verify_card(user_token=token, verify_micro_trx_params=micro)
        if isinstance(response, AddPaymentMethodResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, AddPaymentMethodResponse)
            print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling PartnerSendApi-> verify_card: {e}\n")
        assert False   
        
def test_create_pin():
    full_api : PartnerFullApi = PartnerFullApi(api_client)
    
    request = SetPincodeParamsPartner(
        pincode=pin_code,
        phone=phone        
    )
    try:
        response = full_api.create_pin(set_pincode_params_partner=request)
        if response.status_code == 200:
            print("create pin successfull")
            assert response.status_code == 200
        if response.status_code == 400:
            print("create pin failed")
            assert False
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> create_pin: {e}\n")
        assert False
        
def test_validate_pin_code():
    full_api : PartnerFullApi = PartnerFullApi(api_client)
    request = PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId(
        phone=phone,
        pincode=pin_code
    )
    try:
        response = full_api.validate_pin_code(body=request)
        if response.status_code == 200:
            print("validate pin successfull")
            assert response.status_code == 200
        if response.status_code == 400:
            print("validate pin failed")
            assert False
    except ApiException as e:
        print(f"Exception when calling partenerFullApi -> validate_pin_code: {e}\n")
        assert False
    
def test_create_contact():
    partner_api : PartnerApi = PartnerApi(api_client)
    token = test_get_user_token()
    request = CreateContactRequestParamsPartner(
        alias="alias",
        countryCode="US",
        phone=phone2,
        lastName="lastName",
        firstName="firstName",
        email="email@leap.com"
    )
        
    try:
        response = partner_api.create_contact(user_token=token, create_contact_request_params_partner=request)
        print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling PartnerApi-> create contact: {e}\n")
        assert False
        
def test_list_contacts():
    partner_send_api : PartnerApi = PartnerApi(api_client)
    token = test_get_user_token()
    try:
        response:ContactInfo = partner_send_api.list_contacts(user_token=token)
        if isinstance(response, ContactInfo):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, ContactInfo)
            print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling PartnerSendApi-> list_contacts: {e}\n")
        assert False
        
        
def test_send_funds():
    send_api : PartnerSendApi = PartnerSendApi(api_client)
    request = SendMoneyPartnerParams(
        quotationId="",
        currency="USD",
        amount=10,
        reason="reason",
        destinationPaymentMethodId="",
        sourcePaymentMethodId="",
        correlationId="",
        sendTo="",
    )
    token = test_get_user_token()
    try:
        response:PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen = send_api.send_funds(user_token=token, send_money_partner_params=request)
        if isinstance(response, PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen)
            print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling Send api -> send_funds: {e}\n")
        assert False

def test_get_destination_sof_for_requet_money_operation():
    default_api : DefaultApi = DefaultApi(api_client)
    
    user_token = test_get_user_token()
    
    try :
        response: List[SourceOfFunding] = default_api.get_destination_sof_for_requet_money_operation(user_token=user_token, source_country=source_conutrty, destination_country=destination_country)
        if isinstance(response, List[SourceOfFunding]):
            for sof in response:
                sof: SourceOfFunding
                assert isinstance(sof.to_dict(), dict)
                assert isinstance(sof.to_json(), str)
                assert isinstance(sof.to_str(), str)
                assert isinstance(sof, SourceOfFunding)
                print(sof.to_dict())
        else :
            assert False
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> get_destination_sof_for_requet_money_operation: {e}\n")
        assert False
        
def test_get_operation_quote():
    full_api : PartnerFullApi = PartnerFullApi(api_client)
    
    request = QuoteTransactionBase(
        senderUserId="",
        senderCountryCode="US",
        recipientUserId="",
        recipientCountryCode="MX",
        recipientCurrency="MXN",
        recipientAmount=10,
        isSenderAmount=True,
        amountCurrency="USD",
        amount=10,
        operationType="SendFunds",
        sourcePaymentMethod="DebitCard",
        destinationPaymentMethod="DebitCard",
        tennantFee=0,
    )
    
    user_token = test_get_user_token()    
    try:
        response:RaasQuoteTransactionResponse = full_api.get_operation_quote(user_token=user_token, quote_transaction_base=request)
        if isinstance(response, RaasQuoteTransactionResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, RaasQuoteTransactionResponse)
            print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> get_operation_quote: {e}\n")
        assert False
        
def test_send():
    full_api : PartnerFullApi = PartnerFullApi(api_client)
    
    request = SendMoneyParams(
        correlationId= "",
        sourcePaymentMethod= "DebitCard",
        destinationPaymentMethod= "DebitCard",
        amount= 10,
        currency= "USD",
        code= "USD",
        status= "Completed",
        senderAmount= 10,
        senderCurrency= "USD",
        recipientAmount= 10,
        recipientCurrency= "USD",
        feeType= "Fixed",
        sourceFee= 0,
        transactionFee= 0,
        destinationFee= 0,
        exchangeRate= 0,
        callLocationLongitude= 0.0,
        callLocationLatitude= 0.0,
        reason= "reason",
        tenantId= "",
        userTenantId= "",
        tenantFee= 0,
        sendTo= "",
    )
    
    user_token = test_get_user_token()
    try:
        response:SendMoneyResponse = full_api.send(user_token=user_token, send_money_params=request)
        if isinstance(response, SendMoneyResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, SendMoneyResponse)
            print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> send: {e}\n")
        assert False

def test_get_cash_operators():
    send_api : PartnerSendApi = PartnerSendApi(api_client)
    
    request = CashOperatorsParamsBase(
        operationAmmount=10,
    )
        
    user_token = test_get_user_token()
    
    try:
        response: List[CashOperators] = send_api.get_cash_operators(user_token=user_token, cash_operators_params_base=request)
        if isinstance(response, List[CashOperators]):
            for operator in response:
                operator: CashOperators
                assert isinstance(operator.to_dict(), dict)
                assert isinstance(operator.to_json(), str)
                assert isinstance(operator.to_str(), str)
                assert isinstance(operator, CashOperators)
                print(operator.to_dict())
        else:
            assert False
    except ApiException as e:
        print(f"Exception when calling DefaultApi -> get_cash_operators: {e}\n")
        assert False
        
def test_set_reference_code():
    send_api : PartnerSendApi = PartnerSendApi(api_client)
    
    request = SetReferenceCodeParamsBase(
        operationId="",
        operationCode="",
        amount=10,
        currency="USD",
        senderName="",
        receiverName="",
        networkId="",
        operationType="SendFunds",
        cashProvider="",
    )
    
    token = test_get_user_token()
    try:
        response: GetReferenceCodeResponse = send_api.set_reference_code(user_token=token, set_reference_code_params_base=request)
        if isinstance(response, GetReferenceCodeResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, GetReferenceCodeResponse)
            print(response.to_dict())
    except ApiException as e:
        print(f"Exception when calling PartnerSendApi -> set_reference_code: {e}\n")
        assert False
        
def test_get_in_and_out_operations():
    full_api : PartnerFullApi = PartnerFullApi(api_client)
    
    user_token = test_get_user_token()
    
    try:
        response : List[OperationDetailResponse] = full_api.get_in_and_out_operations(user_token=user_token, to_phone_number=phone)
        if isinstance(response, list):
            for operation in response:
                operation: OperationDetailResponse
                assert isinstance(operation.to_dict(), dict)
                assert isinstance(operation.to_json(), str)
                assert isinstance(operation.to_str(), str)
                assert isinstance(operation, OperationDetailResponse)
                print(operation.to_dict())
        else:
            assert False
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> get_in_and_out_operations: {e}\n")
        assert False

def test_get_destination_sof_for_requet_money_operation():
    default_api : DefaultApi = DefaultApi(api_client)
    
    user_token = test_get_user_token()
    
    try :
        response: List[SourceOfFunding] = default_api.get_destination_sof_for_requet_money_operation(user_token=user_token, source_country=source_conutrty, destination_country=destination_country)
        if isinstance(response, List[SourceOfFunding]):
            for sof in response:
                sof: SourceOfFunding
                assert isinstance(sof.to_dict(), dict)
                assert isinstance(sof.to_json(), str)
                assert isinstance(sof.to_str(), str)
                assert isinstance(sof, SourceOfFunding)
                print(sof.to_dict())
        else :
            assert False
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> get_destination_sof_for_requet_money_operation: {e}\n")
        assert False
        
def test_get_sof_for_send_money_operation():
    send_api : PartnerSendApi = PartnerSendApi(api_client)
    
    user_token = test_get_user_token()
    
    try :
        response: List[SourceOfFunding] = send_api.get_sof_for_send_money_operation(user_token=user_token, source_country=source_conutrty, destination_country=destination_country)
        if isinstance(response, List[SourceOfFunding]):
            for sof in response:
                sof: SourceOfFunding
                assert isinstance(sof, SourceOfFunding)
                assert isinstance(sof.to_dict(), dict)
                assert isinstance(sof.to_json(), str)
                assert isinstance(sof.to_str(), str)                
                print(sof.to_dict())
        else :
            assert False
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> get_sof_for_send_money_operation: {e}\n")
        assert False

def test_receive():
    full_api : PartnerFullApi = PartnerFullApi(api_client)
    
    request = ReceiveMoneyParams(
        destinationPaymentMethod="DebitCard",
        correlationId="",
    )
    
    user_token = test_get_user_token()
    try:
        response:SendMoneyResponse = full_api.receive(user_token=user_token, receive_money_params=request)
        if response.status_code == 200:
            print("receive successfull")
            assert response.status_code == 200
        if response.status_code == 400:
            print("receive failed")
            assert False
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> receive: {e}\n")
        assert False

def test_set_alternate_cip():
    full_api : PartnerFullApi = PartnerFullApi(api_client)
    try:
        response = full_api.set_alternate_cip(phone_number=phone, type=AlternateFlow.SSN)
        if response.status_code == 200:
            print("set alternate cip successfull")
            assert response.status_code == 200
        if response.status_code == 400:
            print("set alternate cip failed")
            assert False
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi -> set_alternate_cip: {e}\n")
        assert False
##For debugging purposes, uncomment the following lines
############################################################################################################
        
if __name__ == '__main__':    
    setup_module()
        
    global phone
    #phone = "+14073649716" 
    phone = "+14073649702" 
    #for add contact 
    phone2 = "+14073649703"
    #set pin code
    pin_code = "123"
    
    #contat jorge
    #phone = "+12146930301"
    global cardId
    cardId = "ac31fb3d-043e-47e8-9f6f-9234d804a5ec"
    
    global source_conutrty
    source_conutrty = "US"
    global destination_country
    destination_country = "MX"
    
    #test_registerlevel2()
    
    #test_exchange_rate()
    #test_is_phone_available(phone)
    #test_register_sender()
    #test_get_user_token()
    #test_get_prequote_transaction()
    #test_get_profile()
    #test_get_cip_info()
    #test_add_card()
    test_list_contacts()
    #test_create_contact()
    
    teardown_module()
    
    
    
    #set_alternate_cip TODO check params
    #pending test
    #set_alternate_cip
    #get_operation_quote
    #send
    #get_cash_operators
    #set_reference_code
    #get_in_and_out_operations
    #operation_quote
    #send_funds
    #get_destination_sof_for_requet_money_operation
    #get_destination_sof_for_requet_money_operation
    #get_sof_for_send_money_operation
    #receive