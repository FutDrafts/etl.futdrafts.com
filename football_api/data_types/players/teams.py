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

class PlayerTeamItem(TypedDict):
    team: TeamInfo
    seasons: List[int]

class PlayerTeamResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[PlayerTeamItem]

class PlayerTeamResponse204(TypedDict):
    get: str
    parameter: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class PlayerTeamResponse499(TypedDict):
    message: str

class PlayerTeamResponse500(TypedDict):
    message: str

PlayerTeamResponse = Union[
    PlayerTeamResponse200,
    PlayerTeamResponse204,
    PlayerTeamResponse499,
    PlayerTeamResponse500
]
