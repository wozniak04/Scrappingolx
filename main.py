from time import sleep
from random import randint
from telefony import gettelefony
from szukanieokazji import okazje
from selenium.webdriver.common.by import By
from selenium import webdriver
from zamknieciepopup import zamknieciepopupu
driver = webdriver.Chrome()
driver.get("https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/q-iphone/")

zakladka=driver.find_element(By.CLASS_NAME,"css-4mw0p4")
zakladka=zakladka.find_elements(By.TAG_NAME,"a")
liczba_zakladek=int(zakladka[3].text)
nr_zakladki=1
dobreceny=[]
while nr_zakladki<=liczba_zakladek:
    sleep(randint(1,7))
    dobreceny.extend(okazje(gettelefony(driver)))
    zamknieciepopupu(driver)
    if nr_zakladki==liczba_zakladek:
        nr_zakladki=1
        zakladka[0].click()
        zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4")
        liczba_zakladek = int(zakladka[3].text)
        dobreceny=[]
        sleep(randint(20,240))
    else:
        print(zakladka[4].get_attribute('href'))
        sleep(2)
        if not (nr_zakladki==2 or nr_zakladki==3 or nr_zakladki==liczba_zakladek-1 or nr_zakladki==liczba_zakladek-2):
            zakladka[4].click()
            sleep(3)
            zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME,'a')
            liczba_zakladek=int(zakladka[3].text)
        else:
            zakladka[5].click()
            sleep(3)
            zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4").find_elements(By.TAG_NAME,'a')
            liczba_zakladek=int(zakladka[4].text)


        #     print(liczba_zakladek)
        # print(f"okazje {len(dobreceny)}")
        sleep(randint(12,35))

driver.quit()



