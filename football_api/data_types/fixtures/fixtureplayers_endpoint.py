from typing import TypedDict, List, Optional, Union

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
    update: str

class PlayerInfo(TypedDict):
    id: int
    name: str
    photo: str

class GamesStats(TypedDict):
    minutes: int
    number: int
    position: str
    rating: str
    captain: bool
    substitute: bool

class ShotsStats(TypedDict):
    total: int
    on: int

class GoalsStats(TypedDict):
    total: Optional[int]
    conceded: int
    assists: Optional[int]
    saves: int

class PassesStats(TypedDict):
    total: int
    key: int
    accuracy: str

class TacklesStats(TypedDict):
    total: Optional[int]
    blocks: int
    interceptions: int

class DuelsStats(TypedDict):
    total: Optional[int]
    won: Optional[int]

class DribblesStats(TypedDict):
    attempts: int
    success: int
    past: Optional[int]

class FoulsStats(TypedDict):
    drawn: int
    committed: int

class CardsStats(TypedDict):
    yellow: int
    red: int

class PenaltyStats(TypedDict):
    won: Optional[int]
    committed: Optional[int]
    scored: int
    missed: int
    saved: int

class PlayerStatistics(TypedDict):
    games: GamesStats
    offsides: Optional[int]
    shots: ShotsStats
    goals: GoalsStats
    passes: PassesStats
    tackles: TacklesStats
    duels: DuelsStats
    dribbles: DribblesStats
    fouls: FoulsStats
    cards: CardsStats
    penalty: PenaltyStats

class PlayerWithStats(TypedDict):
    player: PlayerInfo
    statistics: List[PlayerStatistics]

class TeamWithPlayers(TypedDict):
    team: TeamInfo
    players: List[PlayerWithStats]

class FixturePlayerResponse200(TypedDict):
    get: str
    parameters: dict  
    errors: List
    results: int
    paging: Paging
    response: List[TeamWithPlayers]

class FixturePlayerResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class FixturePlayerResponse499(TypedDict):
    message: str

class FixturePlayerResponse500(TypedDict):
    message: str

FixturePlayerResponse = Union[
    FixturePlayerResponse200,
    FixturePlayerResponse204,
    FixturePlayerResponse499,
    FixturePlayerResponse500
]
