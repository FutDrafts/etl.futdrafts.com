from typing import TypedDict, List, Optional, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class WinnerInfo(TypedDict):
    id: int
    name: str
    comment: str

class GoalsInfo(TypedDict):
    home: str
    away: str

class PercentInfo(TypedDict):
    home: str
    draw: str
    away: str

class Predictions(TypedDict):
    winner: WinnerInfo
    win_or_draw: bool
    under_over: str
    goals: GoalsInfo
    advice: str
    percent: PercentInfo

class LeagueInfo(TypedDict):
    id: int
    name: str
    country: str
    logo: str
    flag: str
    season: int

class GoalsTotalAverage(TypedDict):
    total: int
    average: float

class LastFiveStats(TypedDict):
    form: str
    att: str
    def_: str
    goals: dict

class FixturesStats(TypedDict):
    played: dict
    wins: dict
    draws: dict
    loses: dict

class GoalsStats(TypedDict):
    for_: dict
    against: dict

class StreakStats(TypedDict):
    wins: int
    draws: int
    loses: int

class BiggestStats(TypedDict):
    streak: StreakStats
    wins: dict
    loses: dict
    goals: dict

class CleanSheetStats(TypedDict):
    home: int
    away: int
    total: int

class FailedToScoreStats(TypedDict):
    home: int
    away: int
    total: int

class LeagueTeamStats(TypedDict):
    form: str
    fixtures: FixturesStats
    goals: GoalsStats
    biggest: BiggestStats
    clean_sheet: CleanSheetStats
    failed_to_score: FailedToScoreStats

class TeamInfo(TypedDict):
    id: int
    name: str
    logo: str
    last_5: LastFiveStats
    league: LeagueTeamStats

class Teams(TypedDict):
    home: TeamInfo
    away: TeamInfo

class ComparisonStats(TypedDict):
    form: dict
    att: dict
    def_: dict
    poisson_distribution: dict
    h2h: dict
    goals: dict
    total: dict

class PeriodsInfo(TypedDict):
    first: int
    second: int

class VenueInfo(TypedDict):
    id: Optional[int]
    name: str
    city: Optional[str]

class FixtureStatus(TypedDict):
    long: str
    short: str
    elapsed: int
    extra: Optional[int]

class FixtureInfo(TypedDict):
    id: int
    referee: str
    timezone: str
    date: str
    timestamp: int
    periods: PeriodsInfo
    venue: VenueInfo
    status: FixtureStatus

class MatchTeams(TypedDict):
    home: dict
    away: dict

class MatchGoals(TypedDict):
    home: int
    away: int

class ScoreInfo(TypedDict):
    halftime: dict
    fulltime: dict
    extratime: Optional[dict]
    penalty: Optional[dict]

class H2HItem(TypedDict):
    fixture: FixtureInfo
    league: LeagueInfo
    teams: MatchTeams
    goals: MatchGoals
    score: ScoreInfo

class PredictionItem(TypedDict):
    predictions: Predictions
    league: LeagueInfo
    teams: Teams
    comparison: ComparisonStats
    h2h: List[H2HItem]

class PredictionResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[PredictionItem]

class PredictionResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class PredictionResponse499(TypedDict):
    message: str

class PredictionResponse500(TypedDict):
    message: str

PredictionResponse = Union[
    PredictionResponse200,
    PredictionResponse204,
    PredictionResponse499,
    PredictionResponse500
]
