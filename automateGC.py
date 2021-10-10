import requests
resp = requests.get("https://api.telegram.org//getUpdates")

#to send messages
base_url = "https://api.telegram.org//sendMessage"
parameters = {
    "chat_id" : "",
    "text" :input ("Enter Your TEXT here: ")  
}

resp = requests.get(base_url, data = parameters)
print(resp.text)
