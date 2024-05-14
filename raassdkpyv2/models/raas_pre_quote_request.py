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


from typing import Any, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator

class RaasPreQuoteRequest(BaseModel):
    """
    RaasPreQuoteRequest
    """
    recipient_id: Optional[StrictStr] = Field(None, alias="RecipientId")
    subscriber_id: Optional[StrictStr] = Field(None, alias="SubscriberId")
    destination_payment_method: Optional[Any] = Field(..., alias="DestinationPaymentMethod")
    sender_country_code: StrictStr = Field(..., alias="SenderCountryCode")
    is_sender_amount: StrictBool = Field(..., alias="IsSenderAmount")
    amount: Union[StrictFloat, StrictInt] = Field(..., alias="Amount")
    operation_type: StrictStr = Field(..., alias="OperationType")
    product_type: StrictStr = Field(..., alias="ProductType")
    tennant_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="TennantFee")
    tenant_code: Optional[StrictStr] = Field(None, alias="TenantCode")
    __properties = ["RecipientId", "SubscriberId", "DestinationPaymentMethod", "SenderCountryCode", "IsSenderAmount", "Amount", "OperationType", "ProductType", "TennantFee", "TenantCode"]

    @validator('operation_type')
    def operation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SendFunds', 'RequestFunds', 'WalletLoad', 'WalletTransferOut', 'TopUp', 'RequestTopUp', 'SendFundsVirtualAgent', 'RequestFundsVirtualAgent', 'StorePayment'):
            raise ValueError("must be one of enum values ('SendFunds', 'RequestFunds', 'WalletLoad', 'WalletTransferOut', 'TopUp', 'RequestTopUp', 'SendFundsVirtualAgent', 'RequestFundsVirtualAgent', 'StorePayment')")
        return value

    @validator('product_type')
    def product_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Fund', 'Airtime', 'Loan', 'BillPay', 'NotApplicable', 'VirtualAgent', 'Wallet', 'StorePayment', 'NumiService'):
            raise ValueError("must be one of enum values ('Fund', 'Airtime', 'Loan', 'BillPay', 'NotApplicable', 'VirtualAgent', 'Wallet', 'StorePayment', 'NumiService')")
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
    def from_json(cls, json_str: str) -> RaasPreQuoteRequest:
        """Create an instance of RaasPreQuoteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if destination_payment_method (nullable) is None
        # and __fields_set__ contains the field
        if self.destination_payment_method is None and "destination_payment_method" in self.__fields_set__:
            _dict['DestinationPaymentMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RaasPreQuoteRequest:
        """Create an instance of RaasPreQuoteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RaasPreQuoteRequest.parse_obj(obj)

        _obj = RaasPreQuoteRequest.parse_obj({
            "recipient_id": obj.get("RecipientId"),
            "subscriber_id": obj.get("SubscriberId"),
            "destination_payment_method": obj.get("DestinationPaymentMethod"),
            "sender_country_code": obj.get("SenderCountryCode"),
            "is_sender_amount": obj.get("IsSenderAmount"),
            "amount": obj.get("Amount"),
            "operation_type": obj.get("OperationType"),
            "product_type": obj.get("ProductType"),
            "tennant_fee": obj.get("TennantFee"),
            "tenant_code": obj.get("TenantCode")
        })
        return _obj


