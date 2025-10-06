from playlist import SongNode, Playlist

def test_function():
    song = SongNode("The Night We Met", "Lord Huron")
    result = song.playlist_display()
    print(result)

def test_node():
    node = SongNode(
        title="Do You Remember The Times",
        artist="ISLAND",
        next=None,
        prev=None
    )
    print(node.playlist_display())

def test_add_song():
    playlist = Playlist()
    playlist.add_song("All The Right Moves", "OneRepublic")
    playlist.add_song("Standing In The Middle Of The Field", "Haiku From Zero")
    playlist.add_song("Miol Mor Mara", "Outsider")
    playlist.add_song("Way Out There", "Lord Huron")
    playlist.display_playlist()

test_function()
test_node()
test_add_song()
