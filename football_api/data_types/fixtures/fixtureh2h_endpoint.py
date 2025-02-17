from typing import TypedDict, List, Optional, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class Periods(TypedDict):
    first: int
    second: int

class Venue(TypedDict):
    id: int
    name: str
    city: str

class FixtureStatus(TypedDict):
    long: str
    short: str
    elapsed: int
    extra: Optional[int]

class FixtureDetails(TypedDict):
    id: int
    referee: str
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

class FixtureH2HItem(TypedDict):
    fixture: FixtureDetails
    league: LeagueInfo
    teams: TeamsInfo
    goals: GoalsInfo
    score: ScoreDetails

class FixtureH2HResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[FixtureH2HItem]

class FixtureH2HResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class FixtureH2HResponse499(TypedDict):
    message: str

class FixtureH2HResponse500(TypedDict):
    message: str

FixtureH2HResponse = Union[
    FixtureH2HResponse200,
    FixtureH2HResponse204,
    FixtureH2HResponse499,
    FixtureH2HResponse500
]
