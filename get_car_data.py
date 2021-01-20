import json
import urllib
import pandas as pd
import requests

url = 'https://parseapi.back4app.com/classes/Carmodels_Car_Model_List?limit=9581'
headers = {
    'X-Parse-Application-Id': 'Gz3dE5Dsk7oxifKGZM8hROyVgri1PWsvJAts4XSz', # This is your app's application id
    'X-Parse-REST-API-Key': 'gpKVqhx0X5BdauODoMojAXKXbetkcq4eTHhGE7HX' # This is your app's REST API key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
json_data = json.dumps(data)
df = pd.read_json(json_data)
df.to_csv("car_dataset.csv", index= None)

print(json.dumps(data, indent=2))
