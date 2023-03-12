import discord
import os
from discord.ext import commands
from text_to_speech import tts
from keep_alive import keep_alive
from discord import FFmpegPCMAudio
from chatbot import request, reset

client = commands.Bot(command_prefix='-', intents=discord.Intents.all()) 

@client.event
async def on_ready():
  await client.tree.sync()
  print("Logged into {0.user}".format(client))


@client.tree.command(name="voicechatbot", description="Initializes the VC integrated chatbot")
async def voicechatbot(interaction:discord.Interaction):
    reset()
    await interaction.response.send_message("Chatbot initialized, use $help command for list of commands.")
    await interaction.channel.send("what would you like to talk about?")
    
    if (interaction.user.voice):
      channel = interaction.user.voice.channel
      voice = await channel.connect()
    else:
      await interaction.channel.send("not in vc")
  
    while True:
      msg = await client.wait_for("message")
      
      if msg.content == "/stop":
        await voice.disconnect()
        await msg.channel.send("Chatbot Shutting Down...")
        break

      elif msg.content == "/help":
        
        await msg.channel.send("commands: $stop")

      else:
          
        message = msg.content
        author = msg.author
        response = request(message, author)
        tts(response)
        source = FFmpegPCMAudio("voiceOutput.mp3")
        voice.play(source)
        await msg.channel.send(response)






@client.tree.command(name="textchatbot", description="Initializes the text based chatbot")
async def textchatbot(interaction:discord.Interaction): 
    reset()
    await interaction.response.send_message("Chatbot initialized, use $help command for list of commands.")
    await interaction.channel.send("what would you like to talk about?")
    
    while True:
      msg = await client.wait_for("message")
      if msg.content == "/stop":
        await msg.channel.send("Chatbot Shutting Down...")
        break

      elif msg.content == "/help":
        
        await msg.channel.send("commands: $stop")
      
      else:

        message = msg.content
        author = msg.author
        response = request(message, author)
        await msg.channel.send(response)


  
keep_alive()
client.run(os.environ['TOKEN'])
