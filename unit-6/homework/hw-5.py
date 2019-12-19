import json
import requests

#1. Make separate API calls to retrieve data for the artists Eminem, Ed Sheeran, and Cardi B 
#2. Write the data for each artist to a separate json ﬁle (so you should have eminem.json, ed_sheeran.json, cardi_b.json ﬁles) 
#3. For each of the artists: a. How many tracks? b. How many albums? c.How many tracks with explicit lyrics d. Which year was the most recent album for each? 
#4. When was there lease date for Eminem’s album titled “The Eminem Show”? 
#5. How many tracks are on Ed Sheeran’s album “Shape of You”?
#6. Which artist(s) collaborated with Cardi B on the track titled “Cardi B”?
#7. Build a playlist of 10 songs from these 3 artists.
#        Take songs randomly from each artist until you have 10. 
#        For each track store the artists name along with the following data: 
#        id readable title title_short title_version link duration rank explicit_lyrics explicit_content_lyrics
#8. Save your playlist to a ﬂie called random_playlist.json  

with open('ed_sheeran.json', 'r') as sheeran_file:
    sheeran_data = json.load(sheeran_file)

deezer_sheeran = sheeran_data['data']

for element in deezer_sheeran:
    if element['album']['title'] == 'Shape of You':
        album_tracks = element['artist']['tracklist']
        tracklist = []
        url = album_tracks

        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': "1b65b35d3emshab6ef9589bc846bp107b4djsn81a8182ae0e0"
            }

        tracks_response = requests.request("GET", url, headers=headers)

        tracks_data = tracks_response.json()
        for item in tracks_data['data']:
            tracklist.append(item['title'])
        
        print(tracklist)

#print(json.dumps(data['teams'][0], indent = 4))

#print(f"Shape of You has was released on {album_data['release_date']}")
