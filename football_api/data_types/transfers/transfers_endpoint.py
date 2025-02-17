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

class TransferInfo(TypedDict):
    date: str
    type: str
    teams: dict

class PlayerInfo(TypedDict):
    id: int
    name: str

class TransferResponseItem(TypedDict):
    player: PlayerInfo
    update: str
    transfers: List[TransferInfo]

class TransfersResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[TransferResponseItem]

class TransfersResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class TransfersResponse499(TypedDict):
    message: str

class TransfersResponse500(TypedDict):
    message: str

TransfersResponse = Union[
    TransfersResponse200,
    TransfersResponse204,
    TransfersResponse499,
    TransfersResponse500
]
