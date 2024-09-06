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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from raassdkpyv2.models.ignored_operation_data import IgnoredOperationData
from raassdkpyv2.models.operation_user_detail import OperationUserDetail
from raassdkpyv2.models.payment_method_response import PaymentMethodResponse
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """ # noqa: E501
    currency: Optional[StrictStr] = None
    plat_id: Optional[StrictStr] = Field(default=None, alias="platId")
    correlation_id: StrictStr = Field(alias="correlationId")
    created_at: datetime = Field(alias="createdAt")
    amount: Union[StrictFloat, StrictInt]
    status: StrictStr
    status_details: Optional[StrictStr] = Field(default=None, alias="statusDetails")
    mobile_status: Optional[StrictStr] = Field(default=None, alias="mobileStatus")
    reason: Optional[StrictStr] = None
    code: StrictStr
    recipient_amout: Union[StrictFloat, StrictInt] = Field(alias="recipientAmout")
    sender_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="senderAmount")
    sender_currency: Optional[StrictStr] = Field(default=None, alias="senderCurrency")
    recipient_currency: Optional[StrictStr] = Field(default=None, alias="recipientCurrency")
    source_payment_method: Optional[PaymentMethodResponse] = Field(default=None, alias="sourcePaymentMethod")
    destination_payment_method: Optional[PaymentMethodResponse] = Field(default=None, alias="destinationPaymentMethod")
    source_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sourceFee")
    transaction_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="transactionFee")
    destination_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="destinationFee")
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="exchangeRate")
    estimated_exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="estimatedExchangeRate")
    has_reference_code: Optional[StrictBool] = Field(default=None, alias="hasReferenceCode")
    from_user: OperationUserDetail = Field(alias="fromUser")
    to_user: OperationUserDetail = Field(alias="toUser")
    attribution_link: Optional[StrictStr] = Field(default=None, alias="attributionLink")
    is_ignored: Optional[StrictBool] = Field(default=None, alias="isIgnored")
    ignored_data: Optional[IgnoredOperationData] = Field(default=None, alias="ignoredData")
    tenantfee: Optional[Union[StrictFloat, StrictInt]] = None
    total_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalAmount")
    tax: Optional[Union[StrictFloat, StrictInt]] = None
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    is_landing_port_flow: Optional[StrictBool] = Field(default=None, alias="isLandingPortFlow")
    landing_port_url: Optional[StrictStr] = Field(default=None, alias="landingPortUrl")
    __properties: ClassVar[List[str]] = ["currency", "platId", "correlationId", "createdAt", "amount", "status", "statusDetails", "mobileStatus", "reason", "code", "recipientAmout", "senderAmount", "senderCurrency", "recipientCurrency", "sourcePaymentMethod", "destinationPaymentMethod", "sourceFee", "transactionFee", "destinationFee", "exchangeRate", "estimatedExchangeRate", "hasReferenceCode", "fromUser", "toUser", "attributionLink", "isIgnored", "ignoredData", "tenantfee", "totalAmount", "tax", "userId", "isLandingPortFlow", "landingPortUrl"]

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
        """Create an instance of PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_payment_method
        if self.source_payment_method:
            _dict['sourcePaymentMethod'] = self.source_payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_payment_method
        if self.destination_payment_method:
            _dict['destinationPaymentMethod'] = self.destination_payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of from_user
        if self.from_user:
            _dict['fromUser'] = self.from_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_user
        if self.to_user:
            _dict['toUser'] = self.to_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ignored_data
        if self.ignored_data:
            _dict['ignoredData'] = self.ignored_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency": obj.get("currency"),
            "platId": obj.get("platId"),
            "correlationId": obj.get("correlationId"),
            "createdAt": obj.get("createdAt"),
            "amount": obj.get("amount"),
            "status": obj.get("status"),
            "statusDetails": obj.get("statusDetails"),
            "mobileStatus": obj.get("mobileStatus"),
            "reason": obj.get("reason"),
            "code": obj.get("code"),
            "recipientAmout": obj.get("recipientAmout"),
            "senderAmount": obj.get("senderAmount"),
            "senderCurrency": obj.get("senderCurrency"),
            "recipientCurrency": obj.get("recipientCurrency"),
            "sourcePaymentMethod": PaymentMethodResponse.from_dict(obj.get("sourcePaymentMethod")) if obj.get("sourcePaymentMethod") is not None else None,
            "destinationPaymentMethod": PaymentMethodResponse.from_dict(obj.get("destinationPaymentMethod")) if obj.get("destinationPaymentMethod") is not None else None,
            "sourceFee": obj.get("sourceFee"),
            "transactionFee": obj.get("transactionFee"),
            "destinationFee": obj.get("destinationFee"),
            "exchangeRate": obj.get("exchangeRate"),
            "estimatedExchangeRate": obj.get("estimatedExchangeRate"),
            "hasReferenceCode": obj.get("hasReferenceCode"),
            "fromUser": OperationUserDetail.from_dict(obj.get("fromUser")) if obj.get("fromUser") is not None else None,
            "toUser": OperationUserDetail.from_dict(obj.get("toUser")) if obj.get("toUser") is not None else None,
            "attributionLink": obj.get("attributionLink"),
            "isIgnored": obj.get("isIgnored"),
            "ignoredData": IgnoredOperationData.from_dict(obj.get("ignoredData")) if obj.get("ignoredData") is not None else None,
            "tenantfee": obj.get("tenantfee"),
            "totalAmount": obj.get("totalAmount"),
            "tax": obj.get("tax"),
            "userId": obj.get("userId"),
            "isLandingPortFlow": obj.get("isLandingPortFlow"),
            "landingPortUrl": obj.get("landingPortUrl")
        })
        return _obj


