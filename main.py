from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
from selenium.webdriver.chrome.options import Options
from przejscie_po_zakladkach import przechodzenie
from wysylaniedodiscorda import send_phone

# Set options for ChromeDriver*
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")

# Funkcja główna, która będzie wywoływała asynchronicznie send_phone
async def main():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/q-iphone")

    zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME, "a")
    liczba_zakladek = int(zakladka[3].text)
    nr_zakladki = 1
    dobreceny = []

    while nr_zakladki <= liczba_zakladek:
        wynik = przechodzenie(driver, zakladka, nr_zakladki, liczba_zakladek)
        liczba_zakladek = wynik[0]
        dobreceny.extend(wynik[1])
        zakladka = wynik[2]
        nr_zakladki += 1
        if nr_zakladki == (liczba_zakladek + 1):
            nr_zakladki = 1
        await send_phone(dobreceny)  # Wywołanie asynchroniczne
        dobreceny=[]

    driver.quit()

# Uruchomienie głównej funkcji
asyncio.run(main())
