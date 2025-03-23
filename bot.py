import discord  # For interacting with Discord
import random   # To pick a random quote
import os       # To read environment variables
from dotenv import load_dotenv  # To load .env file

# Load the DISCORD_TOKEN from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Create a Discord client with default intents
intents = discord.Intents.default()
intents.message_content = True  # ← THIS IS REQUIRED
client = discord.Client(intents=intents)

# Function to get a random quote from quotes.txt
def get_random_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

# Event: When the bot successfully logs in
@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

# Event: When a message is sent in any channel
@client.event
async def on_message(message):
    # Don't respond to messages sent by the bot itself
    if message.author == client.user:
        return

    # If the message starts with !quote
    if message.content.startswith("!quote"):
        quote = get_random_quote()
        await message.channel.send(f"📚 {quote}")

# Run the bot using the token
client.run(TOKEN)
