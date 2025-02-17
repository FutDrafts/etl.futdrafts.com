from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class BetInfo(TypedDict):
    id: int
    name: str

class OddsLiveBetsResponse200(TypedDict):
    get: str
    parameters: List
    errors: List
    results: int
    paging: Paging
    response: List[BetInfo]

class OddsLiveBetsResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class OddsLiveBetsResponse499(TypedDict):
    message: str

class OddsLiveBetsResponse500(TypedDict):
    message: str

OddsLiveBetsResponse = Union[
    OddsLiveBetsResponse200,
    OddsLiveBetsResponse204,
    OddsLiveBetsResponse499,
    OddsLiveBetsResponse500
]
