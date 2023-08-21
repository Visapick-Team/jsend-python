from pydantic import BaseModel
from typing import Optional, Any


class JsendBase:
    status: str
    data: Any

    # Error
    code: Optional[int]
    message: Optional[str]

    #  Pagination
    total: Optional[int]
    count: Optional[int]
    offset: Optional[int]


class JsendResponse(JsendBase, BaseModel):
    pass
