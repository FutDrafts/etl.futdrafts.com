from typing import TypedDict, List, Optional, Union
from football_api.data_types.types.players_type import SoccerPlayer

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

class LeagueInfo(TypedDict):
    id: int
    name: str
    country: str
    logo: str
    flag: str
    season: int

class GamesInfo(TypedDict):
    appearences: int
    lineups: int
    minutes: int
    number: Optional[int]
    position: str
    rating: str
    captain: bool

class SubstitutesInfo(TypedDict):
    in_: int
    out: int
    bench: int

class ShotsInfo(TypedDict):
    total: int
    on: int

class GoalsInfo(TypedDict):
    total: int
    conceded: Optional[int]
    assists: int
    saves: int

class PassesInfo(TypedDict):
    total: int
    key: int
    accuracy: int

class TacklesInfo(TypedDict):
    total: int
    blocks: int
    interceptions: int

class DuelsInfo(TypedDict):
    total: int
    won: int

class DribblesInfo(TypedDict):
    attempts: int
    success: int
    past: Optional[int]

class FoulsInfo(TypedDict):
    drawn: int
    committed: int

class CardsInfo(TypedDict):
    yellow: int
    yellowred: int
    red: int

class PenaltyInfo(TypedDict):
    won: int
    commited: Optional[int]
    scored: int
    missed: int
    saved: Optional[int]

class StatisticsItem(TypedDict):
    team: TeamInfo
    league: LeagueInfo
    games: GamesInfo
    substitutes: SubstitutesInfo
    shots: ShotsInfo
    goals: GoalsInfo
    passes: PassesInfo
    tackles: TacklesInfo
    duels: DuelsInfo
    dribbles: DribblesInfo
    fouls: FoulsInfo
    cards: CardsInfo
    penalty: PenaltyInfo

class PlayerTopScorersItem(TypedDict):
    player: SoccerPlayer
    statistics: List[StatisticsItem]

class PlayerTopScorersResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[PlayerTopScorersItem]

class PlayerTopScorersResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class PlayerTopScorersResponse499(TypedDict):
    message: str

class PlayerTopScorersResponse500(TypedDict):
    message: str

PlayerTopScorersResponse = Union[
    PlayerTopScorersResponse200,
    PlayerTopScorersResponse204,
    PlayerTopScorersResponse499,
    PlayerTopScorersResponse500
]
