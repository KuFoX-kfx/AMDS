#import requests
#from API import D_API
#from fake_useragent import UserAgent
#import time
#ua = UserAgent()
#status = {'text': None, 'expires_at': None, 'emoji_id': None, 'emoji_name': None}

#'custom_status': status
#response = requests.get('https://discord.com/api/v9/users/@me/settings', headers={"authorization": D_API})
#print(response.json())

#requests.patch('https://discord.com/api/v9/users/@me/settings', headers={"authorization": D_API, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9021 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36'}, json={'status': online})


#{'text': '06:22:18 PM🌙 • Time_12', 'expires_at': None, 'emoji_id': None, 'emoji_name': '🕒'}
#'2023-12-14T15:55:56.330000+00:00'
#status
#online
#idle
#dnd
#invisible


try: import sys
except: print(f"CRITICAL ERROR | Failed import sys") 
try: import requests
except: print(f"CRITICAL ERROR | Failed import request | {sys.exc_info()}") 
try: import fake_useragent
except: print(f"CRITICAL ERROR | Failed import fake_useragent | {sys.exc_info()}") 
class Discord_API:
    
    def __init__(self, API, UA=None):
        #API
        if str(API) == "": print("ERROR | API key in NULL")
        self.API_KEY = API
        #UA
        if(UA == None): self.UA = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9021 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36"
        elif(UA=="chrome"): self.UA = fake_useragent.UserAgent.chrome()
        elif(UA=="ff"): self.UA = fake_useragent.UserAgent.ff()
        elif(UA=="edge"): self.UA = fake_useragent.UserAgent.edge()
        elif(UA=="safari"): self.UA = fake_useragent.UserAgent.safari()
        elif(UA=="random"): self.UA = fake_useragent.UserAgent.random()
        else: self.UA = UA
        #Request
        response = requests.get('https://discord.com/api/v9/users/@me',
                                headers={"authorization": self.API_KEY, 
                                         'User-Agent': UA})
        #Get answer
        if (response.status_code==200 or response.status_code==201):
            print("LOG | All OK")
        if (response.status_code>=400):
            print(f"ERROR | Error in api discord | {response.reason}")
        
    def set_status(self, text=None, emoji=None):
        try: response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers={"authorization": self.API_KEY, 'User-Agent': self.UA}, json={'custom_status': {"text": text, 'emoji_name': emoji}})
        except: print("ERROR | Status Not CHANGE")
        print(f"LOG | Change Status | {response.reason}")
        
    def get_all(self):
        return requests.get('https://discord.com/api/v9/users/@me/settings', headers={"authorization": self.API_KEY, 'User-Agent': self.UA}).json()