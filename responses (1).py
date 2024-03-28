import random
import discord

def get_response(message: str) -> str:
    p_message=message.lower()

    if p_message=='hello':
        return 'Hey There'

    if message == 'roll':
        return str(random.randint(1,6))

    if p_message=='!help':
        return'This is a help message that youncan modify later'

    return' I didnt understand what you are saying. Try typing !help'