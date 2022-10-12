import fetch1
import fetch2
import datetime 
from dotenv import load_dotenv
import os 


load_dotenv()

now=datetime.datetime.now()

now=now.strftime("%d/%m/%Y,%H:%M:%S")
import hashlib
hash = hashlib.md5( (now + os.getenv("Private_key")+os.getenv("Api_key")).encode())
print(hash.hexdigest())
print(now)
# print(fetch1.fetch_data_api(0,now,"1b124b954b9c1a0f78740b153ae73b15",hash.hexdigest(),'a'))

df =fetch2.fetch_data_api_name(now,"1b124b954b9c1a0f78740b153ae73b15",hash.hexdigest(),'s')
print(df)


# activity 4------------------------------------

column = input("enter column to filter= ")
cond = input("""choose from
1. equal  to 
2. not equal to 
3. less than eqaul to 
4. less than 
5. greater than eqaul to 
6. greater than
choice = """)
value= input (" enter value= ")

print( fetch1.filter_char(df,column,cond,value))
