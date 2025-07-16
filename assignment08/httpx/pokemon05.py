import asyncio
import httpx

names = [
    "pikachu", "bulbasaur", "charmander", "squirtle", "eevee",
    "snorlax", "gengar", "mewtwo", "psyduck", "jigglypuff"
]

async def fetch_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return {
            "name": data["name"].title(),
            "id": data["id"],
            "base_experience": data["base_experience"]
        }

def get_base_experience(pokemon):
    return pokemon["base_experience"]

async def main():
    tasks = [fetch_pokemon_data(name) for name in names]
    results = await asyncio.gather(*tasks)

    sorted_results = sorted(results, key=get_base_experience, reverse=True)

    print("• Pokemon Data (sorted by base_experience):")
    for p in sorted_results:
        print(f"  {p['name']:12} | ID: {p['id']:3} | Base EXP: {p['base_experience']}")

asyncio.run(main())