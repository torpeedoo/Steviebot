import discord
import os
import requests
import random
import time

from keep_alive import keep_alive


client = discord.Client()

url = "https://waifu.p.rapidapi.com/path"

def request(content, author):
  querystring = {"user_id":"sample_user_id","message":content,"from_name":author,"to_name":"Stevie",
  "situation":"Girl loves Boy.","translate_from":"auto","translate_to":"auto"}

  payload = {}

  headers = {
	  "content-type": "application/json",
	  "X-RapidAPI-Host": "waifu.p.rapidapi.com",
	  "X-RapidAPI-Key": "f6ea58b7d1msh4bc1d05012a6974p1139a9jsn2a6eab173bd8"
  }

  response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

  return response.text
  

@client.event
async def on_ready():
  print("Logged into {0.user}".format(client))
  

#if ctx is detected then do one of the things below
@client.event 
async def on_message(ctx):
  if ctx.author == client.user:
    return
  
  elif "$talk to me" in ctx.content:
    await ctx.channel.send("what do you want to talk about?")

    while True:
      msg = await client.wait_for("message")
      if msg.content == "$stop":
        break
      else:
        message = msg.content
        author = msg.author
        response = request(message, author)
        await ctx.channel.send(response)

      

    

    
#pinging the web server so it can continuously run
keep_alive()
client.run(os.getenv("TOKEN"))