from enum import Enum
from typing import TypedDict

class FixtureStatusType(Enum):
    SCHEDULED = "Scheduled"
    IN_PLAY = "InPlay"
    POSTPONED = "Postponed"
    CANCELLED = "Cancelled"
    ABANDONED = "Abandoned"
    NOT_PLAYED = "NotPlayed"

class FixtureStatus(TypedDict):
    short: str
    long: str
    type: FixtureStatusType
    description: str
