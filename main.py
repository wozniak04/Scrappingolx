from telefony import gettelefony
from szukanieokazji import okazje
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/q-iphone/")

zakladka=driver.find_element(By.CLASS_NAME,"css-4mw0p4")
zakladka=zakladka.find_elements(By.TAG_NAME,"a")
liczba_zakladek=int(zakladka[3].text)
print(zakladka)
nr_zakladki=1
dobreceny=[]
print(zakladka[0].text)
while nr_zakladki>=liczba_zakladek:
    for i in range(0,liczba_zakladek):
        dobreceny.append(okazje(gettelefony(driver)))
    if nr_zakladki==liczba_zakladek:
        nr_zakladki=1
        zakladka[0].click()
        zakladka = driver.find_element(By.CLASS_NAME, "css-4mw0p4")


# iphony=gettelefony(driver)
# driver.quit()
# gitceny=okazje(iphony)
# print(f" {len(iphony)} {len(gitceny)}")
# print(gitceny)


