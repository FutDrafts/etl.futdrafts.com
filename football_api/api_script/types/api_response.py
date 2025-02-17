from typing import TypedDict, Generic, TypeVar, Union, List, Optional

P = TypeVar("P")  
R = TypeVar("R") 

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class APIResponse(TypedDict, Generic[P, R]):
    get: str
    parameters: P
    errors: Union[List, ErrorReport]
    results: int
    paging: Paging
    response: Union[R, List, dict]

class FixtureStatus(TypedDict):
    short: str
    long: str
    type: str 
    description: str

class BirthInfo(TypedDict):
    date: str
    place: str
    country: str

class TeamInfo(TypedDict):
    id: int
    name: str
    logo: str

class CareerInfo(TypedDict):
    team: TeamInfo
    start: str
    end: Optional[str]

class CoachInfo(TypedDict):
    id: int
    name: str
    firstname: str
    lastname: str
    age: int
    birth: BirthInfo
    nationality: str
    weight: str
    photo: str
    team: TeamInfo
    career: List[CareerInfo]

class CountryInfo(TypedDict):
    name: str
    code: str
    flag: str

class FixturePeriods(TypedDict):
    first: Optional[int]
    second: Optional[int]

class FixtureVenue(TypedDict):
    id: int
    name: str
    city: str

class FixtureStatusInfo(TypedDict):
    long: str
    short: str
    elapsed: Union[int, None]
    extra: Union[int, None]

class FixtureDetails(TypedDict):
    id: int
    referee: Optional[str]
    timezone: str
    date: str
    timestamp: int
    periods: FixturePeriods
    venue: FixtureVenue
    status: FixtureStatusInfo

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
    extratime: GoalsInfo
    penalty: GoalsInfo

class FixtureResponseItem(TypedDict):
    fixture: FixtureDetails
    league: LeagueInfo
    teams: TeamsInfo
    goals: GoalsInfo
    score: ScoreDetails

class CoachResponse(APIResponse[dict, List[CoachInfo]]): pass
class CountriesResponse(APIResponse[dict, List[CountryInfo]]): pass
class FixturesRoundsResponse(APIResponse[dict, List[str]]): pass
class FixturesResponse(APIResponse[dict, List[FixtureResponseItem]]): pass
