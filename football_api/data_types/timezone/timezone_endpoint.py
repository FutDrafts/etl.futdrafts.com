from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class TimeZoneResponse200(TypedDict):
    get: str
    parameters: List
    errors: List
    results: int
    paging: dict
    response: List[str]

class TimeZoneResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class TimeZoneResponse499(TypedDict):
    message: str

class TimeZoneResponse500(TypedDict):
    message: str

TimeZoneResponse = Union[
    TimeZoneResponse200,
    TimeZoneResponse204,
    TimeZoneResponse499,
    TimeZoneResponse500
]
