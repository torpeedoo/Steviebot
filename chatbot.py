import requests

url = "https://waifu.p.rapidapi.com/path"

def request(content, author):
  querystring =     {"user_id":"sample_user_id","message":content,"from_name":author,"to_name":"Stevie",
  "situation":"conversation","translate_from":"auto","translate_to":"auto"}

  payload = {}

  headers = {
	  "content-type": "application/json",
	  "X-RapidAPI-Host": "waifu.p.rapidapi.com",
	  "X-RapidAPI-Key": "a06f36d888mshac45a0eacccdc2cp1cbcd1jsn3f55394800a6"
  }

  response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

  return response.text

def reset():
  headers1 = {
  	"X-RapidAPI-Key": "a06f36d888mshac45a0eacccdc2cp1cbcd1jsn3f55394800a6",
  	"X-RapidAPI-Host": "waifu.p.rapidapi.com"
  }

  requests.request("DELETE", url, headers=headers1)
