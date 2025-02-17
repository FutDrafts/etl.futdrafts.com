from typing import TypedDict, List, Optional, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class PlayerColors(TypedDict):
    primary: str
    number: str
    border: str

class TeamColors(TypedDict):
    player: PlayerColors
    goalkeeper: PlayerColors

class TeamInfo(TypedDict):
    id: int
    name: str
    logo: str
    colors: TeamColors

class PlayerDetails(TypedDict):
    id: int
    name: str
    number: int
    pos: str
    grid: Optional[str]

class StartXI(TypedDict):
    player: PlayerDetails

class Substitutes(TypedDict):
    player: PlayerDetails

class CoachInfo(TypedDict):
    id: int
    name: str
    photo: str

class FixtureLineup(TypedDict):
    team: TeamInfo
    formation: str
    startXI: List[StartXI]
    substitutes: List[Substitutes]
    coach: CoachInfo

class FixtureLineupsResponse200(TypedDict):
    get: str
    parameters: dict 
    errors: List
    results: int
    paging: Paging
    response: List[FixtureLineup]

class FixtureLineupsResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class FixtureLineupsResponse499(TypedDict):
    message: str

class FixtureLineupsResponse500(TypedDict):
    message: str

FixtureLineupsResponse = Union[
    FixtureLineupsResponse200,
    FixtureLineupsResponse204,
    FixtureLineupsResponse499,
    FixtureLineupsResponse500
]
