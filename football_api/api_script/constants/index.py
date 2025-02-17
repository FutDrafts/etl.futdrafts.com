API_URL = "https://v3.football.api-sports.io"

FIXTURE_STATUS = [
    {
        "short": "TBD",
        "long": "Time To Be Defined",
        "type": "Scheduled",
        "description": "Scheduled but date and time are not known",
    },
    {
        "short": "NS",
        "long": "Not Started",
        "type": "Scheduled",
        "description": "",
    },
    {
        "short": "1H",
        "long": "First Half, Kick Off",
        "type": "In Play",
        "description": "First half in play",
    },
    {
        "short": "HT",
        "long": "Halftime",
        "type": "In Play",
        "description": "Finished in the regular time",
    },
    {
        "short": "2H",
        "long": "Second Half, 2nd Half Started",
        "type": "In Play",
        "description": "Second half in play",
    },
    {
        "short": "ET",
        "long": "Extra Time",
        "type": "In Play",
        "description": "Extra time in play",
    },
    {
        "short": "BT",
        "long": "Break Time",
        "type": "In Play",
        "description": "Break during extra time",
    },
    {
        "short": "P",
        "long": "Penalty In Progress",
        "type": "In Play",
        "description": "Penalty played after extra time",
    },
    {
        "short": "SUSP",
        "long": "Match Suspended",
        "type": "In Play",
        "description": "Suspended by referee's decision, may be rescheduled another day",
    },
    {
        "short": "INT",
        "long": "Match Interrupted",
        "type": "In Play",
        "description": "Interrupted by referee's decision, should resume in a few minutes",
    },
    {
        "short": "FT",
        "long": "Match Finished",
        "type": "Finished",
        "description": "Finished in regular time",
    },
    {
        "short": "AET",
        "long": "Match Finished",
        "type": "Finished",
        "description": "Finished after extra time without going to the penalty shootout",
    },
    {
        "short": "PEN",
        "long": "Match Finished",
        "type": "Finished",
        "description": "Finished after the penalty shootout",
    },
    {
        "short": "PST",
        "long": "Match Postponed",
        "type": "Postponed",
        "description": "Postponed to another day, once the new date and time is known the status will change to Not Started",
    },
    {
        "short": "CANC",
        "long": "Match Cancelled",
        "type": "Cancelled",
        "description": "Cancelled, match will not be played",
    },
    {
        "short": "ABD",
        "long": "Match Abandoned",
        "type": "Abandoned",
        "description": "Abandoned for various reasons (Bad Weather, Safety, Floodlights, Playing Staff Or Referees), Can be rescheduled or not, it depends on the competition",
    },
    {
        "short": "AWD",
        "long": "Technical Loss",
        "type": "Not Played",
        "description": "",
    },
    {
        "short": "WO",
        "long": "WalkOver",
        "type": "Not Played",
        "description": "Victory by forfeit or absence of competitor",
    },
    {
        "short": "LIVE",
        "long": "In Progress",
        "type": "In Play",
        "description": "Used in very rare cases. It indicates a fixture in progress but the data indicating the half-time or elapsed time are not available",
    },
]
