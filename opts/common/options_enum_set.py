from enum import Enum


class ProgrammingLanguageSet(Enum):
    Python = 1
    R = 2
    Scala = 3
    Java = 4
    Ruby = 5
    C = 6
    Cplus = 7
    Perl = 8
    Php = 9
    JavaScript = 10


class TestTypes(Enum):
    Unit = 1
    Integration = 2
    Functional = 3
    E2E = 4
    Acceptance = 5
    Performance = 6
    Regression = 7
    Smoke = 8


class DB(Enum):
    MYSQL = 1
    MARIADB = 2
    MONGODB = 3
    DYNAMODB = 4
    GCP_BIGTABLE = 5
    AWS_AURORA = 6
    GCP_SPANNER = 7
    AWS_CLOUDSQL = 8
    APACHE_CASSANDRA = 9


class ToxicityCategory(Enum):
    Toxic = 1
    SevereToxic = 2
    Sexual = 3
    Obscene = 4
    Threat = 5
    Insult = 6
    Hate = 7
    Promotional = 8


class NewspaperTopic(Enum):
    Politics = 1
    Sports = 2
    Fashion = 3
    Culture = 4
    History = 5


class ApprovalType(Enum):
    Approved = 1
    Needs_Change = 2


class ExpressionType(Enum):
    Creative = 1
    Realistic = 2


class TaskType(Enum):
    bugs = 1
    code_quality = 2
