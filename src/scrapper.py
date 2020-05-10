import requests as r
from bs4 import BeautifulSoup

def get_lyrics(url):
    res = r.get(url)
    print(url)
    content = BeautifulSoup(res.content, 'html.parser')
    lyrics_div = content.find('div', attrs={'class': 'lyrics'})
    if lyrics_div:
        lyrics = lyrics_div.get_text()
        return lyrics
    else:
        return ""
