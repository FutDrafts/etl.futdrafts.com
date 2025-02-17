from typing import TypedDict, List, Optional, Union, Any

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class Periods(TypedDict):
    first: int
    second: Optional[Any]  

class Venue(TypedDict):
    id: int
    name: str
    city: str

class FixtureStatus(TypedDict):
    long: str
    short: str
    elapsed: int
    extra: Optional[Any]  

class FixtureDetails(TypedDict):
    id: int
    referee: Optional[Any]  
    timezone: str
    date: str
    timestamp: int
    periods: Periods
    venue: Venue
    status: FixtureStatus

class LeagueInfo(TypedDict):
    id: int
    name: str
    country: str
    logo: str
    flag: str
    season: int
    round: str

class TeamData(TypedDict):
    id: int
    name: str
    logo: str
    winner: bool

class TeamsInfo(TypedDict):
    home: TeamData
    away: TeamData

class GoalsInfo(TypedDict):
    home: int
    away: int

class ScoreDetails(TypedDict):
    halftime: GoalsInfo
    fulltime: GoalsInfo
    extratime: Optional[GoalsInfo]
    penalty: Optional[GoalsInfo]

class FixtureItem(TypedDict):
    fixture: FixtureDetails
    league: LeagueInfo
    teams: TeamsInfo
    goals: GoalsInfo
    score: ScoreDetails

class FixturesResponse200(TypedDict):
    get: str
    parameters: dict  
    errors: List
    results: int
    paging: Paging
    response: List[FixtureItem]

class FixturesResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class FixturesResponse499(TypedDict):
    message: str

class FixturesResponse500(TypedDict):
    message: str

FixturesResponse = Union[
    FixturesResponse200,
    FixturesResponse204,
    FixturesResponse499,
    FixturesResponse500
]
