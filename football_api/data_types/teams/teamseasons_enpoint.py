from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class TeamSeasonsResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[int]

class TeamSeasonsResponse204(TypedDict):
    get: str
    parameters: dict
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class TeamSeasonsResponse499(TypedDict):
    message: str

class TeamSeasonsResponse500(TypedDict):
    message: str

TeamSeasonsResponse = Union[
    TeamSeasonsResponse200,
    TeamSeasonsResponse204,
    TeamSeasonsResponse499,
    TeamSeasonsResponse500
]
