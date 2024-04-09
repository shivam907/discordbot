import random
import discord
import requests
def get_api_response(var):
    base_url='https://api.api-ninjas.com/v1/cars?'
    if(len(var)==1):
        base_url+="model="+var[0]
    if(len(var)==2):
        base_url+="model="+var[0]+'&'
        base_url+="make="+var[1]
    if(len(var)==3):
        base_url+="model="+var[0]+'&'
        base_url+="make="+var[1]+'&'
        base_url+="transmission="+var[2]
    # model = 'camry'
    # api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
    print(base_url)
    response = requests.get(base_url, headers={'X-Api-Key': 'Ek3HT9c+gj5uxqRyAHSDhg==mWVtx3syErnsrg7C'})
    if response.status_code == requests.codes.ok:
        print(response.text)
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
def get_response(message: str) -> str:
    p_message=message.lower()
    print("hello", message)
    if p_message=='hello':
        return 'Hey There'

    if message == 'roll':
        return str(random.randint(1,6))

    if p_message=='!help':
        return'This is a help message that youncan modify later'
    if p_message.startswith("!car"):
        var=p_message.split(" ")
        var=var[1:]
        res= get_api_response(var)
        print("res", type(res))
        message = ''
        for i in range(len(res)):
            message += "Car " + str(i+1) + "\n"
            kys = res[i].keys()
            for key in kys:
                message += str(key) + ": " + str(res[i][key]) + "\n"
            message += "\n\n"
        return message
    return' I didnt understand what you are saying. Try typing !help'