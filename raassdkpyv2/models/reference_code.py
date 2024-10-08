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


from typing import Any, ClassVar, Dict, List, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ReferenceCode(BaseModel):
    """
    ReferenceCode
    """ # noqa: E501
    id: StrictStr
    operation_id: StrictStr = Field(description="internal Id of operation", alias="operationId")
    operation_code: StrictStr = Field(description="short id of operation", alias="operationCode")
    amount: Union[StrictFloat, StrictInt]
    currency: StrictStr = Field(description="Iso 3 for Curency (USD,MXN)")
    sender_name: StrictStr = Field(description="sender full name", alias="senderName")
    receiver_name: StrictStr = Field(description="receiver full name", alias="receiverName")
    network_id: StrictStr = Field(description="ID of cash operator. This can be obtained from Cash Operator", alias="networkId")
    operation_type: StrictStr = Field(alias="operationType")
    cash_provider: StrictStr = Field(description="can be (Numi, Greendot, Inpamex, NumiCashDelivery, Incomm) and it's obtained from Cash Network.", alias="cashProvider")
    code: StrictStr
    expiration_date: StrictStr = Field(alias="expirationDate")
    subscriber_id: StrictStr = Field(alias="subscriberId")
    operator_name: StrictStr = Field(alias="operatorName")
    network_name: StrictStr = Field(alias="networkName")
    image_url: StrictStr = Field(alias="imageUrl")
    image_circle_url: StrictStr = Field(alias="imageCircleUrl")
    __properties: ClassVar[List[str]] = ["id", "operationId", "operationCode", "amount", "currency", "senderName", "receiverName", "networkId", "operationType", "cashProvider", "code", "expirationDate", "subscriberId", "operatorName", "networkName", "imageUrl", "imageCircleUrl"]

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
        """Create an instance of ReferenceCode from a JSON string"""
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
        """Create an instance of ReferenceCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "operationId": obj.get("operationId"),
            "operationCode": obj.get("operationCode"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "senderName": obj.get("senderName"),
            "receiverName": obj.get("receiverName"),
            "networkId": obj.get("networkId"),
            "operationType": obj.get("operationType"),
            "cashProvider": obj.get("cashProvider"),
            "code": obj.get("code"),
            "expirationDate": obj.get("expirationDate"),
            "subscriberId": obj.get("subscriberId"),
            "operatorName": obj.get("operatorName"),
            "networkName": obj.get("networkName"),
            "imageUrl": obj.get("imageUrl"),
            "imageCircleUrl": obj.get("imageCircleUrl")
        })
        return _obj


