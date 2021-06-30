⛔️ DEPRACATED: aiocodingame module
===================================

Use the `codingame module <https://github.com/takos22/codingame>`_ instead.

Install that module:

.. code-block:: sh

   pip install codingame[async]


To create an asynchronous client:

.. code-block:: py

   import asyncio
   import codingame

   async def main():
      client = codingame.Client(is_async=True)

      # if you want to log in
      await client.login("email@example.com", "password")

      # get a codingamer
      codingamer = await client.get_codingamer("username")
      print(codingamer.pseudo)

      # get the global leaderboard
      global_leaderboard = await client.get_global_leaderboard()
      # print the pseudo of the top codingamer
      print(global_leaderboard.users[0].pseudo)

   asyncio.run(main())
