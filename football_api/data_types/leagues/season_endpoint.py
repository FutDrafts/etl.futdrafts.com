from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class SeasonResponse200(TypedDict):
    get: str
    parameters: List
    errors: List
    results: int
    paging: Paging
    response: List[int]

class SeasonResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class SeasonResponse499(TypedDict):
    message: str

class SeasonResponse500(TypedDict):
    message: str

SeasonResponse = Union[
    SeasonResponse200,
    SeasonResponse204,
    SeasonResponse499,
    SeasonResponse500
]
