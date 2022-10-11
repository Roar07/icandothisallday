import requests;
import pandas as pd
def fetch_data_api(offset,key,Hash,name_start_with) :
    
    payload= {  'ts':'1',
            'apikey': key,
            'hash' : Hash ,
          'limit':'100',
          'offset':offset,
        'nameStartsWith': name_start_with
         }
    r = requests.get("http://gateway.marvel.com/v1/public/characters" ,params = payload)
    print(r.status_code,r.reason)
    if(r.status_code != 200):
        raise Exception(r.reason)
    df = pd.read_json(r.url)
    data=df['data']['results']
    df1= pd.json_normalize(data)
    return df1[['id','name','comics.available','series.available','stories.available','events.available']]

# name = input('name')

# print(name *10)