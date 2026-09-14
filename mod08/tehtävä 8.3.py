lentokentät=[
    {"ICAO-koodi":"EFHK", "lentoasema":"Helsinki-Vantaan lentoasema (Vantaa)" },
    {"ICAO-koodi":"EFOU", "lentoasema":"Oulun lentoasema (Oulu)" },
    {"ICAO-koodi":"EFPO", "lentoasema":"Porin lentoasema (Pori)" },
    {"ICAO-koodi":"EFVA", "lentoasema":"Vaasan lentoasema (Vaasa)" },
    {"ICAO-koodi":"EFTU", "lentoasema":"Turun lentoasema (Turku)" }
]
while True:
    syöte=input("Syötä uusi lentoasema (1), hae lentoasemia (2) ja lopeta (3). Syötä komentoa vastaava numero:\n")
    if syöte=="1":
        koodi=input("Syötä lentoaseman ICAO-koodi:\n")
        uusiasema=input("Syötä vastaavan lentoaseman nimi:\n")
        uusi={"ICAO-koodi":koodi, "lentoasema":uusiasema}
        lentokentät.append(uusi)
    elif syöte=="2":
        haku=input("Syötä lentoasemaa vastaava ICAO-koodi:\n")
        for item in lentokentät:
            if item["ICAO-koodi"] == haku:
                print(f"ICAO-koodia {haku} vastaava lentoasema on {item['lentoasema']}.\n")
                break
    elif syöte=="3":
        print("Kiitos ohjelman käytöstä, näkemiin!")
        break