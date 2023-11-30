#Dictionnaire des prix des différentes énergies
energie_Prix={"électricité":0.20,"gaz":0.15,"fioul":0.10,"bois buche":0.05, "bois briquettes": 0.12, "bois granulés": 0.12, "bois plaquettes":0.03}
#consommation d'énergie par mètres carrés par an (kWh/m^2/an) pour le chauffage par rapport au niveau d'isolation
niveau_isolation={"faible":110, "moyen":100,"bon":90}
#différent rendement par rapport aux différents chauffages 
rendement={"gaz":0.60, "bois":0.7,"électrique":0.78, "chaudières fioul standart":0.8, "chaudières fioul condensation":0.95}
def par_consommation():
    print("coucou")


def consommation(energie, facture):
    conso=facture/energie_Prix[energie]
    return conso

#fonction pour calculer la consommation d'énergie par rapport à la facture
def par_prix_payé():
    facture = int(input("Entrez votre facture d'énergie pour l'année (en €): \n-> "))
    energie="null"
    while energie!="électricité" and energie!="gaz" and energie!="fioul" and energie!="bois":
        energie = input("Entrez l'énergie que vous utilisez dans votre maison pour vous chauffer [ électricité / gaz / fioul / bois ]: \n-> ")
    if energie == "bois" :
        while energie != "bois buche" and energie != "bois granulés" and energie != "bois briquettes" and energie != "bois plaquettes":
            energie = "bois " + input("Entrez quel type de bois que vous utilisez pour vous chauffer [ buche / granulés / briquettes / plaquettes ] : \n-> ")
    conso = consommation(energie,facture)
    conso = round(conso)
    return conso


def par_superficie():
    superficie_foyer=int(input("Entrez la superficie de votre maison : \n-> "))
    isolation_foyer="null"
    while isolation_foyer != "faible" and isolation_foyer!="moyen" and isolation_foyer!="bon":
        isolation_foyer=input("Entrez le niveau d'isolation de votre maison [ faible / moyen / bon ] \n-> ")
    if isolation_foyer == "faible":
        energie_surface=superficie_foyer*niveau_isolation["faible"]
    elif isolation_foyer == "moyen":
        energie_surface=superficie_foyer*niveau_isolation["moyen"]
    elif isolation_foyer == "bon":
        energie_surface=superficie_foyer*niveau_isolation["bon"]
    #ajout de la consomation autre que le chauffage (moyenne en kWh)
    energie_surface+=2421
    return energie_surface

print("Il y a trois manières pour calculer votre consommation d'énergie : \n[1] - Calcul par votre consommation d'énergie pour votre foyer\n[2] - Calcul par le montant de votre facture et du type d'énergie utilisé\n[3] - Calcul par la superficie de votre maison")
choix=0
while choix != 1 and choix != 2 and choix!=3:
    choix=int(input("Par quelle façon voulez vous calculer ? [ 1 / 2 / 3 ]\n-> "))
if choix == 1:
    print(par_consommation(),"\n")
elif choix == 2:
    print(par_prix_payé(),"\n")
elif choix == 3:
    print(par_superficie(),"\n")