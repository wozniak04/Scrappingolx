sciezka="./linki.txt"


def sprawdzlink(link):
    #sprawdzanie czy dany link jest juz w pliku linki.txt
    with open(sciezka, "r", encoding="utf-8") as plik:
        zawartosc = plik.read()

    if link in zawartosc:
        return 1
    else:
        return 0

def dodawanielinku(link):
    #zapisywanie znalezionych ofert
    with open(sciezka, "a", encoding="utf-8") as plik:
        plik.write(link+"\n")
    return 0