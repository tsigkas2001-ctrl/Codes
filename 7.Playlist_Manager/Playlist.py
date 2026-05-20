import random

playlist = []


def menu():
    print("1. Show Playlist")
    print("2. Add Song")
    print("3. Remove Song")
    print("4. Mix & Shuffle")
    print("5. Exit")

def show_playlist(playlist):
    print("--- My Playlist ---")

    try:
        with open("playlist.txt", "r") as f:
            lines = f.readlines()
            songs = [line.strip() for line in lines]

        if len(songs) == 0:
            print("The playlist is empty.")

        else:
            for index , song in enumerate(songs, start=1):
                print(f"{index}. {song}")
    except FileNotFoundError:
        print("The playlist.txt file does not exist yet!")
   
    return playlist

def add_song(playlist,song):
    with open("playlist.txt", "a") as f:
        f.write(f"{}")
        print(f"{song} added to your playlist")

    return playlist

def remove_song

while True:

    choice = input("Select: ")

    if choice == "1":
        show_playlist(playlist)


