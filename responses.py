import random
import discord
import requests
def get_api_response(params):
    base_url='https://api.api-ninjas.com/v1/cars?'
    keys=list(params.keys())
    for i in range(len(keys)):
        base_url=base_url+keys[i]+"="+params[keys[i]]
        if(i<len(keys)-1):
            base_url+='&'
    # model = 'camry'
    # api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
    print(base_url)
    response = requests.get(base_url, headers={'X-Api-Key': 'Ek3HT9c+gj5uxqRyAHSDhg==mWVtx3syErnsrg7C'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
def get_response(message: str) -> str:
    p_message=message.lower()
    parameters={}
    print("hello", message)
    if p_message=='hello':
        return 'Hey There'

    if message == 'roll':
        return str(random.randint(1,6))

    if p_message=='!help':
        return'This is a help message that youncan modify later'
    if p_message.startswith("!car"):
        var=p_message.split("\n")
        var=var[1:]
        for i in var:
            params=i.split("=")
            parameters[params[0]]=params[1]
        print(parameters)
        get_api_response(parameters)
    return' I didnt understand what you are saying. Try typing !help'