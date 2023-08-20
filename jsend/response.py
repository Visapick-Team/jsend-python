from pydantic import BaseModel
from typing import Optional, Any


class JsendResponse(BaseModel):
    status: str
    data: Any

    # Error
    code: Optional[int]
    message: Optional[str]

    #  Pagination
    total: Optional[int]
    count: Optional[int]
    offset: Optional[int]


   