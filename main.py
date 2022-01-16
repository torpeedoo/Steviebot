import discord
from discord import FFmpegPCMAudio
import os
import requests
import random
import time

from keep_alive import keep_alive

client = discord.Client()


#list of quotes that can be said by bot if activated
dababy_quotes = ["https://tenor.com/view/binchiling-john-cena-gif-22115595"]
rustcode = ""
soundPaths = ["steve.mp3", "WELCOME TO MY CHANNEL.mp3"]


@client.event
async def on_ready():
  print("Logged into {0.user}".format(client))

#if message is detected then do one of the things below
@client.event 
async def on_message(message):
  if message.author == client.user:
    return

#selecting random thing to say from quotes list
  if "Stevie" in message.content:
    await message.channel.send(random.choice(dababy_quotes))

#adding something to the quotes list
  if "$add" in message.content:
    await message.channel.send("Word to add:")
    msg = await client.wait_for('message')
    dababy_quotes.append(str(msg.content))
    await message.channel.send("Added!")

#command to start the ai chatbot
  if "talk to me stevie" in message.content:
    url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
    stopsign = "\N{THUMBS UP SIGN}"

    await message.channel.send("Start the conversation by saying something")
    
    while True:

      msg = await client.wait_for('message')

#if the message after starting the conversation is $leave then the chatbot loop is ended
      if str(msg.content) == "see ya stevie":
        break
      
      querystring = {"bid":"178","key":"sX5A2PcYZbsN5EY6","uid":"mashape","msg":str(msg.content)}

      headers = {
          'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com",
          'x-rapidapi-key': "f6ea58b7d1msh4bc1d05012a6974p1139a9jsn2a6eab173bd8"
          }

      response = requests.request("GET", url, headers=headers, params=querystring)
      responsedict = response.json()

      print(responsedict)
      await message.channel.send(responsedict["cnt"])
      await message.add_reaction(stopsign)


  if "$vc" in message.content:
    channel = message.author.voice.channel
    if channel != None:
      vc = await channel.connect()
      source = FFmpegPCMAudio(random.choice(soundPaths))
      vc.play(source)
      
      time.sleep(10)

      await vc.disconnect()

    else:
      print("must be in vc")


#pinging the web server so it can continuously run
keep_alive()
client.run(os.getenv("TOKEN"))