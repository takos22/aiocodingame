# TODO add more tests
import pytest
import os
import sys
import re
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.abspath("..."))

from aiocodingame.exceptions import CodinGameAPIError, CodinGamerNotFound, ClashOfCodeNotFound, LoginRequired

def test_import():
    import aiocodingame
    assert aiocodingame.__title__ == aiocodingame.__name__ == aiocodingame.__package__ == "aiocodingame"
    assert aiocodingame.__author__ == "takos22"

# @pytest.fixture
# def aiocodingame():
#     import aiocodingame
#     return aiocodingame

# def client_attr(client):
#     assert hasattr(client, "logged_in")
#     assert hasattr(client, "codingamer")
#     assert hasattr(client, "get_clash_of_code")
#     assert hasattr(client, "get_pending_clash_of_code")
#     assert hasattr(client, "get_codingamer")
#     assert hasattr(client, "language_ids")
#     assert hasattr(client, "notifications")
#     return True

# def test_client(aiocodingame):
#     client = aiocodingame.Client()
#     assert client_attr(client)

# def test_client_login(aiocodingame):
#     email = os.environ.get("TEST_LOGIN_EMAIL")
#     password = os.environ.get("TEST_LOGIN_PASSWORD")

#     # login at creation
#     client = aiocodingame.Client(email, password)
#     assert client_attr(client)

#     # login after creation
#     client = aiocodingame.Client()
#     client.login(email, password)
#     assert client_attr(client)

# @pytest.fixture
# def client():
#     import aiocodingame
#     return aiocodingame.Client()

# def test_client_codingamer(aiocodingame, client):
#     codingamer = client.get_codingamer(os.environ.get("TEST_CODINGAMER_PUBLIC_HANDLE"))

#     assert type(codingamer) == aiocodingame.CodinGamer

# @pytest.mark.parametrize("public_handle, error, message_regex", [
#     (0, TypeError, re.escape("Argument 'codingamer_handle' needs to be of type 'str' (got type 'int')")),
#     ("", ValueError, re.escape("CodinGamer handle '' isn't in the good format (regex: [0-9a-f]{32}[0-9]{7}).")),
#     ("a" * 32 + "0" * 7, CodinGamerNotFound, re.escape(f"No CodinGamer with handle {'a' * 32 + '0' * 7!r}"))
# ])
# def test_client_codingamer_error(aiocodingame, client, public_handle, error, message_regex):
#     with pytest.raises(error, match=message_regex):
#         codingamer = client.get_codingamer(public_handle)

# def test_client_clash_of_code(aiocodingame, client):
#     clash_of_code = client.get_clash_of_code(os.environ.get("TEST_CLASHOFCODE_PUBLIC_HANDLE"))

#     assert type(clash_of_code) == aiocodingame.ClashOfCode

# @pytest.mark.parametrize("public_handle, error, message_regex", [
#     (0, TypeError, re.escape("Argument 'clash_of_code_handle' needs to be of type 'str' (got type 'int')")),
#     ("", ValueError, re.escape("Clash of Code handle '' isn't in the good format (regex: [0-9]{7}[0-9a-f]{32}).")),
#     ("0" * 7 + "a" * 32, ClashOfCodeNotFound, re.escape(f"No Clash of Code with handle {'0' * 7 + 'a' * 32!r}"))
# ])
# def test_client_clash_of_code_error(aiocodingame, client, public_handle, error, message_regex):
#     with pytest.raises(error, match=message_regex):
#         clash_of_code = client.get_clash_of_code(public_handle)

# def test_client_pending_clash_of_code(aiocodingame, client):
#     clash_of_code = client.get_pending_clash_of_code()

#     assert type(clash_of_code) == aiocodingame.ClashOfCode or clash_of_code is None
