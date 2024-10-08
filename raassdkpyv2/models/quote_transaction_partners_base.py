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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QuoteTransactionPartnersBase(BaseModel):
    """
    QuoteTransactionPartnersBase
    """ # noqa: E501
    recipient_user_id: StrictStr = Field(alias="recipientUserId")
    currency: StrictStr
    amount: Union[StrictFloat, StrictInt]
    is_sender_amount: StrictBool = Field(alias="isSenderAmount")
    source_payment_method_id: Optional[StrictStr] = Field(default=None, alias="sourcePaymentMethodId")
    source_payment_method: Optional[Any] = Field(default=None, alias="sourcePaymentMethod")
    destination_payment_method_id: Optional[StrictStr] = Field(default=None, alias="destinationPaymentMethodId")
    destination_payment_method: Optional[Any] = Field(default=None, alias="destinationPaymentMethod")
    __properties: ClassVar[List[str]] = ["recipientUserId", "currency", "amount", "isSenderAmount", "sourcePaymentMethodId", "sourcePaymentMethod", "destinationPaymentMethodId", "destinationPaymentMethod"]

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
        """Create an instance of QuoteTransactionPartnersBase from a JSON string"""
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
        # set to None if source_payment_method (nullable) is None
        # and model_fields_set contains the field
        if self.source_payment_method is None and "source_payment_method" in self.model_fields_set:
            _dict['sourcePaymentMethod'] = None

        # set to None if destination_payment_method (nullable) is None
        # and model_fields_set contains the field
        if self.destination_payment_method is None and "destination_payment_method" in self.model_fields_set:
            _dict['destinationPaymentMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of QuoteTransactionPartnersBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recipientUserId": obj.get("recipientUserId"),
            "currency": obj.get("currency"),
            "amount": obj.get("amount"),
            "isSenderAmount": obj.get("isSenderAmount"),
            "sourcePaymentMethodId": obj.get("sourcePaymentMethodId"),
            "sourcePaymentMethod": obj.get("sourcePaymentMethod"),
            "destinationPaymentMethodId": obj.get("destinationPaymentMethodId"),
            "destinationPaymentMethod": obj.get("destinationPaymentMethod")
        })
        return _obj


