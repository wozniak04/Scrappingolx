from time import sleep
from random import randint
from telefony import gettelefony
from szukanieokazji import okazje
from selenium.webdriver.common.by import By
from selenium import webdriver
from zamknieciepopup import zamknieciepopupu



def przechodzenie(driver,zakladka):
    zakladka = zakladka.find_elements(By.TAG_NAME, "a")
    liczba_zakladek = int(zakladka[3].text)
    print(f"liczba_zakladek {liczba_zakladek}")
    nr_zakladki = 1
    dobreceny = []
    while nr_zakladki <= liczba_zakladek:
        sleep(randint(1, 3))
        print(f"numer petli:{nr_zakladki}\n {driver.current_url}")
        dobreceny.extend(okazje(gettelefony(driver)))
        zamknieciepopupu(driver)
        if nr_zakladki == liczba_zakladek:
            nr_zakladki = 1
            zakladka[1].click()
            sleep(3)
            zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4")
            liczba_zakladek = int(zakladka[3].text)
            dobreceny = []
            sleep(randint(20, 240))
        else:
            sleep(2)
            if nr_zakladki in range(2, 4) or nr_zakladki in range((liczba_zakladek - 2), liczba_zakladek):
                print(f"zakladka if kliknieta {zakladka[5].text}")
                zakladka[5].click()
                sleep(3)
                zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME, 'a')
                try:
                    liczba_zakladek = int(zakladka[4].text)
                except:
                    liczba_zakladek = int(zakladka[3].text)
            else:
                zakladka[4].click()
                print(f"zakladka else kliknieta ")
                sleep(3)
                zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME, 'a')
                if nr_zakladki != 1:
                    liczba_zakladek = int(zakladka[3].text)
                else:
                    liczba_zakladek = int(zakladka[4].text)

            nr_zakladki += 1
            print(f"liczba_zakladek wszystkich {liczba_zakladek}")
            print(f"okazje {len(dobreceny)} zakladka {nr_zakladki}")
            sleep(randint(1, 7))