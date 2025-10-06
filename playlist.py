class SongNode:
    # Represents one song.
    def __init__(self, title, artist, next=None, prev=None):
        self.title = title
        self.artist = artist
        self.next = next
        self.prev = prev

    def playlist_display(self): 
        return f"[{self.title}] - [{self.artist}]"


class Playlist:
    # Manages the list and navigation.
    def __init__(self):
        self.current = None

    def is_empty(self):
        pass

    def add_song(self, title, artist):
        pass

    def remove_song(self, title):
        pass

    def play_next(self):
        pass

    def play_previous(self):
        pass

    def display_playlist(self):
        pass

    def show_current_song(self):
        pass
