This project is a proof of concept League of Legends spectator parser.

It is written in python and works most of the time.
It takes in binary data from Riot's restful service and converts it into hex to parse.
The program needs gameid and decryption key to be manually changed.
	I have tried getGameMetaData, but the decryption key is always blank.
This was made near the end of season 4 so I have no idea how season 5 will affect the data in anyway.
All items, runes, masteries are in gameid's and can easily be converted into item names.
An iteresting point with items; items have a base cooldown and an active cooldown, but they are both -1 when the item is not on cooldown.
I believe there is a bug where once a game ends, the program stops and does not print the last ~3 or so keyframes.
I have had a few instanced of it crashing on me, but it is pretty isolated and I have no idea what causes it.

I used https://github.com/loldevs/leaguespec/wiki/REST-Service to help get started and was very helpful. Thanks to everyone who worked on it.
