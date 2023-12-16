#Import 
import Discord_API
import tray
import UI_API
from API import D_API
import json
import threading
import time





with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)

def import_ui():
    UI = UI_API.UI_API()
    UI.show()
    
tray.main()

def set_status():
    DAPI = Discord_API.Discord_API(data["authToken"])
    for i in range(len(data["animation"])):
        time.sleep(data["timeout"]/1000)
        DAPI.set_cstatus(text=data["animation"][i]["text"], emoji=data["animation"][i]["emoji_name"])
    
    
#t1 = threading.Thread(target=import_ui)
#t1.start()
#
#t2 = threading.Thread(target=set_status)
#t2.start()




    