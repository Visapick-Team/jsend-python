from abc import ABC
from typing import Optional, Any, Sequence, Generic
from fastapi_pagination import LimitOffsetParams
from fastapi_pagination.bases import AbstractParams, AbstractPage
from fastapi_pagination.types import GreaterEqualOne, GreaterEqualZero
from fastapi_pagination.utils import create_pydantic_model
from jfast.response import ResponseMultiple, Model

class ResponsePagination(ResponseMultiple, AbstractPage[Model], Generic[Model], ABC):
    total: GreaterEqualZero


class Pagination(ResponsePagination[Model], Generic[Model]):
    limit: Optional[GreaterEqualOne]
    offset: Optional[GreaterEqualZero]

    __params_type__ = LimitOffsetParams

    @classmethod
    def create(
        cls,
        items: Sequence[Model],
        params: AbstractParams,
        *,
        total: Optional[int] = None,
        **kwargs: Any,
    ):
        raw_params = params.to_raw_params().as_limit_offset()

        return create_pydantic_model(
            cls,
            total=total,
            data=items,
            limit=raw_params.limit,
            offset=raw_params.offset,
            **kwargs,
        )
