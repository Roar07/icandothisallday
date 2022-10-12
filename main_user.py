import fetch1
import fetch2
import datetime 
import os
from dotenv import load_dotenv
now=datetime.datetime.now()

load_dotenv()
# print(os.getenv("Private_key"))

# taking inputs --------
apikey=input("API-key= ")
start_with=input("name start with = ")

now=now.strftime("%d/%m/%Y,%H:%M:%S")
import hashlib
hash = hashlib.md5( (now +os.getenv("Private_key")+ apikey).encode())
# print(hash.hexdigest())
# print(now)
# print(fetch1.fetch_data_api(0,now,"1b124b954b9c1a0f78740b153ae73b15",hash.hexdigest(),'a'))

print(fetch2.fetch_data_api_name(now,"1b124b954b9c1a0f78740b153ae73b15",hash.hexdigest(),start_with))
