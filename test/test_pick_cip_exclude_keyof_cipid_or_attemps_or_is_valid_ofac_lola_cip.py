# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpyv2.models.pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac_lola_cip import PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP  # noqa: E501

class TestPickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP(unittest.TestCase):
    """PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP:
        """Test PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP`
        """
        model = PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP()  # noqa: E501
        if include_optional:
            return PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP(
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                in_progress = True
            )
        else:
            return PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP(
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                in_progress = True,
        )
        """

    def testPickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP(self):
        """Test PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
