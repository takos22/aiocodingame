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
