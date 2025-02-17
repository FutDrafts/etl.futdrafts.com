from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class SidelinedItem(TypedDict):
    type: str
    start: str
    end: str

class SidelinedResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[SidelinedItem]

class SidelinedResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class SidelinedResponse499(TypedDict):
    message: str

class SidelinedResponse500(TypedDict):
    message: str

SidelinedResponse = Union[
    SidelinedResponse200,
    SidelinedResponse204,
    SidelinedResponse499,
    SidelinedResponse500
]
