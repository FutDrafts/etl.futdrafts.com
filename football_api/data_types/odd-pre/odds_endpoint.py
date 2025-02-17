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
    name: str
    country: str
    logo: str
    flag: str
    season: int

class FixtureInfo(TypedDict):
    id: int
    timezone: str
    date: str
    timestamp: int

class BetValue(TypedDict):
    value: float
    odd: str

class BetInfo(TypedDict):
    id: int
    name: str
    values: List[BetValue]

class BookmakerInfo(TypedDict):
    id: int
    name: str
    bets: List[BetInfo]

class OddsItem(TypedDict):
    league: LeagueInfo
    fixture: FixtureInfo
    update: str
    bookmakers: List[BookmakerInfo]

class OddsResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[OddsItem]

class OddsResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class OddsResponse499(TypedDict):
    message: str

class OddsResponse500(TypedDict):
    message: str

OddsResponse = Union[
    OddsResponse200,
    OddsResponse204,
    OddsResponse499,
    OddsResponse500
]
