# Discord.py Bot Template
A template I've made to act as a base to help with the creation of discord bots.
This template has been designed with some little personal oddities of mine, such as the error handler sending unhandled errors to a discord channel.

## Setting up
#### Requirements:
Install the libraries defined in `requirements.txt`. These can all be done via pip.
#### .env file:
* Assign `TOKEN` your bot's token, which can be got at the [Discord Dev Portal](https://discord.com/developers).
* Assign `DEFAULT_PREFIX` a string for the prefix you would like your bot to use. This is useful so multiple bots on the same token can be running with different prefixes, say for testing purposes.
* If you're going to make a GitHub repository for your bot, add `.env` to `gitignore`. This is so your token isn't accidentally committed and made viewable for the whole world to see.
#### error_handler.py:
On line 67 there's a line which gets a channel within my personal discord server, This is done so that an unhandled error can be dumped there. Either replace the channel ID with the ID for a channel in your own server, or just remove the code from lines 62 to 72.
