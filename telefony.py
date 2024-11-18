from selenium.webdriver.common.by import By
import re

pattern = r"\b(x|xs|xr|10|1[1-6])\b(\s+pro)?(\s+mini)?(\s+max)?\b"
telefony=[]



def gettelefony(driver):
    el = driver.find_elements(By.CLASS_NAME, "css-l9drzq")
    for i in el:
        cenastr=i.find_element(By.CLASS_NAME,"css-13afqrm")
        link=i.find_element(By.TAG_NAME,"a").get_attribute("href")
        nazwastr=i.find_element(By.CLASS_NAME,"css-1wxaaza")
        lokalizacja=i.find_element(By.CLASS_NAME,"css-1mwdrlh").text

        cena=''.join(filter(str.isdigit, cenastr.text))
        cena=float(cena)
        nazwa=re.findall(pattern, nazwastr.text, re.IGNORECASE)
        nazwacala=""
        index=nazwastr.text.lower().find("gb")
        pamiec= "" if index==-1 else nazwastr.text[index-3:index].replace(" ","")

        try:
            nazwacala = f"iphone {'x' if nazwa[0][0] == 10 else nazwa[0][0]} {nazwa[0][1]} {nazwa[0][2]} {nazwa[0][3]}"
            telefony.append({
                "nazwa": nazwacala.lower().replace(" ",""),
                "cena": cena,
                "pamiec": pamiec,
                "lokalizacja": lokalizacja,
                "link": link

            })


        except:
            nazwacala=nazwastr.text
            print(f"zła nazwa nie przeszła regex{nazwacala}, {cena}, {link}")

    return telefony




