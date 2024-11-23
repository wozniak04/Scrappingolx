from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from przejscie_po_zakladkach import przechodzenie

service = Service(ChromeDriverManager().install())


driver = webdriver.Chrome(service=service)
driver.get("https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/q-iphone")

zakladka=driver.find_element(By.CLASS_NAME,"css-4mw0p4").find_elements(By.TAG_NAME,"a")
liczba_zakladek=int(zakladka[3].text)
nr_zakladki=1
dobreceny=[]

while nr_zakladki<=liczba_zakladek:

    wynik=przechodzenie(driver,zakladka,nr_zakladki,liczba_zakladek)
    liczba_zakladek=wynik[0]
    dobreceny.extend(wynik[1])
    zakladka=wynik[2]
    nr_zakladki+=1
    if nr_zakladki==(liczba_zakladek+1):
        nr_zakladki=1
    print(len(dobreceny))



driver.quit()



