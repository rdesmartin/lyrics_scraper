from dotenv import load_dotenv
import requests as r
import scrapper
import os
import sys
import argparse


# Parse arguments
parser = argparse.ArgumentParser(description='Basic lyrics scrapper. You must provide either '
                                             'an id or search terms for your artist')
parser.add_argument('-i', '--id', default=0,
                    help='The artist\'s ID for Genius\' API')
parser.add_argument('-s', '--search', metavar='S',
                    help='A Genius search that you think will return a song result by '
                         'the artist in the first n results (eg: "Frank Sinatra Fly Me to The Moon)')
parser.add_argument('-f', '--file-path', metavar='F', default='out.txt',
                    help='Destination file path (defaults to "out.txt)')

args = parser.parse_args(sys.argv[1:])

if not args.id and not args.search:
    parser.parse_args(['--help'])
    exit(1)

# read env
load_dotenv()
auth_token = os.getenv('GENIUS_TOKEN')
if not auth_token:
    print('error: no Authorization token found')
    exit(1)
api = 'http://api.genius.com'
auth_token = 'Bearer ' + auth_token
headers = {'Authorization': auth_token}

# Get artist's id
artist_id = 0
if args.id:
    artist_id = args.id
elif args.search:
    res = r.get(api + '/search?q=' + args.search,
                headers=headers).json()
    results = res['response']['hits']
    artists = [r['result']['primary_artist'] for r in results]
    for x in range(len(artists)):
        print('#' + str(x) + '  ' + artists[x]['name'] +
              ' (id:' + str(artists[x]['id']) + ')')
    x = int(input('# of your artist:'))
    artist_id = artists[x]['id']
    print('scrapping songs by ' + artists[x]['name'] + '...')
exit(0)

# Scrap songs and write in file
out = open(args.file_path, "a")
page = 1
while page:
    params = {'page': page}
    res = r.get('/artists/' + artist_id + '/songs',
                headers=headers,
                params=params).json()
    page = res['response']['next_page']
    songs = res['response']['songs']

    for s in songs:
        # Take only song with only one artist (no featurings)
        if s['title'] != s['title_with_featured'] or s['lyrics_state'] != 'complete':
            continue
        lyrics = scrapper.get_lyrics(s['url'])
        if lyrics:
            out.write(lyrics)

out.close()
