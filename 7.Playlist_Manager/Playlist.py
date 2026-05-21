import random

playlist = []


def menu():
    print("\n1. Show Playlist")
    print("2. Add Song")
    print("3. Remove Song")
    print("4. Mix & Shuffle")
    print("5. Exit\n")

def show_playlist(playlist):
    print("\n--- My Playlist ---")

    try:
        with open("playlist.txt", "r") as f:
            lines = f.readlines()
            songs = [line.strip() for line in lines]

        if len(songs) == 0:
            print("The playlist is empty.\n")

        else:
            for index , song in enumerate(songs, start=1):
                print(f"{index}. {song}")
    except FileNotFoundError:
        print("The playlist.txt file does not exist yet!\n")
   
    return playlist

def add_song(playlist,song):

    with open("playlist.txt", "a") as f:
        f.write(f"{song}\n")
        print(f"{song} added to your playlist\n")

    return playlist

def remove_song():

    try:
        with open("playlist.txt", "r") as f:
            lines = f.readlines()
            songs = [line.strip() for line in lines]
    except FileNotFoundError:
        print("No playlist found to remove from\n")
        return

    song_to_remove = input("Enter the name of the song you want to remove: ")

    if song_to_remove in songs:
        songs.remove(song_to_remove)

        with open("playlist.txt" ,"w") as f:
            for song in songs:
                f.write(f"{song}\n")
            print(f"{song_to_remove} removed from playlist!\n")

    else:
        print("Song not found")

def shuffle_playlist():

    try:
        with open("playlist.txt", "r") as f:
            lines = f.readlines()
            songs = [line.strip() for line in lines]
    except FileNotFoundError:
        print("No playlist found to remove from\n")
        return

    if len(songs)>0:

        random.shuffle(songs)

        with open("playlist.txt", "w") as f:
            for song in songs:
                f.write(f"{song}\n")


        print("Playlist shuffled!")

    else:
        print("Your playlist is empty!")


while True:

    menu()
    choice = input("\nSelect: ")

    if choice == "1":       
        show_playlist(playlist)
     

    elif choice == "2":

        song = input("Enter song name: ")
        add_song(playlist, song)

    elif choice == "3":
        
        remove_song()

    elif choice == "4":

        shuffle_playlist()

    elif choice == "5":
        print("Exiting the program...")
        break

