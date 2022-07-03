import requests as t

link = 'https://pokeapi.co/api/v2/berry-firmness/'

re = t.get(link)

print(re.status_code)
re = re.json()
print(re.keys())
print(re['count'])
print(re['next'])