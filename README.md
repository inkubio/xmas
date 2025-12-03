# Xmas Spotify
Lighting up guild members life during December at the guild room.
The script taps into the spotify api, checks whether the playlist is correct and even playing and then defaults to a specified playlist.

You can set the spotify user info in the config file. Like the playlists you want to default back to.

Currently the script is playing on the guildroom computer as a constant system d service on the background. If you want to disable it, there are instructions next to the code files so please DO NOT touch the script itself.

Rigth now the Spotify API doesn't let us do much but things for the future as these work to bypass the workings of the script:
- Adding songs to the queue
--> Emptying the queue if the songs don't belong to the playlist 
- Jam going on
--> Stopping the jams
