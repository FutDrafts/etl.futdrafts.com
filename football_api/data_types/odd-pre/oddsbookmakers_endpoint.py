from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class BookmakerInfo(TypedDict):
    id: int
    name: str

class OddsBookmakersResponse200(TypedDict):
    get: str
    parameters: List
    errors: List
    results: int
    paging: Paging
    response: List[BookmakerInfo]

class OddsBookmakersResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class OddsBookmakersResponse499(TypedDict):
    message: str

class OddsBookmakersResponse500(TypedDict):
    message: str

OddsBookmakersResponse = Union[
    OddsBookmakersResponse200,
    OddsBookmakersResponse204,
    OddsBookmakersResponse499,
    OddsBookmakersResponse500
]
