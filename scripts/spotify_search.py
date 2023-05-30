import os
import webbrowser

# Spotify uygulamasının bulunduğu dizini belirle
spotify_path = "C:\\Users\\realh\\AppData\\Roaming\\Spotify\\Spotify.exe"

# Arama sonuçlarını al
search_query = "parça adı"
os.system(f'start {spotify_path} --uri spotify:search:{search_query}')

# Arama sonuçlarından ilk parçayı aç
webbrowser.open(f"https://open.spotify.com/track/parça_id")