from typing import TypedDict, List, Optional, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class TimeInfo(TypedDict):
    elapsed: int
    extra: int

class TeamInfo(TypedDict):
    id: int
    name: str
    logo: str

class PlayerInfo(TypedDict):
    id: int
    name: str

class AssistInfo(TypedDict):
    id: int
    name: str

class FixtureEvent(TypedDict):
    time: TimeInfo
    team: TeamInfo
    player: PlayerInfo
    assist: AssistInfo
    type: str
    detail: str
    comments: Optional[str]

class FixtureEventResponse200(TypedDict):
    get: str
    parameters: dict 
    errors: List
    results: int
    paging: Paging
    response: List[FixtureEvent]

class FixtureEventResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class FixtureEventResponse499(TypedDict):
    message: str

class FixtureEventResponse500(TypedDict):
    message: str

FixtureEventResponse = Union[
    FixtureEventResponse200,
    FixtureEventResponse204,
    FixtureEventResponse499,
    FixtureEventResponse500
]
