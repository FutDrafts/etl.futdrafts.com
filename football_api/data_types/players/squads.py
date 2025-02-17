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

class PlayerInfo(TypedDict):
    id: int
    name: str
    age: int
    number: int
    position: str
    photo: str

class SquadItem(TypedDict):
    team: TeamInfo
    players: List[PlayerInfo]

class PlayerSquadResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[SquadItem]

class PlayerSquadResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class PlayerSquadResponse499(TypedDict):
    message: str

class PlayerSquadResponse500(TypedDict):
    message: str

PlayerSquadResponse = Union[
    PlayerSquadResponse200,
    PlayerSquadResponse204,
    PlayerSquadResponse499,
    PlayerSquadResponse500
]
