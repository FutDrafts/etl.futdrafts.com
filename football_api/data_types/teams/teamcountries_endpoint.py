from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class CountryInfo(TypedDict):
    name: str
    code: str
    flag: str

class TeamCountriesResponse200(TypedDict):
    get: str
    parameters: List
    errors: List
    results: int
    paging: Paging
    response: List[CountryInfo]

class TeamCountriesResponse204(TypedDict):
    get: str
    parameters: dict
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class TeamCountriesResponse499(TypedDict):
    message: str

class TeamCountriesResponse500(TypedDict):
    message: str

TeamCountriesResponse = Union[
    TeamCountriesResponse200,
    TeamCountriesResponse204,
    TeamCountriesResponse499,
    TeamCountriesResponse500
]
