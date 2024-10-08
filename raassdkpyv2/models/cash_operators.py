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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from raassdkpyv2.models.cash_location import CashLocation
from raassdkpyv2.models.cash_network import CashNetwork
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CashOperators(BaseModel):
    """
    id: Unique Identifier of CashOperator  networkId: Unique Identifier of the CashOperator’s Store Chain.  ExternalId??  network: List of Networks associated to this operator  country: Country code of this Operator  name: Name of this operator  imageUrl: URL of image to identify this operator  location: List of Locatios associated to this operator  cashAccountType:  Enum that identifies the type of network {CREDIT, PREPAID}   imageCircleUrl: URL of image to identify this operator (circle shape)
    """ # noqa: E501
    id: StrictStr
    external_id: StrictStr = Field(alias="externalId")
    network: List[CashNetwork]
    country: StrictStr
    name: StrictStr
    image_url: StrictStr = Field(alias="imageUrl")
    location: List[CashLocation]
    cash_account_type: Dict[str, Any] = Field(alias="cashAccountType")
    image_circle_url: StrictStr = Field(alias="imageCircleUrl")
    __properties: ClassVar[List[str]] = ["id", "externalId", "network", "country", "name", "imageUrl", "location", "cashAccountType", "imageCircleUrl"]

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
        """Create an instance of CashOperators from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in network (list)
        _items = []
        if self.network:
            for _item in self.network:
                if _item:
                    _items.append(_item.to_dict())
            _dict['network'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in location (list)
        _items = []
        if self.location:
            for _item in self.location:
                if _item:
                    _items.append(_item.to_dict())
            _dict['location'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CashOperators from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "externalId": obj.get("externalId"),
            "network": [CashNetwork.from_dict(_item) for _item in obj.get("network")] if obj.get("network") is not None else None,
            "country": obj.get("country"),
            "name": obj.get("name"),
            "imageUrl": obj.get("imageUrl"),
            "location": [CashLocation.from_dict(_item) for _item in obj.get("location")] if obj.get("location") is not None else None,
            "cashAccountType": obj.get("cashAccountType"),
            "imageCircleUrl": obj.get("imageCircleUrl")
        })
        return _obj


