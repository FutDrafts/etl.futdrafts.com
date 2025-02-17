from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class TrophyInfo(TypedDict):
    league: str
    country: str
    season: str
    place: str

class TrophiesResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[TrophyInfo]

class TrophiesResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class TrophiesResponse499(TypedDict):
    message: str

class TrophiesResponse500(TypedDict):
    message: str

TrophiesResponse = Union[
    TrophiesResponse200,
    TrophiesResponse204,
    TrophiesResponse499,
    TrophiesResponse500
]
