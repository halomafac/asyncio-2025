import requests

url = "http//pokeapi.co/api/v2/pikachu"
response = requests.get(url)

data = response.json()

print('Name :',data["name"])
print('ID :',data["id"])
print('Height :',data["height"])
print('Weight :',data["weight"])
print('Types :',[t["type"]["name"] for u in data["types"]])