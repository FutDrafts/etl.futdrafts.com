from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class BirthInfo(TypedDict):
    date: str
    place: str
    country: str

class PlayerInfo(TypedDict):
    id: int
    name: str
    firstname: str
    lastname: str
    age: int
    birth: BirthInfo
    nationality: str
    height: str
    weight: str
    number: int
    position: str
    photo: str

class PlayerProfileItem(TypedDict):
    player: PlayerInfo

class PlayerProfileResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[PlayerProfileItem]

class PlayerProfileResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class PlayerProfileResponse499(TypedDict):
    message: str

class PlayerProfileResponse500(TypedDict):
    message: str

PlayerProfileResponse = Union[
    PlayerProfileResponse200,
    PlayerProfileResponse204,
    PlayerProfileResponse499,
    PlayerProfileResponse500
]
