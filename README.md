
# Python Discord Downloader

This is a little discord bot i wrote for downloading attachements in one channel on start of the bot.

## Installation

Clone the repo and install the dependencies:

```shell
clone https://github.com/Cybercube21/python-discord-downloader.git
cd python-discord-downloader
pip3 install -r requirements.txt
```

## Usage
To start, you first have to add a ".env" file and insert your token like this:
```
# .env
DISCORD_TOKEN="<Insert bot token here>"
```

Then you'll have to change the channel ID in the downloader.py like this:\
```
channel = client.get_channel(<Insert Channel ID here>)
```

On default it will scan the last 100 messages and download the attachements, if there are some.\
You can increase that limit easily if you change following line like this:
```
messages = await channel.history(limit=6969).flatten()
```

Create a folder called "downloads" and just execute the script:
```shell
python3 ./downloader.py
```
## Contact 
Join my [Discord Server](https://discord.gg/4XYcD2Jk54) or DM me: Cybercube#0499

## License
[MIT](https://opensource.org/licenses/MIT)