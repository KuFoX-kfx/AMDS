import Discord_API
from API import D_API
import json
import time


with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
leng = len(data["animation"])

print(data["timeout"])
print(data["authToken"])
for i in range(leng):
    print(data["animation"][i]["text"])
    print(data["animation"][i]["emoji_name"])
    time.sleep(1)
    
#DAPI = Discord_API(D_API)



