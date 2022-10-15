ljudfiler = ["a","b","c","d","e","f","g"]
historik = []



def runda(toner, svagast_vinner):
    """Funktionen tar in en lista över toner och låter användaren parvis
    jämföra vilken ton som är starkast. Den gör detta rekurvivt.

    EXEMPEL
    Låt toner vara ["a","b","c","d","e","f","g"]. Ponera att användaren väljer
    "a" över "b", "d" över "c", "e" över "f". Sedan kör den funktionen igen
    rekursivt, då toner är ["a","d","e","g"]. Ponera att användaren väljer
    "a" över "d", "g" över "e". Sedan kör den funktionen igen rekursivt, då
    toner är ["a","g"]. Ponera att användaren väljer "a" över "g". Då
    returnerar funktionen "a".
    """

    starka_toner = []

    for ton_1, ton_2 in zip(toner[::2], toner[1::2]):
        print("\nLjud som spelas :", ton_1, ton_2)
        # Spela ljud_1 och ljud_2
        
        svar = None
        while svar not in ("1", "2"):
            svar = input("Vilket ljud är tydligast (1 eller 2) ? ")

        if svar == "1":
            tonpar = (ton_1, ton_2)  # stark ton före svag ton
        else:
            tonpar = (ton_2, ton_1)
        starka_toner.append(tonpar[svagast_vinner])
        historik.append(tonpar)

    # Lägger till sista tonen OM listan över toner är udda
    # så den också kan jämföras.
    if len(toner)%2:
        starka_toner.append(toner[-1])

    # Startar igång ytterligare en runda om det finns kvar
    # toner att jämföra.
    if len(starka_toner) == 1:
        return starka_toner[0]
    else:
        return runda(starka_toner, svagast_vinner=svagast_vinner)



den_högsta_tonen = runda(ljudfiler, svagast_vinner=False)
print("", f"Kandidater : {ljudfiler}", f"Vinnare : {den_högsta_tonen}", sep="\n")

kandidater = [ton_2 for ton_1, ton_2 in historik if ton_1 == den_högsta_tonen]
den_näst_högsta_tonen = runda(kandidater, svagast_vinner=False)
print("", f"Kandidater : {kandidater}", f"Vinnare : {den_näst_högsta_tonen}", sep="\n")

# höga_toner: Mängden av toner som i en jämförelse varit starkare än en annan
höga_toner = set(ton_1 for ton_1, _ in historik)
kandidater = list(set(ljudfiler)-höga_toner)
den_lägsta_tonen = runda(kandidater, svagast_vinner=True)
print("", f"Kandidater : {kandidater}", f"Vinnare : {den_lägsta_tonen}", sep="\n")

kandidater = [ton_1 for ton_1, ton_2 in historik if
    ton_2 == den_lägsta_tonen
    and ton_1 in kandidater
]
den_näst_lägsta_tonen = runda(kandidater, svagast_vinner=True)
print("", f"Kandidater : {kandidater}", f"Vinnare : {den_näst_lägsta_tonen}", sep="\n")

print("Skriv ned följande:", den_högsta_tonen, den_näst_högsta_tonen, den_näst_lägsta_tonen, den_lägsta_tonen, "och lämna in.")