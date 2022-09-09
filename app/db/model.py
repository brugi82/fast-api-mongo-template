from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
import datetime


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid objectid {v}")
        return ObjectId(v)


class MongoModel(BaseModel):
    id: Optional[PyObjectId] = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: lambda x: str(x), datetime: lambda x: x.isoformat()}

    def __init__(__pydantic_self__, **data):
        if not data:
            return data
        id = data.pop("_id", None)
        super().__init__(**dict(data, id=id))

    @classmethod
    def to_mongo(self, **kwargs):
        exclude_unset = kwargs.pop("exclude_unset", True)
        by_alias = kwargs.pop("by_alias", True)

        parsed = self.dict(
            exclude_unset=exclude_unset,
            by_alias=by_alias,
            **kwargs,
        )

        if "_id" not in parsed and "id" in parsed:
            parsed["_id"] = parsed.pop("id")

        return parsed
