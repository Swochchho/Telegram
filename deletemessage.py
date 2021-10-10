import requests
resp = requests.get("https://api.telegram.org/bot2020906583:AAEU3u405rf6MwrF_blHQbkFTaUlM3DbCdU/getUpdates")

#to send messages
base_url = "https://api.telegram.org/bot2020906583:AAEU3u405rf6MwrF_blHQbkFTaUlM3DbCdU/deleteMessage"
parameters = {
    "chat_id" : "-507611847",
    "message_id" :input ("Enter Your TEXT here: ")  
}

resp = requests.get(base_url, data = parameters)
print(resp.text)
