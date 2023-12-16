#Import 
import Discord_API
from API import D_API
import json
import time





with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
DAPI = Discord_API.Discord_API(data["authToken"])

for i in range(len(data["animation"])):
    time.sleep(data["timeout"]/1000)
    DAPI.set_cstatus(text=data["animation"][i]["text"], emoji=data["animation"][i]["emoji_name"])
    