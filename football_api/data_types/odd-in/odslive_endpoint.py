from typing import TypedDict, List, Optional, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class FixtureStatus(TypedDict):
    long: str
    elapsed: int
    seconds: str

class FixtureInfo(TypedDict):
    id: int
    status: FixtureStatus

class LeagueInfo(TypedDict):
    id: int
    season: int

class TeamGoals(TypedDict):
    id: int
    goals: int

class TeamsInfo(TypedDict):
    home: TeamGoals
    away: TeamGoals

class MatchStatus(TypedDict):
    stopped: bool
    blocked: bool
    finished: bool

class OddValue(TypedDict):
    value: str
    odd: str
    handicap: str
    main: Optional[bool]
    suspended: Optional[bool]

class OddsInfo(TypedDict):
    id: int
    name: str
    values: List[OddValue]

class OddsLiveItem(TypedDict):
    fixture: FixtureInfo
    league: LeagueInfo
    teams: TeamsInfo
    status: MatchStatus
    update: str
    odds: List[OddsInfo]

class OddsLiveResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[OddsLiveItem]

class OddsLiveResponse204(TypedDict):
    get: str
    parameter: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class OddsLiveResponse499(TypedDict):
    message: str

class OddsLiveResponse500(TypedDict):
    message: str

OddsLiveResponse = Union[
    OddsLiveResponse200,
    OddsLiveResponse204,
    OddsLiveResponse499,
    OddsLiveResponse500
]
