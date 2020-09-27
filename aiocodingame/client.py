import asyncio
import aiohttp
import re

from typing import AsyncGenerator, AsyncIterator, List, Optional

from .codingamer import CodinGamer
from .clash_of_code import ClashOfCode
from .notification import Notification

from .endpoints import Endpoints
from .exceptions import CodinGamerNotFound, ClashOfCodeNotFound, LoginRequired
from .utils import validate_args


class Client:
    """CodinGame API client.

    Attributes
    -----------
        logged_in: :class:`bool`
            If the client is logged in as a CodinGamer.

        codingamer: Optional[:class:`CodinGamer`]
            The CodinGamer that is logged in through the client. ``None`` if the client isn't logged in.
    """

    _CODINGAMER_HANDLE_REGEX = re.compile(r"[0-9a-f]{32}[0-9]{7}")
    _CLASH_OF_CODE_HANDLE_REGEX = re.compile(r"[0-9]{7}[0-9a-f]{32}")

    logged_in: bool
    codingamer: Optional[CodinGamer]

    def __init__(self, *, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self._session = aiohttp.ClientSession(loop=self.loop)

        self.logged_in = False
        self.codingamer = None

    async def close(self):
        """Closes the Client connection."""
        await self._session.close()

    @validate_args
    async def login(self, email: str, password: str):
        """Login to a CodinGamer account.

        Parameters
        -----------
            email: :class:`str`
                Email adress of the CodinGamer.

            password: :class:`str`
                Password of the CodinGamer.

        Raises
        ------
            :exc:`ValueError`
                Error with the login (empty email, empty password, wrong email format, incorrect password, etc).

        Returns
        --------
            :class:`CodinGamer`
                The CodinGamer that is logged in.
        """

        if email == "":
            raise ValueError("Email is required")
        if password == "":
            raise ValueError("Password is required")

        r = await self._session.post(Endpoints.CodinGamer_login, json=[email, password, True])
        json = await r.json()
        if "id" in json and "message" in json:
            raise ValueError(f"{json['id']}: {json['message']}")
        self.logged_in = True
        self.codingamer = CodinGamer(client=self, **json["codinGamer"])
        return self.codingamer

    @validate_args
    async def get_codingamer(self, codingamer_handle: str) -> CodinGamer:
        """Get a CodinGamer from his public handle.

        Parameters
        -----------
            codingamer_handle: :class:`str`
                The CodinGamer's public handle.
                39 character long hexadecimal string (regex: ``[0-9a-f]{32}[0-9]{7}``).

        Raises
        ------
            :exc:`ValueError`
                The CodinGamer handle isn't in the good format.

            :exc:`.CodinGamerNotFound`
                The CodinGamer with the given public handle isn't found.

        Returns
        --------
            :class:`CodinGamer`
                The CodinGamer.
        """

        if not self._CODINGAMER_HANDLE_REGEX.match(codingamer_handle):
            raise ValueError(
                f"CodinGamer handle {codingamer_handle!r} isn't in the good format " "(regex: [0-9a-f]{32}[0-9]{7})."
            )

        r = await self._session.post(Endpoints.CodinGamer, json=[codingamer_handle])
        json = await r.json()
        if json is None:
            raise CodinGamerNotFound(f"No CodinGamer with handle {codingamer_handle!r}")
        return CodinGamer(client=self, **json["codingamer"])

    @validate_args
    async def get_clash_of_code(self, clash_of_code_handle: str) -> ClashOfCode:
        """Get a Clash of Code from its public handle.

        Parameters
        -----------
            clash_of_code_handle: :class:`str`
                The Clash of Code's public handle.
                39 character long hexadecimal string (regex: ``[0-9]{7}[0-9a-f]{32}``).

        Raises
        ------
            :exc:`ValueError`
                The Clash of Code handle isn't in the good format.

            :exc:`.ClashOfCodeNotFound`
                The Clash of Code with the given public handle isn't found.

        Returns
        --------
            :class:`ClashOfCode`
                The ClashOfCode.
        """

        if not self._CLASH_OF_CODE_HANDLE_REGEX.match(clash_of_code_handle):
            raise ValueError(
                f"Clash of Code handle {clash_of_code_handle!r} isn't in the good format "
                "(regex: [0-9]{7}[0-9a-f]{32})."
            )

        r = await self._session.post(Endpoints.ClashOfCode, json=[clash_of_code_handle])
        json = await r.json()
        if "id" in json and "message" in json:
            raise ClashOfCodeNotFound(f"No Clash of Code with handle {clash_of_code_handle!r}")
        return ClashOfCode(client=self, **json)

    async def get_pending_clash_of_code(self) -> Optional[ClashOfCode]:
        """Get a pending Clash of Code.

        Returns
        --------
            Optional[:class:`ClashOfCode`]
                The pending ClashOfCode if there's one or ``None``.
        """

        r = await self._session.post(Endpoints.ClashOfCode_pending, json=[])
        json = await r.json()
        if len(json) == 0:
            return None
        return ClashOfCode(client=self, **json[0])

    async def language_ids(self) -> List[str]:
        """Get all valid language ids from CodinGame.

        Returns
        --------
            List[:class:`str`]
                List of all available language ids.
        """

        r = await self._session.post(Endpoints.LanguageIds, json=[])
        return await r.json()

    async def notifications(self) -> AsyncIterator[Notification]:
        """Get all the unseen notifications of the Client.

        You need to be logged in to get notifications or else a :exc:`LoginRequired` will be raised.

        Raises
        ------
            :exc:`LoginRequired`
                The Client needs to log in. See :meth:`login`.

        Yields
        -------
            :class:`Notification`
                The Notification.
        """

        if not self.logged_in:
            raise LoginRequired()

        r = await self._session.post(Endpoints.UnseenNotifications, json=[self.codingamer.id])
        async for notification in await r.json():
            yield Notification(notification)
