from typing import TypedDict, List, Union

class Paging(TypedDict):
    current: int
    total: int

class ErrorReport(TypedDict):
    time: str
    bug: str
    report: str

class VenueInfo(TypedDict):
    id: int
    name: str
    address: str
    city: str
    country: str
    capacity: int
    surface: str
    image: str

class VenuesResponse200(TypedDict):
    get: str
    parameters: dict
    errors: List
    results: int
    paging: Paging
    response: List[VenueInfo]

class VenuesResponse204(TypedDict):
    get: str
    parameters: dict
    errors: ErrorReport
    results: int
    paging: Paging
    response: List

class VenuesResponse499(TypedDict):
    message: str

class VenuesResponse500(TypedDict):
    message: str

VenuesResponse = Union[
    VenuesResponse200,
    VenuesResponse204,
    VenuesResponse499,
    VenuesResponse500
]
