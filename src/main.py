from dotenv import load_dotenv
import requests as r
import scrapper
import os

load_dotenv()

auth_token = os.getenv('GENIUS_TOKEN')
if not auth_token:
    print('error: no Authorization token found')
    exit(1)
auth_token = 'Bearer ' + auth_token
headers = {'Authorization': auth_token}

out = open("jul.txt", "a")

page = 1
while page:
    params = {'page': page}
    res = r.get('http://api.genius.com/artists/74283/songs',
                headers=headers,
                params=params)
    res = res.json()
    page = res['response']['next_page']
    songs = res['response']['songs']

    for s in songs:
        print(s)
        # Take only song with only one artist (no featurings)
        if s['title'] != s['title_with_featured'] or s['lyrics_state'] != 'complete':
            continue
        lyrics = scrapper.get_lyrics(s['url'])
        if lyrics:
            out.write(lyrics)

out.close()
