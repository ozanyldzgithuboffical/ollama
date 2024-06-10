from enum import Enum


class DeveloperSolvingCategories(Enum):
    code_solving = 1
    solving_bug = 2
    code_fixing_issue = 3


class CodeReviewerStates(Enum):
    Approved = 1
    Rejected = 2
    ChangeNeeded = 3
    ImprovementNeeded = 4
    UnEthical = 5


class TestTypes(Enum):
    Unit = 1
    Integration = 2
    End_to_End = 3
    Functional = 4
    Smoke = 5
    Acceptance = 6
    Regression = 7
