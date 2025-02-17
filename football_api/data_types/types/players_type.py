from typing import TypedDict

class BirthInfo(TypedDict):
    date: str
    place: str
    country: str

class SoccerPlayer(TypedDict):
    id: int
    name: str
    firstname: str
    lastname: str
    age: int
    birth: BirthInfo
    nationality: str
    height: str
    weight: str
    injured: bool
    photo: str
