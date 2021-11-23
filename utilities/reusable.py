import requests
from utilities.configurations import *
from utilities.resources import *

def Login(stage, user):
    url = getConfig()['API'][stage] + '/api/v1/users/login'

    headers = {"Content-Type": "application/json"}

    loginResponse = requests.post(url, json=userType[user], headers=headers)

    c = loginResponse.json()

    accessToken = c['accessToken']

    print('access token passed is ' + accessToken)
    print(type(accessToken))

    return accessToken