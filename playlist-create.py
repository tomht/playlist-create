import os
from mutagen.easyid3 import EasyID3


def create_m3u_playlist(directory):
    return


def get_subdirectories(directory):
    return filter(os.path.isdir, [os.path.join(directory, f) for f in os.listdir(directory)])


def has_supported_extension(file):
    supported_extensions = ["mp3", "m4a"]
    extension = file.split('.')[-1]
    return extension in supported_extensions

root_directory = "/Users/tom/temp_music"

artist_directories = get_subdirectories(root_directory)

for artist_directory in artist_directories:
    album_directories = get_subdirectories(artist_directory)
    for album_directory in album_directories:
        track_files = [os.path.join(album_directory, f) for f in os.listdir(album_directory) if has_supported_extension(f)]
        track_numbers = []
        for track_file in track_files:
            track = EasyID3(track_file)
            track_number = int(track["tracknumber"][0])
            track_numbers.append((track_file, track_number))
        track_numbers.sort(key=lambda x: x[1])


