from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from jsend.response import JsendResponse

class JsendException(APIException):
    def __init__(self, detail=None, status_code=None, **kwargs):
        self.detail = detail or self.message
        self.code = status_code or self.status_code
        super().__init__(self.detail, self.status_code)

    def __str__(self):
        return str(self.detail)


class NotFoundException(JsendException):
    message = "Object were not found"
    status_code = 404


class PageNotFoundException(JsendException):
    message = "Page not found"
    status_code = 404


class PermissionDeniedException(JsendException):
    message = "Permission Denied."
    status_code = 403


class InternalException(JsendException):
    message = "Internal error."
    status_code = 500


def handler404(request, exception):
    raise PageNotFoundException()


def jsend_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if isinstance(exc, JsendException):
        data = JsendResponse(status="error", message=exc.detail)
        return Response(data.dict(exclude_none=True), status=exc.status_code)
    elif isinstance(response, Response):
        if isinstance(response.data, list):
            detail = response.data
        elif isinstance(response.data, dict):
            detail = str(response.data["detail"])
        else:
            detail = response.data["detail"]

        response.data = JsendResponse(status="error", message=detail).dict(
            exclude_none=True
        )

    return response
