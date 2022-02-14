# Imports
import discord
import os
import requests
import asyncio
from dotenv import load_dotenv

#Load Discord Token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

    # Counters for shell output
    index = 0
    message_counter = 0

    # Enter Channel ID to collect memes from
    channel = client.get_channel()

    # Add "limit=6969" for example to set a message history limit in channel.history()
    messages = await channel.history().flatten()

    # For all message
    for msg in messages:

        # For each attachement
        for attachment in msg.attachments:

            # Get filename
            filename = attachment.url
            filename = filename.rsplit('/', 1)[1]
            print("Gonna download: " + filename)
            
            # Fetch file content
            meme = requests.get(attachment.url, allow_redirects=True)

            # Write attachement in file with the same filename
            open("downloads/" + str(index) + "-" + filename, 'wb').write(meme.content)
            print(filename + " downloaded!                         Download NR: " + str(index))

            # Count download counter up
            index = int(index) +1

            # Wait for 0.3 Secs so Discord doesnt block the Bot for spamming
            await asyncio.sleep(0.3)

        # Count message counter up
        print("Message: " + str(message_counter))
        message_counter = int(message_counter) + 1
    
    # We're done!
    print("Download done!")

client.run(token)