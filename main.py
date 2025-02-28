from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response


print("Environment Variables in Railway:")
for key, value in os.environ.items():
    print(f"{key}={value}")

TOKEN: Final = os.getenv('DISCORD_TOKEN')



if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN is not set. Make sure it is correctly configured in Railway.")

print(f"DISCORD_TOKEN: {TOKEN}")


intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    
    is_private = (user_message[0] == '?')
    if is_private :
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
   
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")
    
@client.event
async def on_message(message : Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    
def main() -> None:
    client.run(token = TOKEN)
    
    
if __name__ == "__main__":
    main()
