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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class UserUpdateParams(BaseModel):
    """
    UserUpdateParams
    """
    email: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    middle_name: Optional[StrictStr] = Field(None, alias="middleName")
    second_last_name: Optional[StrictStr] = Field(None, alias="secondLastName")
    address1: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    place_id: Optional[StrictStr] = Field(None, alias="placeId")
    country: Optional[StrictStr] = None
    gender: Optional[StrictStr] = None
    dob: Optional[datetime] = None
    country_id: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    first_time: Optional[StrictBool] = Field(None, alias="firstTime")
    __properties = ["email", "firstName", "lastName", "middleName", "secondLastName", "address1", "address2", "placeId", "country", "gender", "dob", "country_id", "status", "firstTime"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('new', 'ready'):
            raise ValueError("must be one of enum values ('new', 'ready')")
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
    def from_json(cls, json_str: str) -> UserUpdateParams:
        """Create an instance of UserUpdateParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserUpdateParams:
        """Create an instance of UserUpdateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserUpdateParams.parse_obj(obj)

        _obj = UserUpdateParams.parse_obj({
            "email": obj.get("email"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "middle_name": obj.get("middleName"),
            "second_last_name": obj.get("secondLastName"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "place_id": obj.get("placeId"),
            "country": obj.get("country"),
            "gender": obj.get("gender"),
            "dob": obj.get("dob"),
            "country_id": obj.get("country_id"),
            "status": obj.get("status"),
            "first_time": obj.get("firstTime")
        })
        return _obj


