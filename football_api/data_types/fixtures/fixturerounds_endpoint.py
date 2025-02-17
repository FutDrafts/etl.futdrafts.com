from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class FixtureRoundsResponse200(TypedDict):
    get: str
    parameters: dict 
    errors: List
    results: int
    paging: Paging
    response: List[str] 

class FixtureRoundsResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class FixtureRoundsResponse499(TypedDict):
    message: str

class FixtureRoundsResponse500(TypedDict):
    message: str

FixtureRoundsResponse = Union[
    FixtureRoundsResponse200,
    FixtureRoundsResponse204,
    FixtureRoundsResponse499,
    FixtureRoundsResponse500
]
