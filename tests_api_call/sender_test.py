import pytest
from datetime import datetime

import raassdkpyv2
from raassdkpyv2.api.partner_send_api import PartnerSendApi
from raassdkpyv2.api.partner_full_api import PartnerFullApi 
from raassdkpyv2.api.partner_api import PartnerApi
from raassdkpyv2.api.default_api import DefaultApi

# MODELS
from raassdkpyv2.models.register_user_params import RegisterUserParams
from raassdkpyv2.models.country_alpha2_code import CountryAlpha2Code
from raassdkpyv2.models.user_token_response import UserTokenResponse

#Exceptions
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


def test_register_sender():
    partner_send_api : PartnerSendApi = PartnerSendApi(api_client=api_client)
    
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
        response:UserTokenResponse = partner_send_api.register_sender(request)
        if isinstance(response, UserTokenResponse):
            assert isinstance(response.to_dict(), dict)
            assert isinstance(response.to_json(), str)
            assert isinstance(response.to_str(), str)
        assert isinstance(response, UserTokenResponse)
            
    except ApiException as e:
        print(f"Exception when calling PartnerSendApi -> test_register_sender: {e}\n")
        assert False
        