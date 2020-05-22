a basic scrapper to get lyrics off of genius.com.

## Usage
install dependencies
```
pip install beautifulsoup4 requests python-dotenv
```
```
usage: main.py [-h] [-i ID] [-s S] [-f F]

Basic lyrics scrapper. You must provide either an id or search terms for your artist

optional arguments:
  -h, --help           show this help message and exit
  -i ID, --id ID       The artist's ID for Genius' API
  -s S, --search S     A Genius search that you think will return a song result by the artist in the first n results (eg: "Frank Sinatra Fly Me to The Moon)
  -f F, --file-path F  Destination file path (defaults to "out.txt)
```
## Genius API
Register your app at [http://api.genius.com]().
Generate an authorization token and put it in a .env file:
```
GENIUS_TOKEN="Pa5t3yOUr70kenh3rEqsDFQqq34HR4dgdcb5d34"
```
