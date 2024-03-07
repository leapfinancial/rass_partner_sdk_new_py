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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class QuoteTransactionBase(BaseModel):
    """
    QuoteTransactionBase
    """
    sender_user_id: Optional[StrictStr] = Field(None, alias="senderUserId")
    sender_country_code: StrictStr = Field(..., alias="senderCountryCode")
    recipient_user_id: StrictStr = Field(..., alias="recipientUserId")
    recipient_country_code: StrictStr = Field(..., alias="recipientCountryCode")
    recipient_currency: StrictStr = Field(..., alias="recipientCurrency")
    recipient_amount: Union[StrictFloat, StrictInt] = Field(..., alias="recipientAmount")
    is_sender_amount: StrictBool = Field(..., alias="isSenderAmount")
    amount_currency: StrictStr = Field(..., alias="amountCurrency")
    amount: Union[StrictFloat, StrictInt] = Field(...)
    operation_type: Optional[Any] = Field(..., alias="operationType", description="\"SendFunds\"|\"RequestFunds\"|\"WalletLoad\"|\"WalletTransferOut\"|\"TopUp\"|\"RequestTopUp\"|\"SendFundsVirtualAgent\"|\"RequestFundsVirtualAgent\"|\"StorePayment\"")
    source_payment_method: Optional[Any] = Field(..., alias="sourcePaymentMethod")
    destination_payment_method: Optional[Any] = Field(None, alias="destinationPaymentMethod")
    tennant_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="tennantFee")
    __properties = ["senderUserId", "senderCountryCode", "recipientUserId", "recipientCountryCode", "recipientCurrency", "recipientAmount", "isSenderAmount", "amountCurrency", "amount", "operationType", "sourcePaymentMethod", "destinationPaymentMethod", "tennantFee"]

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
    def from_json(cls, json_str: str) -> QuoteTransactionBase:
        """Create an instance of QuoteTransactionBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if operation_type (nullable) is None
        # and __fields_set__ contains the field
        if self.operation_type is None and "operation_type" in self.__fields_set__:
            _dict['operationType'] = None

        # set to None if source_payment_method (nullable) is None
        # and __fields_set__ contains the field
        if self.source_payment_method is None and "source_payment_method" in self.__fields_set__:
            _dict['sourcePaymentMethod'] = None

        # set to None if destination_payment_method (nullable) is None
        # and __fields_set__ contains the field
        if self.destination_payment_method is None and "destination_payment_method" in self.__fields_set__:
            _dict['destinationPaymentMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QuoteTransactionBase:
        """Create an instance of QuoteTransactionBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QuoteTransactionBase.parse_obj(obj)

        _obj = QuoteTransactionBase.parse_obj({
            "sender_user_id": obj.get("senderUserId"),
            "sender_country_code": obj.get("senderCountryCode"),
            "recipient_user_id": obj.get("recipientUserId"),
            "recipient_country_code": obj.get("recipientCountryCode"),
            "recipient_currency": obj.get("recipientCurrency"),
            "recipient_amount": obj.get("recipientAmount"),
            "is_sender_amount": obj.get("isSenderAmount"),
            "amount_currency": obj.get("amountCurrency"),
            "amount": obj.get("amount"),
            "operation_type": obj.get("operationType"),
            "source_payment_method": obj.get("sourcePaymentMethod"),
            "destination_payment_method": obj.get("destinationPaymentMethod"),
            "tennant_fee": obj.get("tennantFee")
        })
        return _obj

