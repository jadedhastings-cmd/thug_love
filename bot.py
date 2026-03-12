from dotenv import load_dotenv
import os
import csv
from atproto import Client

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()

handle = os.getenv("BLUESKY_HANDLE")
password = os.getenv("BLUESKY_PASSWORD")

with open(os.path.join(BASE_DIR,"love_songs.csv"),"r", encoding="latin-1") as f:
    reader = csv.DictReader(f)
    songs = list(reader)

try:
    with open(os.path.join(BASE_DIR,"state.txt"), 'r') as f:
        # File exists and is open
        index = int(f.read())
except FileNotFoundError:
    # File does not exist
    index = 0
    with open(os.path.join(BASE_DIR,"state.txt"),"w") as f:
        f.write(str(index))
        
song = songs[index]

new_song = song["Title"].replace("love","thug").replace("Love","Thug").replace("lovi","thuggi").replace("Lovi","Thuggi")

post_text = f'"{new_song}", {song["Artist"]}, {song["Year"]}'

client = Client()
client.login(handle, password)
client.send_post(post_text)

index += 1
if index >= len(songs):
    index = 0

with open(os.path.join(BASE_DIR,"state.txt"),"w") as f:
    f.write(str(index))