from selenium.webdriver.common.by import By
import re
from dzialanienapliku import sprawdzlink

pattern = r"(x|xs|xr|10|1[1-5])(pro)?(mini)?(max)?"



def gettelefony(driver):
    telefony = []
    el = driver.find_elements(By.CLASS_NAME, "css-l9drzq")
    cena=""
    for i in el:
        cenastr=i.find_element(By.CLASS_NAME,"css-13afqrm")
        link=i.find_element(By.TAG_NAME,"a").get_attribute("href")
        nazwastr=i.find_element(By.CLASS_NAME,"css-1s3qyje")
        lokalizacja=i.find_element(By.CLASS_NAME,"css-1mwdrlh").text
        try:
            cena=''.join(filter(str.isdigit, cenastr.text))
            cena.replace(",",".")
            cena=float(cena)
        except:
            pass
            #print(cenastr.text)
        nazwa=re.findall(pattern, nazwastr.text.replace(" ",""), re.IGNORECASE)
        index=nazwastr.text.lower().find("gb")
        pamiec= "" if index==-1 else nazwastr.text[index-3:index].replace(" ","")

        try:
            if sprawdzlink(link)!=1:
                nazwacala = f"iphone {'x' if nazwa[0][0] == '10' else nazwa[0][0]} {nazwa[0][1]} {nazwa[0][2]} {nazwa[0][3]}"
                telefony.append({
                    "nazwa": nazwacala.lower().replace(" ",""),
                    "cena": cena,
                    "pamiec": pamiec,
                    "lokalizacja": lokalizacja,
                    "link": link

                })



        except:
            nazwacala=nazwastr.text
            #print(f"zła nazwa nie przeszła regex{nazwacala}, {cena}, {link}")

    return telefony




