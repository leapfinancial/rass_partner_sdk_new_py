import raassdkpyv2


from raassdkpyv2.api.partner_send_api import PartnerSendApi
from raassdkpyv2.api.partner_full_api import PartnerFullApi 
from raassdkpyv2.api.partner_api import PartnerApi
from raassdkpyv2.api.default_api import DefaultApi

#Exceptions
from raassdkpyv2.exceptions import ApiException

# MODELS
# models is_phone_available
from raassdkpyv2.models.is_phone_available_request import IsPhoneAvailableRequest
from raassdkpyv2.models.is_phone_available_response import IsPhoneAvailableResponse
#models get_profile
from raassdkpyv2.models.user import User
# models get_user_token
from raassdkpyv2.models.get_user_token_params import GetUserTokenParams
from raassdkpyv2.models.user_token_response import UserTokenResponse
#models get_cip_info
from raassdkpyv2.models.pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac import PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC
#models exchange_rate
from raassdkpyv2.models.exchange_rate_dto import ExchangeRateDTO

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
        
def test_get_user_token()->str:
    partner_api = PartnerApi(api_client)    
                    
    user_token_params : GetUserTokenParams = {
        "phoneNumber":f"{phone}",
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

def test_get_profile():
    full_api : PartnerFullApi = PartnerFullApi(api_client)    
    try:
        response:User = full_api.get_profile(phone=phone)
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