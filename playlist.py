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
        self.start = None

    def is_empty(self):
        if self.current is None:
            return True
        else:
            return False

    def add_song(self, title, artist):
        if self.is_empty(): # If empty, add first song.
            self.current = SongNode(title, artist) # Make new song the current song.
            self.current.next = self.current # Point next and prev to itself.
            self.current.prev = self.current
            self.start = self.current # Set start to the first song.
            return f"Added {self.current.playlist_display()} as the first song in the playlist."
        else: # If not empty, add new song before current.
            new_song = SongNode(title, artist) # Create new song node.
            new_song.prev = self.current.prev # Make the prev node point to what current's prev was.
            new_song.next = self.current # Make new song's next point to current.
            self.current.prev.next = new_song # If the current node shifts forward and finds no node, 
            self.current.prev = new_song # then it will start at the beginning of the list.
            return f"Added {self.current.playlist_display()} as the first song in the playlist."
    
    def remove_song(self, title):
        pass

    def play_next(self):
        pass

    def play_previous(self):
        pass

    def display_playlist(self):
        playlist = []

        while self.current:
            print(self.current.playlist_display()) # Print for each node it's title and artist.
            playlist.append(self.current.playlist_display()) # Add each node's title and artist to a list.
            self.current = self.current.next # Move to the next node.
            if self.current == self.start: # If we have looped back to the start, break.
                break # Since it's circular you need to put a stop to the looping.


    def show_current_song(self):
        pass
