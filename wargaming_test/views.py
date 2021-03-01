import pydantic
from aiohttp.web import Request
from aiohttp.web import Response
from aiohttp.web import json_response
from pydantic import BaseModel
from pydantic import Field

from wargaming_test import storages
from wargaming_test import utils


class QueryParams(BaseModel):
    """Валидатор параметров запроса"""
    start: int = Field(alias='from')
    end: int = Field(alias='to')


@utils.handle_exceptions(pydantic.ValidationError)
async def get_fibonacci(request: Request) -> Response:
    query_params = QueryParams(**request.rel_url.query)
    collection = storages.fibonacci_slice.get(**query_params.dict())
    return json_response({'items': collection})
