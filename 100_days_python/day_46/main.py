import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"
response = requests.get(url = URL)
response.raise_for_status()

bot_song = response.text

soup = BeautifulSoup(bot_song, 'html.parser')
# song_list = soup.find_all('h3','chart-entry__title')
# all_songs = [item.getText() for item in song_list] 
# print(all_songs)

song_names = [tag.getText() for tag in soup.select("h3.chart-entry__title")]
print(song_names)

file_path = "D:/python/100_days_python/day_46/browser.json"
PLAY_NAME = f"{date} Billboard 100"

yt = YTMusic(file_path)
playlists = yt.get_library_playlists(limit=100)
print(f"Found {len(playlists)} playlists in your library.")

play_id = None
for play in playlists:
    if play["title"] == PLAY_NAME:
        play_id = play["playlistId"]
        break
if play_id:
    print("This playlist already exists.")
else:
    play_id = yt.create_playlist(title=PLAY_NAME, description= f"Playlist with the hottest songs from {date}", privacy_status="PRIVATE")
    print("playlist created")

for song in song_names:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(play_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
        
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")