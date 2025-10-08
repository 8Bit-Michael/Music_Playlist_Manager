from playlist import SongNode, Playlist
playlist = Playlist()

def test_function():
    print('--- Test Function ---')
    song = SongNode("The Night We Met", "Lord Huron")
    result = song.playlist_display()
    print(result)

def test_node():
    print('--- Test Node ---')
    node = SongNode(
        title="Do You Remember The Times",
        artist="ISLAND",
        next=None,
        prev=None
    )
    print(node.playlist_display())

def test_add_song():
    print('--- Add Song ---')
    playlist.add_song("All The Right Moves", "OneRepublic")
    playlist.add_song("Standing In The Middle Of The Field", "Haiku From Zero")
    playlist.add_song("Miol Mor Mara", "Outsider")
    playlist.add_song("Way Out There", "Lord Huron")
    playlist.display_playlist()

def prev_test():
    print('--- Previous Test ---')
    if playlist.is_empty():
        print("Playlist is empty.")
    else:
        playlist.play_previous()
        print(playlist.show_current_song())

def next_test():
    print('--- Next Test ---')
    if playlist.is_empty():
        print("Playlist is empty.")
    else:
        playlist.play_next() # It's not returning None, but it's not going to print it
        print(playlist.show_current_song()) # because the value has only been returned.

def remove_test():
    print('--- Remove Test ---')
    if playlist.is_empty():
        print("Playlist is empty.")
    else:
        print(playlist.remove_song("Standing In The Middle Of The Field"))
        playlist.display_playlist() # Where is All The Right Moves now?

test_function()
test_node()
test_add_song()
next_test()
prev_test()
remove_test()
