from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class LeagueInfo(TypedDict):
    id: int
    season: int

class FixtureInfo(TypedDict):
    id: int
    date: str
    timestamp: int

class OddsMappingItem(TypedDict):
    league: LeagueInfo
    fixture: FixtureInfo
    update: str

class OddsMappingResponse200(TypedDict):
    get: str
    parameters: List
    errors: List
    results: int
    paging: Paging
    response: List[OddsMappingItem]

class OddsMappingResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class OddsMappingResponse499(TypedDict):
    message: str

class OddsMappingResponse500(TypedDict):
    message: str

OddsMappingResponse = Union[
    OddsMappingResponse200,
    OddsMappingResponse204,
    OddsMappingResponse499,
    OddsMappingResponse500
]
