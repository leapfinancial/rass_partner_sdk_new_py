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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from raassdkpyv2.models.raa_s_payment_method import RaaSPaymentMethod
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RequestMoneyParams(BaseModel):
    """
    RequestMoneyParams
    """ # noqa: E501
    correlation_id: StrictStr = Field(alias="correlationId")
    destination_payment_method: RaaSPaymentMethod = Field(alias="destinationPaymentMethod")
    reason: StrictStr
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    currency: Optional[StrictStr] = None
    sender_currency: Optional[StrictStr] = Field(default=None, alias="senderCurrency")
    sender_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="senderAmount")
    recipient_amount: Union[StrictFloat, StrictInt] = Field(alias="recipientAmount")
    recipient_currency: StrictStr = Field(alias="recipientCurrency")
    bonus_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="bonusAmount")
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    user_tenant_id: Optional[StrictStr] = Field(default=None, alias="userTenantId")
    application: Optional[StrictStr] = None
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="exchangeRate")
    request_to: StrictStr = Field(alias="requestTo")
    __properties: ClassVar[List[str]] = ["correlationId", "destinationPaymentMethod", "reason", "amount", "currency", "senderCurrency", "senderAmount", "recipientAmount", "recipientCurrency", "bonusAmount", "tenantId", "userTenantId", "application", "exchangeRate", "requestTo"]

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
        """Create an instance of RequestMoneyParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of destination_payment_method
        if self.destination_payment_method:
            _dict['destinationPaymentMethod'] = self.destination_payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RequestMoneyParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "correlationId": obj.get("correlationId"),
            "destinationPaymentMethod": RaaSPaymentMethod.from_dict(obj.get("destinationPaymentMethod")) if obj.get("destinationPaymentMethod") is not None else None,
            "reason": obj.get("reason"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "senderCurrency": obj.get("senderCurrency"),
            "senderAmount": obj.get("senderAmount"),
            "recipientAmount": obj.get("recipientAmount"),
            "recipientCurrency": obj.get("recipientCurrency"),
            "bonusAmount": obj.get("bonusAmount"),
            "tenantId": obj.get("tenantId"),
            "userTenantId": obj.get("userTenantId"),
            "application": obj.get("application"),
            "exchangeRate": obj.get("exchangeRate"),
            "requestTo": obj.get("requestTo")
        })
        return _obj


