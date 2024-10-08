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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ErrorsCIPProcess(BaseModel):
    """
    ErrorsCIPProcess
    """ # noqa: E501
    error_id_scan_date_expired: Optional[StrictStr] = Field(default=None, alias="ERROR_ID_SCAN_DATE_EXPIRED")
    error_ofac_not_valid: Optional[StrictStr] = Field(default=None, alias="ERROR_OFAC_NOT_VALID")
    error_face_match_not_valid: Optional[StrictStr] = Field(default=None, alias="ERROR_FACE_MATCH_NOT_VALID")
    error_photo_scan_id_required: Optional[StrictStr] = Field(default=None, alias="ERROR_PHOTO_SCAN_ID_REQUIRED")
    error_ocr_profile_match_not_valid: Optional[StrictStr] = Field(default=None, alias="ERROR_OCR_PROFILE_MATCH_NOT_VALID")
    __properties: ClassVar[List[str]] = ["ERROR_ID_SCAN_DATE_EXPIRED", "ERROR_OFAC_NOT_VALID", "ERROR_FACE_MATCH_NOT_VALID", "ERROR_PHOTO_SCAN_ID_REQUIRED", "ERROR_OCR_PROFILE_MATCH_NOT_VALID"]

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
        """Create an instance of ErrorsCIPProcess from a JSON string"""
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
        """Create an instance of ErrorsCIPProcess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ERROR_ID_SCAN_DATE_EXPIRED": obj.get("ERROR_ID_SCAN_DATE_EXPIRED"),
            "ERROR_OFAC_NOT_VALID": obj.get("ERROR_OFAC_NOT_VALID"),
            "ERROR_FACE_MATCH_NOT_VALID": obj.get("ERROR_FACE_MATCH_NOT_VALID"),
            "ERROR_PHOTO_SCAN_ID_REQUIRED": obj.get("ERROR_PHOTO_SCAN_ID_REQUIRED"),
            "ERROR_OCR_PROFILE_MATCH_NOT_VALID": obj.get("ERROR_OCR_PROFILE_MATCH_NOT_VALID")
        })
        return _obj


