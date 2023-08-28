from pydantic import BaseModel
from typing import Optional, Any


class JsendBase:
    status: str
    data: Any

    # Error
    code: Optional[int] = None
    message: Optional[str] = None

    #  Pagination
    total: Optional[int] = None
    count: Optional[int] = None
    offset: Optional[int] = None


class JsendResponse(JsendBase, BaseModel):
    pass
