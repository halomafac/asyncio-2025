import asyncio
import httpx

async def fetch_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        types = [t['type']['name'] for t in data['types']]
        print(f"{data['name'].title()}, ID: {data['id']}, Types: {types}")

async def main():
    pokemon_names = ["pikachu", "bulbasaur", "charmander", "squirtle", "snorlax"]
    tasks = [fetch_pokemon(name) for name in pokemon_names]
    await asyncio.gather(*tasks)

asyncio.run(main())