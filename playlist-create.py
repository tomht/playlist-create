import os
import ConfigParser
from mutagen.easyid3 import EasyID3


def create_m3u_playlist(album_directory):
    path_parts = album_directory.split('/')
    album_artist = path_parts[-2]
    album_title = path_parts[-1]
    track_files = [os.path.join(album_directory, f) for f in os.listdir(album_directory) if
                   has_supported_extension(f)]
    track_numbers = []
    for track_file in track_files:
        track = EasyID3(track_file)
        track_number = int(track["tracknumber"][0].split('/')[0])
        track_numbers.append((track_file, track_number))
    track_numbers.sort(key=lambda x: x[1])
    playlist_filename = album_artist + " - " + album_title + ".m3u"
    with open(os.path.join(album_directory, playlist_filename), 'w') as playlist_file:
        for track in track_numbers:
            playlist_file.write(track[0] + "\n")
    return


def get_subdirectories(directory):
    return filter(os.path.isdir, [os.path.join(directory, f) for f in os.listdir(directory)])


def has_supported_extension(file):
    supported_extensions = ["mp3"]
    extension = file.split('.')[-1]
    return extension in supported_extensions

config = ConfigParser.ConfigParser()
config.read("playlist-create.cfg")
root_directory = config.get("Main", "root_directory")

artist_directories = get_subdirectories(root_directory)

for artist_directory in artist_directories:
    album_directories = get_subdirectories(artist_directory)
    for album_directory in album_directories:
        create_m3u_playlist(album_directory)
