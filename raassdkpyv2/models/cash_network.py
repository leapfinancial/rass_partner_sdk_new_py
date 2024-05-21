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


from typing import Any, Dict
from pydantic import BaseModel, Field, StrictStr

class CashNetwork(BaseModel):
    """
    id: Unique Identifier of CashNetwork  name: Name of Network  cashProvider: Enum that identifies the type of provider use {Numi, Greendot, Inpamex, NumiCashDelivery, Incomm}   imageUrl: URL of image to identify this network  # noqa: E501
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    cash_provider: Dict[str, Any] = Field(..., alias="cashProvider")
    image_url: StrictStr = Field(..., alias="imageUrl")
    __properties = ["id", "name", "cashProvider", "imageUrl"]

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
    def from_json(cls, json_str: str) -> CashNetwork:
        """Create an instance of CashNetwork from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CashNetwork:
        """Create an instance of CashNetwork from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CashNetwork.parse_obj(obj)

        _obj = CashNetwork.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "cash_provider": obj.get("cashProvider"),
            "cashProvider": obj.get("cashProvider"),
            "image_url": obj.get("imageUrl"),
            "imageUrl": obj.get("imageUrl")
        })
        return _obj


