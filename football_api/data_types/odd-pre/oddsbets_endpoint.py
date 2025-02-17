from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: str
    total: str

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class BetInfo(TypedDict):
    id: int
    name: str

class OddsBetsResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[BetInfo]

class OddsBetsResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class OddsBetsResponse499(TypedDict):
    message: str

class OddsBetsResponse500(TypedDict):
    message: str

OddsBetsResponse = Union[
    OddsBetsResponse200,
    OddsBetsResponse204,
    OddsBetsResponse499,
    OddsBetsResponse500
]
