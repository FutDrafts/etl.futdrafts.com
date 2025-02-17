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
    code: str
    country: str
    founded: int
    national: bool
    logo: str

class VenueInfo(TypedDict):
    id: int
    name: str
    city: str
    capacity: int
    surface: str
    image: str

class TeamResponseItem(TypedDict):
    team: TeamInfo
    venue: VenueInfo

class TeamInfoResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[TeamResponseItem]

class TeamInfoResponse204(TypedDict):
    get: str
    parameters: dict
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class TeamInfoResponse499(TypedDict):
    message: str

class TeamInfoResponse500(TypedDict):
    message: str

TeamInfoResponse = Union[
    TeamInfoResponse200,
    TeamInfoResponse204,
    TeamInfoResponse499,
    TeamInfoResponse500
]
