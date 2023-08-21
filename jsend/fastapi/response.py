from typing import TypeVar, Generic, List, Any
from pydantic import BaseModel
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field
from jsend.response import JsendBase


Model = TypeVar("Model", bound=BaseModel)


def get_default_status() -> str:
    return "success"


class BaseGenericResponse(GenericModel, JsendBase):
    status: str = Field(default_factory=get_default_status)
    message: Any | None


class GenericSingleResponse(BaseGenericResponse, Generic[Model]):
    data: Model


class GenericErrorResponse(BaseGenericResponse, Generic[Model]):
    data: Any


class GenericMultipleResponse(BaseGenericResponse, Generic[Model]):
    data: List[Model]


class ResponseMultiple(GenericMultipleResponse, GenericModel, Generic[Model]):
    pass


class Response(GenericSingleResponse, GenericModel, Generic[Model]):
    pass


class ErrorResponse(GenericErrorResponse, GenericModel, Generic[Model]):
    pass
