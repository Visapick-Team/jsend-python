from jsend.response import JsendResponse
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from jsend.fastapi.exception import  JSONResponse

class ExceptionMiddleware:

    def __init__(self, app) -> None:
        self.app = app
        self.app.add_exception_handler(HTTPException, self.http_exception_handler)

    def http_exception_handler(self, request, exc):
        
        payload = JsendResponse(
            status="error",
            message=exc.detail,
        )
        response = JSONResponse(
            payload.dict(exclude_none=True), status_code=exc.status_code
        )
        return response