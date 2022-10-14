ljudfiler=["a","b","c","d","e","f","g"]
högst_ljud = []
lägst_ljud = []
jämförda_par = []


def sortera(ljud_1, ljud_2, svar):
    fel = 0
    if svar == "1":
        högst_ljud.append(ljud_1)
        lägst_ljud.append(ljud_2)
    elif svar == "2":
        högst_ljud.append(ljud_2)
        lägst_ljud.append(ljud_1)
    else:
        fel = 1
    return (fel)


def listgenomgång(ljudlista):
    i = 0
    while True:
        print("")
        if i == len(ljudlista) // 2:
            break
        nytt_par = 0
        ljud_1 = ljudlista[2 * i]
        ljud_2 = ljudlista[2 * i + 1]
        print("ljud som spelas:", ljud_1, ljud_2)
        #Spela ljud_1 och ljud_2
        svar = str(input("vilket ljud är tydligast (1 eller 2)?"))
        fel = sortera(ljud_1, ljud_2, svar)
        if fel == 0:
            i += 1
            jämförda_par.append((ljud_1, ljud_2))



#ger högsta
for i in range(3):
    if i == 1:
        lägst_ljud1 = lägst_ljud  #sparar de lägsta ljuden till senare
    högst_ljud = []
    lägst_ljud = []
    listgenomgång(ljudfiler)
    ljudfiler = högst_ljud
    print("ljudfiler:", ljudfiler)
print("sparade lägst ljud:", lägst_ljud1)
ljud1 = ljudfiler[0]
print("ljud1: ", ljud1)  #högsta ljudet
ljudfiler = []

#skapar ljudlistan för potentiella ljud2
for i in jämförda_par:
    if i[0] == ljud1:
        ljudfiler.append(i[1])
    elif i[1] == ljud1:
        ljudfiler.append(i[0])

#hittar ljud2
print("ljudfiler:", ljudfiler)
while len(ljudfiler) > 1:
    högst_ljud = []
    lägst_ljud = []
    listgenomgång(ljudfiler)
    ljudfiler.remove(lägst_ljud[0])
    print("ljudfiler:", ljudfiler)

#skapar lista för potentiellt lägsta ljud
ljud2 = ljudfiler[0]
print("ljud2: ", ljud2)
ljudfiler = lägst_ljud1
print("ljudfiler: ", ljudfiler)
for i in ljudfiler:
    if i == ljud1 or i == ljud2:
        ljudfiler.remove(i)

#hittar lägsta ljud
for i in range(2):
    högst_ljud = []
    lägst_ljud = []
    listgenomgång(ljudfiler)
    ljudfiler = lägst_ljud
    print("ljudfiler:", ljudfiler)

ljud8 = ljudfiler[0]
print("ljud8: ", ljud8)  #lägsta ljudet
ljudfiler = []

#skapar lista med potentiellt näst lägsta ljud
for i in jämförda_par:
    if i[0] == ljud8 and i[1] != ljud1 and i[1] != ljud2:
        ljudfiler.append(i[1])
    elif i[1] == ljud8 and i[0] != ljud1 and i[0] != ljud2:
        ljudfiler.append(i[0])
#hittar näst lägsta ljud
while len(ljudfiler) > 1:
    högst_ljud = []
    lägst_ljud = []
    listgenomgång(ljudfiler)
    ljudfiler.remove(högst_ljud[0])
    print("ljudfiler:", ljudfiler)
ljud7 = ljudfiler[0]

print("Skriv ned följande: ", ljud1, ljud2, ljud7, ljud8, " och lämna in.")
