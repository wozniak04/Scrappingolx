from asyncio import sleep
from random import randint
from telefony import gettelefony
from szukanieokazji import okazje
from selenium.webdriver.common.by import By
from zamknieciepopup import zamknieciepopupu


#funkcja zwraca liczbe zakladek i znalezione oferty
async def przechodzenie(driver,zakladka,nr_zakladki,liczba_zakladek):
    #print(f"liczba_zakladek {liczba_zakladek}")
    dobreceny = []
#wyswietlenie zakładki i url strony
    #print(f"numer petli:{nr_zakladki}\n {driver.current_url}")
    dobreceny.extend(okazje(gettelefony(driver))) #pobieranie okazyjnych ofert
    await sleep(1)
    zamknieciepopupu(driver) #zaakceptowanie cookies jezeli sa

    #przechodzenie znowu do zakładki pierwszej jeżeli zeskanowaliśmy ostatnia
    if nr_zakladki == liczba_zakladek:
        driver.get("https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/q-iphone/")
        await sleep(randint(3,7))
        zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME, 'a')
        liczba_zakladek = int(zakladka[3].text)
        #await sleep(randint(200, 2400))

    else:
        #warunek sprawdza w jakiej zakladce jestesmy w zaleznosci od niej przycisk next jest w roznych indeksach
        if nr_zakladki in range(2, 4) or nr_zakladki in range((liczba_zakladek - 2), liczba_zakladek):
            #print(f"zakladka if kliknieta ")
            # przejscie do nastepnej zakladki
            zakladka[5].click()
            await sleep(randint(3,7))
            #przypisanie następnej zakładki
            zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME, 'a')
            try:
                liczba_zakladek = int(zakladka[4].text)
            except:
                liczba_zakladek = int(zakladka[3].text)
        else:
            # przejscie do nastepnej zakladki
            zakladka[4].click()
            #print(f"zakladka else kliknieta ")
            # zatrzymanie programu przez dany czas aby strona sie wczytała
            await sleep(randint(3,7))
            #przypisanie do zmiennej zakladka nowe wartości po zmianie strony
            zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME, 'a')
            if nr_zakladki != 1:
                liczba_zakladek = int(zakladka[3].text)
            else:
                liczba_zakladek = int(zakladka[4].text)

            await sleep(randint(3, 7))
    return liczba_zakladek,dobreceny,zakladka