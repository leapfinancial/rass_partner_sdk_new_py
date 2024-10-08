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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AddBankAccountParamsBase(BaseModel):
    """
    AddBankAccountParamsBase
    """ # noqa: E501
    name: StrictStr = Field(description="payment method name: p.e. HSBC-1111")
    account_number: StrictStr = Field(alias="accountNumber")
    bank_account_type: StrictStr = Field(description="Bank account type", alias="bankAccountType")
    bank_entity_number: StrictStr = Field(alias="bankEntityNumber")
    is_primary: StrictBool = Field(description="Main payment method?", alias="isPrimary")
    country: StrictStr
    currency: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "accountNumber", "bankAccountType", "bankEntityNumber", "isPrimary", "country", "currency"]

    @field_validator('bank_account_type')
    def bank_account_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CheckingAccount', 'SavingsAccount', 'OtherAccount'):
            raise ValueError("must be one of enum values ('CheckingAccount', 'SavingsAccount', 'OtherAccount')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddBankAccountParamsBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AddBankAccountParamsBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "accountNumber": obj.get("accountNumber"),
            "bankAccountType": obj.get("bankAccountType"),
            "bankEntityNumber": obj.get("bankEntityNumber"),
            "isPrimary": obj.get("isPrimary"),
            "country": obj.get("country"),
            "currency": obj.get("currency")
        })
        return _obj


