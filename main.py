import fetch1
import fetch2
import datetime 
now=datetime.datetime.now()


now=now.strftime("%d/%m/%Y,%H:%M:%S")
import hashlib
hash = hashlib.md5( (now +"1dbd0287f2bf85c8ad18b654f3863fb131a57528"+ '1b124b954b9c1a0f78740b153ae73b15').encode())
print(hash.hexdigest())
print(now)
# print(fetch1.fetch_data_api(0,now,"1b124b954b9c1a0f78740b153ae73b15",hash.hexdigest(),'a'))
print(fetch2.fetch_data_api_name(now,"1b124b954b9c1a0f78740b153ae73b15",hash.hexdigest(),'s'))
