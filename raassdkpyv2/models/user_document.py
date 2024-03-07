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
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class UserDocument(BaseModel):
    """
    tsoa_sample No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  The version of the OpenAPI document: 1.1.0 Contact: alejamp@gmail.com  NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech). https://openapi-generator.tech Do not edit the class manually.  # noqa: E501
    """
    id: StrictStr = Field(...)
    type: Dict[str, Any] = Field(...)
    sub_type: Union[StrictFloat, StrictInt] = Field(..., alias="subType")
    number: StrictStr = Field(...)
    expiration_date: Optional[StrictStr] = Field(None, alias="expirationDate")
    issued_country: Optional[StrictStr] = Field(None, alias="issuedCountry")
    issued_date: Optional[StrictStr] = Field(None, alias="issuedDate")
    user_identity_data: Optional[Dict[str, Any]] = Field(None, alias="userIdentityData")
    date_time: Optional[datetime] = Field(None, alias="dateTime")
    __properties = ["id", "type", "subType", "number", "expirationDate", "issuedCountry", "issuedDate", "userIdentityData", "dateTime"]

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
    def from_json(cls, json_str: str) -> UserDocument:
        """Create an instance of UserDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserDocument:
        """Create an instance of UserDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserDocument.parse_obj(obj)

        _obj = UserDocument.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "sub_type": obj.get("subType"),
            "number": obj.get("number"),
            "expiration_date": obj.get("expirationDate"),
            "issued_country": obj.get("issuedCountry"),
            "issued_date": obj.get("issuedDate"),
            "user_identity_data": obj.get("userIdentityData"),
            "date_time": obj.get("dateTime")
        })
        return _obj

