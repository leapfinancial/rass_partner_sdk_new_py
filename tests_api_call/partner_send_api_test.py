import pytest
import raassdkpyv2
from raassdkpyv2.api.partner_send_api import PartnerSendApi
from raassdkpyv2.api.partner_full_api import PartnerFullApi 
from raassdkpyv2.api.partner_api import PartnerApi

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

#models register Send
from raassdkpyv2.models.register_user_params import RegisterUserParams
from raassdkpyv2.models.country_alpha2_code import CountryAlpha2Code
from datetime import datetime

from raassdkpyv2.exceptions import ApiException


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
    partner_send_api : PartnerSendApi = PartnerSendApi(api_client=api_client)    

    try:
        request = IsPhoneAvailableRequest(phone="+526621057900")
        
        response:IsPhoneAvailableResponse = partner_send_api.is_phone_available(request)
        if isinstance(response, IsPhoneAvailableResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
        assert isinstance(response, IsPhoneAvailableResponse)
            
    except ApiException as e:
        print(f"Exception when calling DefaultApi->is_phone_available: {e}\n")
        assert False
        

def test_register_user():
    partner_send_api : PartnerSendApi = PartnerSendApi(api_client)
    
    phoneNumber="+526621057900"
    
    request = RegisterUserParams(
        phoneNumber=phoneNumber,
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
        response : UserTokenResponse = partner_send_api.register_sender(register_user_params=request)

        if isinstance(response, UserTokenResponse):
            assert response.to_dict
            assert response.to_json
            assert response.to_str
    except ApiException as e:        
        print(f"\033[91m Exception when calling PartnerSendApi -> register_sender:{e}\n\033[0m")
        assert False, "prueba de formato con texto"
           
               
    # resp: {'status': 'Completed','status_detail': 'None','user_id': '8x58C4MMuPS9xFjd5jv9FYwwLX93'}
    print('resp registerUser: '+str(response))      
        
def test_exchange_rate():  
    partner_full_api : PartnerFullApi = PartnerFullApi(api_client)    
    current_code_src = "USD"
    current_code_dest = "MXN"
    
    try:
        response:ExchangeRateDTO = partner_full_api.get_exchange_rates(currency_code_src = current_code_src, currency_code_dest = current_code_dest)[0]            
        if isinstance(response, ExchangeRateDTO):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
            assert isinstance(response, ExchangeRateDTO)
                
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi->get_exchange_rates: {e}\n")
        assert False, ""
  

def test_get_user_token()->str:
    api_instance = PartnerApi(api_client)
    phoneNumber = "+526621057900"
                    
    user_token_params : GetUserTokenParams = {
        "phoneNumber":f"{phoneNumber}",
    }
    
    try:
        token: UserTokenResponse = api_instance.get_user_token( user_token_params )
        token = token.to_dict()
    except ApiException as e:
        print(f"\033[91m Exception when calling PartnerApi -> get_user_token:{e}\n\033[0m")
        assert False
    
    return token['userId']

def test_get_prequote_transaction():
    partner_full_api : PartnerFullApi = PartnerFullApi(api_client)
    request : RaasPreQuoteRequest = RaasPreQuoteRequest(
        # DestinationPaymentMethod={
        #     "type": "BankAccount",
        #     "country": "MX",
        # },
        # SenderCountryCode="US",
        # IsSenderAmount=True,
        # Amount=20,
        # OperationType="SendFunds",
        # ProductType="NumiService"
        
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
    print(token)
    response:RaasPreQuoteResponse = partner_full_api.pre_quote(token, raas_pre_quote_request=request)
    for quote in response.quotes:
        quote : RaasPreQuoteResponse
        quote = quote.to_dict()
        print(quote['type'])    
    
    
    
def test_get_profile():
    partner_full_api : PartnerFullApi = PartnerFullApi(api_client)
    token = test_get_user_token()
    response = partner_full_api.get_profile(user_token=token)
    print(response.to_dict())
        
  
##For debugging purposes, uncomment the following lines
############################################################################################################
        
if __name__ == '__main__':    
    setup_module()
    #test_is_phone_available()
    #test_exchange_rate()
        
    #test_register_user()
    #test_get_user_token()
    test_get_prequote_transaction()
    
    teardown_module()