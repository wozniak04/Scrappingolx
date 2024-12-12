
from selenium.webdriver.common.by import By
#zamykanie popapu cookies jezeli jest
def zamknieciepopupu(driver):
    try:
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    except:
        print("zamkniety")

