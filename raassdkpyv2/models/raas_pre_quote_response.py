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


from typing import List
from pydantic import BaseModel, Field, conlist
from raassdkpyv2.models.raas_pre_quote_values import RaasPreQuoteValues

class RaasPreQuoteResponse(BaseModel):
    """
    RaasPreQuoteResponse
    """
    quotes: List[RaasPreQuoteValues] = Field(..., alias="Quotes")
    __properties = ["Quotes"]

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
    def from_json(cls, json_str: str) -> RaasPreQuoteResponse:
        """Create an instance of RaasPreQuoteResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in quotes (list)
        _items = []
        if self.quotes:
            for _item in self.quotes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Quotes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RaasPreQuoteResponse:
        """Create an instance of RaasPreQuoteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RaasPreQuoteResponse.parse_obj(obj)

        _obj = RaasPreQuoteResponse.parse_obj({
            "quotes": [RaasPreQuoteValues.from_dict(_item) for _item in obj.get("Quotes")] if obj.get("Quotes") is not None else None
        })
        return _obj


