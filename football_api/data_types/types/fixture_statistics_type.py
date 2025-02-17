from enum import Enum

class FixtureStatisticType(Enum):
    SHOTS_ON_GOAL = "ShotsOnGoal"
    SHOTS_OFF_GOAL = "ShotsOffGoal"
    TOTAL_SHOTS = "TotalShots"
    BLOCKED_SHOTS = "BlockedShots"
    SHOTS_IN_BOX = "ShotsInBox"
    SHOTS_OUT_BOX = "ShotsOutBox"
    FOULS = "Fouls"
    CORNER_KICKS = "CornerKicks"
    OFFSIDES = "Offsides"
    BALL_POSSESSION = "BallPossession"
    YELLOW_CARDS = "YellowCards"
    RED_CARDS = "RedCards"
    GOALKEEPER_SAVES = "GoalKeeperSaves"
    TOTAL_PASSES = "TotalPasses"
    ACCURATE_PASSES = "AccuratePasses"
    PASS_PERCENTAGE = "PassPercentage"
