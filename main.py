from random import randint
import discord
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from przejscie_po_zakladkach import przechodzenie
from asyncio import sleep

#selenium
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=options)
driver.get("https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/q-iphone")


#discord
intents = discord.Intents.default()
intents.messages = True
Token = os.getenv("Token")
client = discord.Client(intents=intents)
kanal=int(os.getenv("IDchannel"))

# Wydarzenie: bot gotowy do działania
@client.event
async def on_ready():
    print(f'Bot zalogowany jako {client.user}')
    zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME, "a")
    liczba_zakladek = int(zakladka[3].text)
    nr_zakladki = 1
    dobreceny = []

    while nr_zakladki <= liczba_zakladek:
        wynik = await przechodzenie(driver, zakladka, nr_zakladki, liczba_zakladek)
        liczba_zakladek = wynik[0]
        dobreceny.extend(wynik[1])
        zakladka = wynik[2]
        nr_zakladki += 1
        if nr_zakladki == (liczba_zakladek + 1):
            nr_zakladki = 1
        await send_phone(dobreceny)
        dobreceny = []

    driver.quit()


async def send_phone(telefony):
    for i in telefony:
        print(i)
        try:

            channel = await client.fetch_channel(kanal)
            await channel.send(f"{i['nazwa']} {i['pamiec']+'gb'}    {i['cena']}zł \n {i['lokalizacja']} \n {i['link']}")
        except discord.NotFound:
            print("Kanał o podanym ID nie istnieje.")
        except discord.Forbidden:
            print("Bot nie ma wystarczających uprawnień do dostępu do kanału.")
        except discord.HTTPException as e:
            print(f"Nie udało się wysłać wiadomości: {e}")
        await sleep(randint(3,10))
client.run(Token)


