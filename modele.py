def etiquettte_foyer():
    energie=130
    niveau=["A","B","C","D","E","F","G"]
    if energie<=50:
        classement="A"
    elif energie>=51 and energie<=90:
        classement="B"
    elif energie>=91 and energie<=150:
        classement="C"
    elif energie>=151 and energie<=230:
        classement="D"
    elif energie>=231 and energie<=330:
        classement="E"
    elif energie>=331 and energie<=450:
        classement="F"
    else:
        classement="G"
    for i in range(len(niveau)):
        print(niveau[i], end=" ")
        for j in range(i):
            print("-",end="")
        print(">", end="")
        for j in range((len(niveau)+2)-i):
            print(" ",end="")
        if classement == niveau[i]:
            print(f"< {energie} kWh/an/m2")
        else:
            print("")
