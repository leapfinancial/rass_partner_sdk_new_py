# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class AddBankAccountParamsBase(BaseModel):
    """
    AddBankAccountParamsBase
    """
    name: StrictStr = Field(..., description="payment method name: p.e. HSBC-1111")
    account_number: StrictStr = Field(..., alias="accountNumber")
    bank_account_type: StrictStr = Field(..., alias="bankAccountType", description="Bank account type")
    bank_entity_number: StrictStr = Field(..., alias="bankEntityNumber")
    is_primary: StrictBool = Field(..., alias="isPrimary", description="Main payment method?")
    country: StrictStr = Field(...)
    currency: Optional[StrictStr] = None
    __properties = ["name", "accountNumber", "bankAccountType", "bankEntityNumber", "isPrimary", "country", "currency"]

    @validator('bank_account_type')
    def bank_account_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CheckingAccount', 'SavingsAccount', 'OtherAccount'):
            raise ValueError("must be one of enum values ('CheckingAccount', 'SavingsAccount', 'OtherAccount')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AddBankAccountParamsBase:
        """Create an instance of AddBankAccountParamsBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddBankAccountParamsBase:
        """Create an instance of AddBankAccountParamsBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddBankAccountParamsBase.parse_obj(obj)

        _obj = AddBankAccountParamsBase.parse_obj({
            "name": obj.get("name"),
            "account_number": obj.get("accountNumber"),
            "bank_account_type": obj.get("bankAccountType"),
            "bank_entity_number": obj.get("bankEntityNumber"),
            "is_primary": obj.get("isPrimary"),
            "country": obj.get("country"),
            "currency": obj.get("currency")
        })
        return _obj

