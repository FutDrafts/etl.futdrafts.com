from typing import TypedDict, List, Union, Optional, Any

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class TeamInfo(TypedDict):
    id: int
    name: str
    logo: str

class Statistic(TypedDict):
    type: str
    value: Optional[Union[int, str]] 

class TeamStatistics(TypedDict):
    team: TeamInfo
    statistics: List[Statistic]

class FixtureStatsResponse200(TypedDict):
    get: str
    parameters: dict  
    errors: List
    results: int
    paging: Paging
    response: List[TeamStatistics]

class FixtureStatsResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class FixtureStatsResponse499(TypedDict):
    message: str

class FixtureStatsResponse500(TypedDict):
    message: str

FixtureStatsResponse = Union[
    FixtureStatsResponse200,
    FixtureStatsResponse204,
    FixtureStatsResponse499,
    FixtureStatsResponse500
]
