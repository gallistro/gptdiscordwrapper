import discord
from discord.ext import commands
import asyncio
from chatgpt_wrapper import ChatGPT
import nest_asyncio

nest_asyncio.apply()

bot = ChatGPT()

def get_message(chatInput):
	response = bot.ask(chatInput)
	return response
	
intents = discord.Intents.all()
client = discord.ext.commands.Bot(intents = intents, command_prefix = ".")

@client.event
async def on_ready():
	print("Bot is ready!")

@client.command(aliases=['gpt'])
async def chatman(ctx, *, chatInput):
		response = get_message(chatInput)
		await ctx.send(f'ChatGPT: {response}')

client.run("{token}")


