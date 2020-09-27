.. _quickstart:

.. currentmodule:: aiocodingame

Quickstart
==========

This page gives a brief introduction to the library. It assumes you have the library installed,
if you don't check the :ref:`installing` portion.
You can find examples `here <https://github.com/takos22/aiocodingame/tree/master/examples>`_.

Get a CodinGamer
----------------

Let's get a CodinGamer from his handle, your public handle is the 39 character length hexadecimal string at the end of your profile link.

The code will be something like this:

.. code-block:: python3

    import asyncio
    import aiocodingame

    async def main():
        client = aiocodingame.Client()

        # get a codingamer from his public handle
        me = client.get_codingamer("your handle here")

        print(me)
        print(me.pseudo)
        print(me.public_handle)
        print(me.avatar_url)

    asyncio.run(main())

Get a Clash of Code
-------------------

Let's get a Clash of Code from its handle, the public handle is the 39 character
length hexadecimal string at the end of the Clash of Code invite link.
You can also get a pending public Clash of Code.

The code will be something like this:

.. code-block:: python3

    import asyncio
    import aiocodingame

    async def main():
        client = aiocodingame.Client()

        # get a pending public clash of code
        coc = await client.get_pending_clash_of_code()
        # or get a clash of code from its public handle
        coc = await client.get_clash_of_code("clash of code handle here")

        print(coc)
        print(coc.join_url)
        print(coc.modes)
        print(coc.programming_languages)
        print(coc.public_handle)
        print(coc.players)

    asyncio.run(main())

Login
-----

Let's log in into a profile with the email and password.

.. code-block:: python3

    import asyncio
    import aiocodingame

    async def main():
        client = aiocodingame.Client()
        await client.login("email", "password")

        # then you can access the logged in codingamer like this
        print(client.logged_in)
        print(client.codingamer)
        print(client.codingamer.pseudo)
        print(client.codingamer.public_handle)
        print(client.codingamer.avatar_url)

    asyncio.run(main())

.. note::
    Don't worry, the email and the password aren't stored.
    You can see that `here <https://github.com/takos22/aiocodingame/blob/master/codingame/client.py>`_.
