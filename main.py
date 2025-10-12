while __name__ == "__main__":
    from playlist import Playlist, SongNode
    from difflib import get_close_matches

    def match_input(user_input, options, cutoff=0.6):
        return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)
    
    playlist = Playlist()
    while True:
        command = input(
            "Enter command add_song, remove_song, play_next,"
            "play_previous, show_current_song, show_playlist, or exit: "
        )

        if command == "add_song":
            title = input("Enter title: ")
            artist = input("Enter artist: ")
            result = playlist.add_song(title, artist)
            print(result)

        elif command == "remove_song":
            title = input("Enter title: ")
            artist = input("Enter artist: ")
            result = playlist.remove_song(title, artist)
            print(result)
            
        elif command == "play_next":
            result = playlist.play_next()
            print(result)

        elif command == "play_previous":
            result = playlist.play_previous()
            print(result)

        elif command == "show_current_song":
            result = playlist.show_current_song()
            print(result)

        elif command == "show_playlist":
            playlist.display_playlist()

        elif command == "exit":
            print("Exiting playlist manager.")
            exit(0)

        else:
            matched = match_input(command, ["add_song", "remove_song", "play_next",
            "play_previous", "show_current_song", "show_playlist", "exit"])
            if matched:
                print(f"Did you mean mean '{matched[0]}'? Please try again.")
            else:
                print("Unknown command. Please try again.")
