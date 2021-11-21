import discord
import os
import requests
import random
import ast

from keep_alive import keep_alive

client = discord.Client()

dababy_quotes = ["https://tenor.com/view/binchiling-john-cena-gif-22115595"]


@client.event
async def on_ready():
  print("Logged into {0.user}".format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if "Stevie" in message.content:
    await message.channel.send(random.choice(dababy_quotes))

  if "$add" in message.content:
    await message.channel.send("Word to add:")
    msg = await client.wait_for('message')
    dababy_quotes.append(str(msg.content))
    await message.channel.send("Added!")

  if "conversation" in message.content:
    url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

    await message.channel.send("Start the conversation by saying something")
    
    while True:

      msg = await client.wait_for('message')
      if str(msg.content) == "$done":
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


keep_alive()
client.run(os.getenv("TOKEN"))