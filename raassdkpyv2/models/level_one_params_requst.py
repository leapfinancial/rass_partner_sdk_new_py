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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LevelOneParamsRequst(BaseModel):
    """
    LevelOneParamsRequst
    """ # noqa: E501
    zip_code: StrictStr = Field(alias="zipCode")
    place_detail: Optional[StrictStr] = Field(default=None, alias="placeDetail")
    city: StrictStr
    address4: Optional[StrictStr] = None
    address3: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    address1: StrictStr
    call_location_longitude: Union[StrictFloat, StrictInt] = Field(alias="callLocationLongitude")
    call_location_latitude: Union[StrictFloat, StrictInt] = Field(alias="callLocationLatitude")
    country_code: StrictStr = Field(alias="countryCode")
    state: StrictStr
    date_of_birth: Optional[StrictStr] = Field(default=None, alias="dateOfBirth")
    gender: Optional[StrictStr] = None
    birth_state: Optional[StrictStr] = Field(default=None, alias="birthState")
    user_id: StrictStr = Field(alias="userId")
    __properties: ClassVar[List[str]] = ["zipCode", "placeDetail", "city", "address4", "address3", "address2", "address1", "callLocationLongitude", "callLocationLatitude", "countryCode", "state", "dateOfBirth", "gender", "birthState", "userId"]

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
        """Create an instance of LevelOneParamsRequst from a JSON string"""
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
        """Create an instance of LevelOneParamsRequst from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "zipCode": obj.get("zipCode"),
            "placeDetail": obj.get("placeDetail"),
            "city": obj.get("city"),
            "address4": obj.get("address4"),
            "address3": obj.get("address3"),
            "address2": obj.get("address2"),
            "address1": obj.get("address1"),
            "callLocationLongitude": obj.get("callLocationLongitude"),
            "callLocationLatitude": obj.get("callLocationLatitude"),
            "countryCode": obj.get("countryCode"),
            "state": obj.get("state"),
            "dateOfBirth": obj.get("dateOfBirth"),
            "gender": obj.get("gender"),
            "birthState": obj.get("birthState"),
            "userId": obj.get("userId")
        })
        return _obj


