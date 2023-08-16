from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class JSendLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 12
    def get_paginated_response(self, data):
        return Response(
            {
                "status": "success",
                "data": data,
                "total": self.count,
                "count": len(data),
                "offset": self.offset,
            },
            status=HTTP_200_OK,
        )


class JSendRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):

        if data is not None and "status" in data:
            status = data.pop("status")
            if status == "success":
                response_data = {"status": "success", **data}
            elif status == "fail":
                response_data = {"status": "fail", "data": data}
            elif status == "error":
                response_data = {
                    "status": "error",
                    "message": data.get("message", "An error occurred"),
                }
                if "code" in data:
                    response_data["code"] = data["code"]
            else:
                response_data = {"status": "success", "data": data}
        else:
            response_data = {"status": "success", "data": data}
        return super().render(response_data, accepted_media_type, renderer_context)

