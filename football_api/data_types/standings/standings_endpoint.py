from typing import TypedDict, List, Union

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

class GoalsInfo(TypedDict):
    for_: int
    against: int

class RecordStats(TypedDict):
    played: int
    win: int
    draw: int
    lose: int
    goals: GoalsInfo

class StandingsItem(TypedDict):
    rank: int
    team: TeamInfo
    points: int
    goalsDiff: int
    group: str
    form: str
    status: str
    description: str
    all: RecordStats
    home: RecordStats
    away: RecordStats
    update: str

class LeagueInfo(TypedDict):
    id: int
    name: str
    country: str
    logo: str
    flag: str
    season: int
    standings: List[List[StandingsItem]]

class StandingsResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[LeagueInfo]

class StandingsResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class StandingsResponse499(TypedDict):
    message: str

class StandingsResponse500(TypedDict):
    message: str

StandingsResponse = Union[
    StandingsResponse200,
    StandingsResponse204,
    StandingsResponse499,
    StandingsResponse500
]
