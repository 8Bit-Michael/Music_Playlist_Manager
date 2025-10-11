Hello, this repository consists of a music playlist manager I created using circular doubly linked lists. Each song is stored as a node containing its title and artist. 
The user can interactively manage the playlist using a simple text-based interface.

To run this project Make sure both main.py and playlist.py are in the same directory, run the project using main.py, and you will be given a prompt in the
command line interface.

The following is an example of how the manager can be used:

Enter command add_song
Enter title: The Night We Met
Enter artist: Lord Huron
Added [The Night We Met] - [Lord Huron] as the first song in the playlist.

Enter command add_song
Enter title: Meet Me in the Woods
Enter artist: Lord Huron
Added [The Night We Met] - [Lord Huron] as the first song in the playlist.

Enter command add_song
Enter title: Wait by the River
Enter artist: Lord Huron
Added [The Night We Met] - [Lord Huron] as the first song in the playlist.

Enter command add_song
Enter title: When the Night is Over
Enter artist: Lord Huron
Added [The Night We Met] - [Lord Huron] as the first song in the playlist.

Enter command add_song
Enter title: Fool for Love
Enter artist: Lord Huron
Added [Fool for Love] - [Lord Huron] to the playlist.

Enter command show_playlist
[The Night We Met] - [Lord Huron]
[Meet Me in the Woods] - [Lord Huron]
[Wait by the River] - [Lord Huron]
[When the Night is Over] - [Lord Huron]
[Fool for Love] - [Lord Huron]

Enter command show_current_song
[The Night We Met] - [Lord Huron]

Enter command play_next
Current node [Meet Me in the Woods] - [Lord Huron]

Enter command play_next
Current node [Wait by the River] - [Lord Huron]

Enter command play_previous
(Current node set to [Meet Me in the Woods] - [Lord Huron])

Enter command remove_song
Enter title: Fool for Love
Removed Fool for Love from the playlist.

Enter command show_playlist
[The Night We Met] - [Lord Huron]
[Meet Me in the Woods] - [Lord Huron]
[Wait by the River] - [Lord Huron]
[When the Night is Over] - [Lord Huron]

Enter command exit
Exiting playlist manager.


Enter command exit
Exiting playlist manager.
