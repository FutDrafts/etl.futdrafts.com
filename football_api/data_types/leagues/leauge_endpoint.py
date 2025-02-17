from typing import TypedDict, List, Optional, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class FixturesCoverage(TypedDict):
    events: bool
    lineups: bool
    statistics_fixtures: bool
    statistics_players: bool

class Coverage(TypedDict):
    fixtures: FixturesCoverage
    standings: bool
    players: bool
    top_scorers: bool
    top_assists: bool
    top_cards: bool
    injuries: bool
    predictions: bool
    odds: bool

class SeasonInfo(TypedDict):
    year: int
    start: str
    end: str
    current: bool
    coverage: Coverage

class LeagueInfo(TypedDict):
    id: int
    name: str
    type: str
    logo: str

class CountryInfo(TypedDict):
    name: str
    code: str
    flag: str

class LeagueItem(TypedDict):
    league: LeagueInfo
    country: CountryInfo
    seasons: List[SeasonInfo]

class LeagueResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[LeagueItem]

class LeagueResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class LeagueResponse499(TypedDict):
    message: str

class LeagueResponse500(TypedDict):
    message: str

LeagueResponse = Union[
    LeagueResponse200,
    LeagueResponse204,
    LeagueResponse499,
    LeagueResponse500
]
