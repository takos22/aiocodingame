"""
CodinGame API Wrapper
~~~~~~~~~~~~~~~~~~~~~

Basic async wrapper for the undocumented CodinGame API.
"""

from typing import NamedTuple

VersionInfo = NamedTuple(
    "VersionInfo", major=int, minor=int, micro=int, releaselevel=str, serial=int
)

version_info = VersionInfo(major=0, minor=1, micro=1, releaselevel="", serial=0)

__title__ = "aiocodingame"
__author__ = "takos22"
__version__ = "0.1.1"

__all__ = [
    "Client",
    "CodinGamer",
    "ClashOfCode",
    "Player",
    "Notification",
    "CodinGameAPIError",
    "CodinGamerNotFound",
    "ClashOfCodeNotFound",
    "LoginRequired",
]

from .client import Client
from .codingamer import CodinGamer
from .clash_of_code import ClashOfCode, Player
from .notification import Notification
from .exceptions import CodinGameAPIError, CodinGamerNotFound, ClashOfCodeNotFound, LoginRequired
