import os
import mutagen


def create_m3u_playlist(directory):
    return


def get_subdirectories(directory):
    return filter(os.path.isdir, [os.path.join(directory, f) for f in os.listdir(directory)])

def has_supported_extension(file):
    SUPPORTED_EXTENSIONS = ["mp3", "m4a"]
    return True

root_directory = "/Users/tom/temp_music"

artist_directories = get_subdirectories(root_directory)

for artist_directory in artist_directories:
    album_directories = get_subdirectories(artist_directory)
    for album_directory in album_directories:
        track_files = [f for f in os.listdir(album_directory) if has_supported_extension(f)]



