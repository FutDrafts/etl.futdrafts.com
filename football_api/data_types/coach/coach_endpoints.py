from typing import TypedDict, List, Optional, Union

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
    height: str
    weight: str
    photo: str
    team: TeamInfo
    career: List[CareerInfo]

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class CoachesResponse200(TypedDict):
    get: str
    parameters: dict 
    errors: List
    results: int
    paging: Paging
    response: List[CoachInfo]

class CoachesResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class CoachesResponse499(TypedDict):
    message: str

class CoachesResponse500(TypedDict):
    message: str

CoachesResponse = Union[CoachesResponse200, CoachesResponse204, CoachesResponse499, CoachesResponse500]
