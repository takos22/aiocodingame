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
