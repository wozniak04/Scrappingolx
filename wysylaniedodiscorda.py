import discord
import os


intents = discord.Intents.default()
intents.messages = True  # Jeśli bot ma odczytywać i wysyłać wiadomości
Token = os.getenv("Token")
# Prawidłowe utworzenie klienta z intencjami
client = discord.Client(intents=intents)
kanal=int(os.getenv("IDchannel"))

# Wydarzenie: bot gotowy do działania
@client.event
async def on_ready():
    print(f'Bot zalogowany jako {client.user}')



async def send_phone(telefony):
    for i in telefony:
        print(i)
        # try:
            
        #     channel = await client.fetch_channel(kanal)
        #     await channel.send("Hello world") 
        # except discord.NotFound:
        #     print("Kanał o podanym ID nie istnieje.")
        # except discord.Forbidden:
        #     print("Bot nie ma wystarczających uprawnień do dostępu do kanału.")
        # except discord.HTTPException as e:
        #     print(f"Nie udało się wysłać wiadomości: {e}")



client.run(Token)