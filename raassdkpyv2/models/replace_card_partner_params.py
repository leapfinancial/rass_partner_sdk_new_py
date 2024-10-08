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
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ReplaceCardPartnerParams(BaseModel):
    """
    ReplaceCardPartnerParams
    """ # noqa: E501
    number: Annotated[str, Field(min_length=1, strict=True)]
    name: StrictStr
    cardtype: StrictStr
    is_primary: StrictBool = Field(alias="isPrimary")
    name_on_card: StrictStr = Field(alias="nameOnCard")
    expiration_date: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="expirationDate")
    security_code: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, alias="securityCode")
    currency: Optional[StrictStr] = None
    country: Annotated[str, Field(min_length=1, strict=True)]
    card_network: StrictStr = Field(alias="cardNetwork")
    operation_id: StrictStr = Field(alias="operationId")
    __properties: ClassVar[List[str]] = ["number", "name", "cardtype", "isPrimary", "nameOnCard", "expirationDate", "securityCode", "currency", "country", "cardNetwork", "operationId"]

    @field_validator('cardtype')
    def cardtype_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DebitCard', 'CreditCard'):
            raise ValueError("must be one of enum values ('DebitCard', 'CreditCard')")
        return value

    @field_validator('card_network')
    def card_network_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('NotApplicable', 'UATP', 'Visa', 'ChinaUnionPay', 'InterPayment', 'DiscoverCard', 'Dankort', 'Cardguard', 'MIR', 'MasterCard', 'Verve', 'InstaPayment', 'Maestro', 'DinersClubInternational', 'AmericanExpress', 'JCB', 'TROY'):
            raise ValueError("must be one of enum values ('NotApplicable', 'UATP', 'Visa', 'ChinaUnionPay', 'InterPayment', 'DiscoverCard', 'Dankort', 'Cardguard', 'MIR', 'MasterCard', 'Verve', 'InstaPayment', 'Maestro', 'DinersClubInternational', 'AmericanExpress', 'JCB', 'TROY')")
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
        """Create an instance of ReplaceCardPartnerParams from a JSON string"""
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
        """Create an instance of ReplaceCardPartnerParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "name": obj.get("name"),
            "cardtype": obj.get("cardtype"),
            "isPrimary": obj.get("isPrimary"),
            "nameOnCard": obj.get("nameOnCard"),
            "expirationDate": obj.get("expirationDate"),
            "securityCode": obj.get("securityCode"),
            "currency": obj.get("currency"),
            "country": obj.get("country"),
            "cardNetwork": obj.get("cardNetwork"),
            "operationId": obj.get("operationId")
        })
        return _obj


