import asyncio
import httpx

API_URL = "https://pokeapi.co/api/v2/ability/?limit=20"

def count_pokemon(ability_detail):
    return ability_detail["name"], len(ability_detail["pokemon"])

async def fetch_detail(url, client):
    res = await client.get(url)
    return res.json()

async def main():
    async with httpx.AsyncClient() as client:
        res = await client.get(API_URL)
        abilities = res.json()["results"][:10]

        detail_tasks = [fetch_detail(a["url"], client) for a in abilities]
        details = await asyncio.gather(*detail_tasks)

        for d in details:
            name, count = count_pokemon(d)
            print(f"{name:<20} - {count} Pokémon")

if __name__ == "__main__":
    asyncio.run(main())
