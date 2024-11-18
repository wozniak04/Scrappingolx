from time import sleep
from selenium.webdriver.common.by import By

def zamknieciepopupu(driver):
    try:
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    except:
        print("zamkniety")
sleep(2)
