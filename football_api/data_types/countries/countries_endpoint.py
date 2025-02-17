from typing import TypedDict, List, Union

class CountryInfo(TypedDict):
    name: str
    code: str
    flag: str

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class CountriesResponse200(TypedDict):
    get: str
    parameters: dict  
    errors: List
    results: int
    paging: Paging
    response: List[CountryInfo]

class CountriesResponse204(TypedDict):
    get: str
    parameters: List
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class CountriesResponse499(TypedDict):
    message: str

class CountriesResponse500(TypedDict):
    message: str

CountriesResponse = Union[CountriesResponse200, CountriesResponse204, CountriesResponse499, CountriesResponse500]
