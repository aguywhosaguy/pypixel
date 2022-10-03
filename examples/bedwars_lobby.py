# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

__doc__ = """A simple example showing how to display a full bedwars lobby username."""

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            player = await client.player('gamerboy80')
            # Will display [None] as the rank if the player has no rank
            # You can add your own logic
            print(f'[{player.bedwars.level}✫] [{player.rank}] {player.name}')
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())