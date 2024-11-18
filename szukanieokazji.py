


okazyjneceny = {
    "iphonex": 450,
    "iphonexs": 400,
    "iphonexr": 400,
    "iphonexsmax": 600,
    "iphone11": 600,
    "iphone11pro": 700,
    "iphone12mini": 700,
    "iphone12": 900,
    "iphone12pro": 1100,
    "iphone12promax": 1400,
    "iphone13mini": 1200,
    "iphone13": 1400,
    "iphone13pro": 1700,
    "iphone13promax": 2200,
    "iphone14": 1700,
    "iphone14pro": 2400,
    "iphone14promax": 2800,
    "iphone14plus": 2100,
    "iphone15": 2600,
    "iphone15pro": 3500,
    "iphone15promax": 4000,
    "iphone15plus": 3000,

}


def okazje(telefony):
    dobreceny = []

    for i in telefony:
        try:
            if okazyjneceny[i["nazwa"]] > i["cena"]:
                dobreceny.append(i)
        except:
            pass
            #print(f"cos nie tak {i}")

    return dobreceny

