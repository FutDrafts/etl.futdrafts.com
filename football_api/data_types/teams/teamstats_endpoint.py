from typing import TypedDict, List, Dict, Union

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

class TeamInfo(TypedDict):
    id: int
    name: str
    logo: str

class FixturesStats(TypedDict):
    played: Dict[str, int]
    wins: Dict[str, int]
    draws: Dict[str, int]
    loses: Dict[str, int]

class GoalsMinuteStats(TypedDict):
    total: int
    percentage: str

class GoalsStats(TypedDict):
    total: Dict[str, int]
    average: Dict[str, str]
    minute: Dict[str, GoalsMinuteStats]
    under_over: Dict[str, Dict[str, int]]

class BiggestStats(TypedDict):
    streak: Dict[str, int]
    wins: Dict[str, str]
    loses: Dict[str, str]
    goals: Dict[str, Dict[str, int]]

class CleanSheetStats(TypedDict):
    home: int
    away: int
    total: int

class FailedToScoreStats(TypedDict):
    home: int
    away: int
    total: int

class PenaltyStats(TypedDict):
    scored: Dict[str, Union[int, str]]
    missed: Dict[str, Union[int, str]]
    total: int

class LineupStats(TypedDict):
    formation: str
    played: int

class CardsStats(TypedDict):
    yellow: Dict[str, GoalsMinuteStats]
    red: Dict[str, GoalsMinuteStats]

class TeamStatsResponseItem(TypedDict):
    league: LeagueInfo
    team: TeamInfo
    form: str
    fixtures: FixturesStats
    goals: Dict[str, GoalsStats]
    biggest: BiggestStats
    clean_sheet: CleanSheetStats
    failed_to_score: FailedToScoreStats
    penalty: PenaltyStats
    lineups: List[LineupStats]
    cards: CardsStats

class TeamStatsResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: TeamStatsResponseItem

class TeamStatsResponse204(TypedDict):
    get: str
    parameters: dict
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class TeamStatsResponse499(TypedDict):
    message: str

class TeamStatsResponse500(TypedDict):
    message: str

TeamStatsResponse = Union[
    TeamStatsResponse200,
    TeamStatsResponse204,
    TeamStatsResponse499,
    TeamStatsResponse500
]
