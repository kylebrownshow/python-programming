import json
import requests

sheeran_id = 384236
cardi_id = 9064930
eminem_id = 13

sheeran = "https://deezerdevs-deezer.p.rapidapi.com/artist/384236"
cardi = "https://deezerdevs-deezer.p.rapidapi.com/artist/9064930"
eminem = "https://deezerdevs-deezer.p.rapidapi.com/artist/13"

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "1b65b35d3emshab6ef9589bc846bp107b4djsn81a8182ae0e0"
    }

sheeran_response = requests.request("GET", sheeran, headers=headers)
cardi_response = requests.request("GET", cardi, headers=headers)
eminem_response = requests.request("GET", eminem, headers=headers)

sheeran_data = sheeran_response.json()
cardi_data = cardi_response.json()
eminem_data = eminem_response.json()

print(eminem_data.keys())

with open('ed_sheeran_artist.json', 'w') as sheeran_artist:
    sheeran_artist.write(json.dumps(sheeran_data))

with open('cardi_artist.json', 'w') as cardi_artist:
    cardi_artist.write(json.dumps(cardi_data))

with open('eminem_artist.json', 'w') as eminem_artist:
    eminem_artist.write(json.dumps(eminem_data))