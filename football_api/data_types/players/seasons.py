from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class PlayerSeasonsResponse200(TypedDict):
    get: str
    parameters: List
    errors: List
    results: int
    paging: Paging
    response: List[int]

class PlayerSeasonsResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class PlayerSeasonsResponse499(TypedDict):
    message: str

class PlayerSeasonsResponse500(TypedDict):
    message: str

PlayerSeasonsResponse = Union[
    PlayerSeasonsResponse200,
    PlayerSeasonsResponse204,
    PlayerSeasonsResponse499,
    PlayerSeasonsResponse500
]
