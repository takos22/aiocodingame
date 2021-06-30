import warnings

warnings.filterwarnings(
    "default", category=DeprecationWarning, module="aiocodingame"
)

warnings.showwarning(
    "aiocodingame module is deprecated, please use the codingame module and"
    " create an asynchronous client with `codingame.Client(is_async=True)`",
    DeprecationWarning,
    "aiocodingame",
    "",
    line="",
)

from typing import NamedTuple

VersionInfo = NamedTuple(
    "VersionInfo", major=int, minor=int, micro=int, releaselevel=str, serial=int
)

version_info = VersionInfo(major=1, minor=0, micro=0, releaselevel="", serial=0)

__title__ = "aiocodingame"
__author__ = "takos22"
__version__ = "1.0.0"

from codingame import Client as BaseClient


class Client(BaseClient):
    def __new__(cls, is_async=True):
        super().__new__(cls, is_async)


from codingame import (
    ChallengeLeaderboard,
    ChallengeNotFound,
    ChallengeRankedCodinGamer,
    ClashOfCode,
    ClashOfCodeNotFound,
    CodinGameAPIError,
    CodinGamer,
    CodinGamerNotFound,
    EmailNotLinked,
    EmailRequired,
    GlobalLeaderboard,
    GlobalRankedCodinGamer,
    IncorrectPassword,
    League,
    LoginError,
    LoginRequired,
    MalformedEmail,
    NotFound,
    Notification,
    PasswordRequired,
    Player,
    PuzzleLeaderboard,
    PuzzleNotFound,
    PuzzleRankedCodinGamer,
)

__all__ = [
    # Client
    Client,
    # CodinGamer
    CodinGamer,
    # Clash of Code
    ClashOfCode,
    Player,
    # Notification
    Notification,
    # Leaderboard
    GlobalLeaderboard,
    GlobalRankedCodinGamer,
    League,
    ChallengeLeaderboard,
    ChallengeRankedCodinGamer,
    PuzzleLeaderboard,
    PuzzleRankedCodinGamer,
    # Exceptions
    CodinGameAPIError,
    LoginError,
    EmailRequired,
    MalformedEmail,
    PasswordRequired,
    EmailNotLinked,
    IncorrectPassword,
    LoginRequired,
    NotFound,
    CodinGamerNotFound,
    ClashOfCodeNotFound,
    ChallengeNotFound,
    PuzzleNotFound,
]
