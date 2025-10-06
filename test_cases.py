from playlist import SongNode, Playlist

def test_function():
    song = SongNode("Way Out There", "Lord Huron")
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

test_function()
test_node()
