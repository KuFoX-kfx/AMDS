import Discord_API
from API import D_API
import json
import threading
import time

def ther():
    while(True):
        time.sleep(1)
        print("lol")



lol = threading.Thread(target=ther)
lol.setName("lol")
lol.start()
kek = threading.enumerate()
for i in kek:
    print(i.name)
print(kek)


#with open("AMDS-kfx.json", "r", encoding="utf8") as json_file: data = json.load(json_file)
#leng = len(data["animation"])
#
#print(data["timeout"])
#print(data["authToken"])
#for i in range(leng):
#    print(data["animation"][i]["text"])
#    print(data["animation"][i]["emoji_name"])
#    time.sleep(1)
    
#DAPI = Discord_API(D_API)



