import pytest
import raassdkpyv2
from raassdkpyv2.api.partner_send_api import PartnerSendApi
from raassdkpyv2.api.partner_full_api import PartnerFullApi 
from raassdkpyv2.models.is_phone_available_request import IsPhoneAvailableRequest
from raassdkpyv2.models.is_phone_available_response import IsPhoneAvailableResponse
from raassdkpyv2.models.raas_pre_quote_request import RaasPreQuoteRequest
from raassdkpyv2.models.exchange_rate_dto import ExchangeRateDTO
from raassdkpyv2.exceptions import ApiException


"""Initial config for the test module. 
    this method is called before any test is executed
"""
def setup_module():
    global api_client
    configuration = raassdkpyv2.Configuration(
        host="https://raas-partner-dev.nomas.cash/v1",        
        api_key={'api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoidWJKbW9SVmxJbUNlbkRoV21iZEYiLCJuYW1lIjoiTnVtaSIsImNvdW50cnkiOiJVUyIsImNvZGUiOiJudW1pX2FwcF9zZW5kIiwic2NvcGVzIjpbInBhcnRuZXJfZnVsbCJdfSwiaWF0IjoxNjgyMDE5Nzg1LCJleHAiOjE3MTM1NTU3ODV9.De3zQyh6vIjVTr7ob4sOFmjWDChFDuFB0o2MOYERSUQ'}
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
        request = IsPhoneAvailableRequest(phone="+526621057946")
        
        response:IsPhoneAvailableResponse = partner_send_api.is_phone_available(request)
        if isinstance(response, ExchangeRateDTO):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
        assert isinstance(response, IsPhoneAvailableResponse)
            
    except ApiException as e:
        print(f"Exception when calling DefaultApi->is_phone_available: {e}\n")
        assert False
        
def test_exchange_rate():  
    partner_full_api : PartnerFullApi = PartnerFullApi(api_client)    
    current_code_src = "USD"
    current_code_dest = "MXN"
    
    try:
        response:ExchangeRateDTO = partner_full_api.get_exchange_rates(currency_code_src = current_code_src, currency_code_dest = current_code_dest)[0]            
        assert isinstance(response.to_dict(), dict)
        assert isinstance(response.to_json(), str)
        assert isinstance(response.to_str(), str)
        assert isinstance(response, ExchangeRateDTO)
                
    except ApiException as e:
        print(f"Exception when calling PartnerFullApi->get_exchange_rates: {e}\n")
        assert False
  
  
##For debugging purposes, uncomment the following lines
############################################################################################################
        
# if __name__ == '__main__':    
#     setup_module()
#     test_is_phone_available()
#     test_exchange_rate()
#     teardown_module()