import json
import requests

#print(json.dumps(ed_sheeran, indent=2)) #indents are useful for making the output easier to read.  there are no rules, but 2 or 4 is enough.  

with open('ed_sheeran.json', 'r') as sheeran_file:
    sheeran_data = json.load(sheeran_file)
    deezer_sheeran = sheeran_data['data']
    sheeran_tracks = 0
    sheeran_albums = []
    sheeran_explicit_tracks = 0
    
    for element in deezer_sheeran:
        sheeran_tracks += 1
        sheeran_albums.append(element['album']['title'])
        sheeran_explicit_tracks += element['explicit_content_lyrics']
        es_album_id = element['id']
        
        url = (f"https://deezerdevs-deezer.p.rapidapi.com/album/{es_album_id}")

        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': "1b65b35d3emshab6ef9589bc846bp107b4djsn81a8182ae0e0"
            }

        es_response = requests.request("GET", url, headers=headers)
        es_release = es_response.json()
#        print(es_release['release_date'])

with open('cardi_b.json', 'r') as cardi_file:
    cardi_data = json.load(cardi_file)
    deezer_cardi = cardi_data['data']
    cardi_tracks = 0
    cardi_albums = []
    cardi_explicit_tracks = 0
    
    for element in deezer_cardi:
        cardi_tracks += 1
        cardi_albums.append(element['album']['title'])
        cardi_explicit_tracks += element['explicit_content_lyrics']
        cb_album_id = element['id']
        
        url = (f"https://deezerdevs-deezer.p.rapidapi.com/album/{cb_album_id}")

        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': "1b65b35d3emshab6ef9589bc846bp107b4djsn81a8182ae0e0"
            }

        cb_response = requests.request("GET", url, headers=headers)
#        cb_release = cb_response.json()
#    cb_latest_release = cb_release['release_date']

with open('eminem.json', 'r') as eminem_file:
    eminem_data = json.load(eminem_file)
    deezer_eminem = eminem_data['data']
    eminem_tracks = 0
    eminem_albums = []
    eminem_explicit_tracks = 0
    
    for element in deezer_eminem:
        eminem_tracks += 1
        eminem_albums.append(element['album']['title'])
        eminem_explicit_tracks += element['explicit_content_lyrics']
        em_album_id = element['id']
        
        url = (f"https://deezerdevs-deezer.p.rapidapi.com/album/{em_album_id}")

        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': "1b65b35d3emshab6ef9589bc846bp107b4djsn81a8182ae0e0"
            }

        em_response = requests.request("GET", url, headers=headers)
#        em_release = em_response.json()
#    em_latest_release = em_release['release_date']
    
print(f'there are {sheeran_tracks} tracks and {len(set(sheeran_albums))} albums listed in Deezer for Ed Sheeran.  {sheeran_explicit_tracks} have explicit lyrics. The most recent album name is {es_album_id}.  It was released ')
print(f'there are {cardi_tracks} tracks and {len(set(cardi_albums))} albums listed in Deezer for Cardi B.  {cardi_explicit_tracks} have explicit lyrics.  The most recent album name is {cb_album_id}.  It was released ')
print(f'there are {eminem_tracks} tracks and {len(set(eminem_albums))} albums listed in Deezer for Eminem.  {eminem_explicit_tracks} have explicit lyrics.  The most recent album name is {em_album_id}.  It was released ')

#shapeofyou_tracks = 'https://api.deezer.com/album/14996073/tracks'
#response = requests.get(shapeofyou_tracks)
#data = response.json()

#print(json.dumps(sheeran_data,indent=4))
