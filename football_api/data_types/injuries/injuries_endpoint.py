from typing import TypedDict, List, Optional, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class PlayerInfo(TypedDict):
    id: int
    name: str
    photo: str
    type: str
    reason: str

class TeamInfo(TypedDict):
    id: int
    name: str
    logo: str

class FixtureInfo(TypedDict):
    id: int
    timezone: str
    date: str
    timestamp: int

class LeagueInfo(TypedDict):
    id: int
    season: int
    name: str
    country: str
    logo: str
    flag: Optional[str]

class InjuryItem(TypedDict):
    player: PlayerInfo
    team: TeamInfo
    fixture: FixtureInfo
    league: LeagueInfo

class InjuriesResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[InjuryItem]

class InjuriesResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class InjuriesResponse499(TypedDict):
    message: str

class InjuriesResponse500(TypedDict):
    message: str

InjuriesResponse = Union[
    InjuriesResponse200,
    InjuriesResponse204,
    InjuriesResponse499,
    InjuriesResponse500
]
