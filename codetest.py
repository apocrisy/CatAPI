import requests
from payLoad import *
from utilities.configurations import *
from utilities.reusable import *
from utilities.resources import *

import requests
import json

url = "https://api.thecatapi.com/v1/breeds"

payload={}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

abc = response.json()

for i in abc:
  if i['hypoallergenic']==1:
    if i['dog_friendly']==5:
      if i['shedding_level']==1:
        print("{} {} {} {} {} {} {} {} {}".format("Name: ",i['name'], "\n", "Shedding level: ", i['shedding_level'],"\n", "Hypoallergenic: ", i['hypoallergenic'],"\n"))





