import requests
resp = requests.get("https://api.telegram.org//getUpdates")

#to send messages
base_url = "https://api.telegram.org//deleteMessage"
parameters = {
    "chat_id" : "",
    "message_id" :input ("Enter Your TEXT here: ")  
}

resp = requests.get(base_url, data = parameters)
print(resp.text)
