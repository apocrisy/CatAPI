import requests
from behave import *
from payLoad import *
from utilities.resources import *
from utilities.configurations import *
from utilities.reusable import *
import json

@given('Looking for a cat over TheCatAPI in breeds endpoint')
def step_impl(context):
    context.headers = {"Content-Type": "application/json","x-api-key":"78c829f9-e87f-4bf6-8699-03e335fa1e20" }
    context.url = getConfig()['API']['prod'] + ApiResource.breeds


@when('Get request is sent to TheCatAPI breeds')
def step_impl(context):
    payload ={}
    context.response = requests.request("GET", context.url, data=payload, headers=context.headers)


@then('status code of response should be 200')
def step_impl(context):
    context.response_json = context.response.json()
    assert context.response.status_code == 200


@then('List should contain cats that are hypoallergenic, dog friendly and do not shed.')
def step_impl(context):
    for i in context.response_json:
        if i['hypoallergenic'] == 1:
            assert i['hypoallergenic'] == 1
            if i['dog_friendly'] == 5:
                assert i['dog_friendly'] == 5
                if i['shedding_level'] == 1:
                    assert i['shedding_level'] == 1
                    print("{} {} {} {} {} {} {} {} {}".format("Name: ", i['name'], "\n", "Shedding level: ",
                                                              i['shedding_level'], "\n", "Hypoallergenic: ",
                                                              i['hypoallergenic'], "\n"))
