#Dictionnaire des prix des différentes énergies en €
energie_Prix={"électricité":0.20,"gaz":0.15,"fioul":0.10,"bois buche":0.05, "bois briquettes": 0.12, "bois granulés": 0.12, "bois plaquettes":0.03}
#Dictionnaire des conversions des différentes énergie en kWh
energie_eq_kwh={"électricité":1,"fioul": 10, "gaz naturel": 1, "gaz bouteille": 13, "bois buche": 1700, "bois granulés": 5000, "bois briquettes": 5000, "bois plaquettes":2500}
unité_energie={"électricité":"kWh","fioul": "Litre", "gaz naturel": "m3", "gaz bouteille": "kg", "bois buche": "stères ou m3", "bois granulés": "tonne", "bois briquettes": "tonne", "bois plaquettes":"tonne"}

#Dictionnaire consommation d'énergie par mètres carrés par an (kWh/m^2/an) pour le chauffage par rapport au niveau d'isolation
niveau_isolation={"faible":110, "moyen":100,"bon":90}

def par_consommation(superficie_foyer):
    energie="null"
    nbr_energie=int(input("\nCombien d'énergie différentes avez vous pour vous chauffer ? (nombre) :\n-> "))
    for i in range(nbr_energie):
        if i==0:
            while energie!="électricité" and energie!="gaz" and energie!="fioul" and energie!="bois":
                energie = input("\nEntrez la 1er énergie que vous utilisez dans votre maison pour vous chauffer [ électricité / gaz / fioul / bois ] : \n-> ")
        else:
            while energie!="électricité" and energie!="gaz" and energie!="fioul" and energie!="bois":
                energie = input(f"\nEntrez la {i+1}ème énergie que vous utilisez dans votre maison pour vous chauffer [ électricité / gaz / fioul / bois ] : \n-> ")
        if energie == "bois" :
            while energie != "bois buche" and energie != "bois granulés" and energie != "bois briquettes" and energie != "bois plaquettes":
                energie = "bois " + input("\nEntrez quel type de bois que vous utilisez pour vous chauffer [ buche / granulés / briquettes / plaquettes ] : \n-> ")
        elif energie == "gaz" :
            while energie != "gaz naturel" and energie != "gaz bouteille":
                energie = "gaz " + input("\nEntrez quel type de gaz que vous utilisez pour vous chauffer [ naturel / bouteille ] : \n-> ")
        if energie == "électricité":
            quantité_energie=int(input(f"Entrez combien  vous avez consommé d'électricité en kWh : \n-> "))
        else:
            quantité_energie=int(input(f"Entrez combien  vous avez consommé de {energie} en {unité_energie[energie]} : \n-> "))
        
        
#fonction pour calculer la consommation d'énergie par rapport à la facture sortie en kWh/m2/an
def par_prix_payé(superficie_foyer):
    energie="null"
    conso=0

    nbr_energie=int(input("\nCombien d'énergie différentes avez vous pour vous chauffer ? (nombre) :\n-> "))
    for i in range(nbr_energie):
        if i==0:
            while energie!="électricité" and energie!="gaz" and energie!="fioul" and energie!="bois":
                energie = input("\nEntrez la 1er énergie que vous utilisez dans votre maison pour vous chauffer [ électricité / gaz / fioul / bois ] : \n-> ")
        else:
            while energie!="électricité" and energie!="gaz" and energie!="fioul" and energie!="bois":
                energie = input(f"\nEntrez la {i+1}ème énergie que vous utilisez dans votre maison pour vous chauffer [ électricité / gaz / fioul / bois ] : \n-> ")
        facture = int(input(f"\nEntrez votre facture d'énergie pour l'année (en €) pour {energie}: \n-> "))
        if energie == "bois" :
            while energie != "bois buche" and energie != "bois granulés" and energie != "bois briquettes" and energie != "bois plaquettes":
                energie = "bois " + input("\nEntrez quel type de bois que vous utilisez pour vous chauffer [ buche / granulés / briquettes / plaquettes ] : \n-> ")
        
        conso += facture/energie_Prix[energie]
        energie="null"
    conso/=superficie_foyer
    conso = round(conso)
    return conso

#fonction pour la partie du calcul par la superficie
def par_superficie(superficie_foyer):
    #boucle pour être sur que la valeur rentré peut être traité par le programme
    isolation_foyer="null"
    while isolation_foyer != "faible" and isolation_foyer!="moyen" and isolation_foyer!="bon":
        isolation_foyer=input("Entrez le niveau d'isolation de votre maison [ faible / moyen / bon ] \n-> ")
    #appel de la fonction pour le calcul, sortie en kWh
    energie_surface=superficie_foyer*niveau_isolation[isolation_foyer]
    #ajout de la consommation autre que le chauffage (moyenne en kWh)
    energie_surface+=2421
    return energie_surface

print("Il y a trois manières pour calculer votre consommation d'énergie : \n[1] - Calcul par votre consommation d'énergie pour votre foyer\n[2] - Calcul par le montant de votre facture et du type d'énergie utilisé\n[3] - Calcul par la superficie de votre maison")
choix=0
while choix != 1 and choix != 2 and choix!=3:
    choix=int(input("\nPar quelle façon voulez vous calculer ? [ 1 / 2 / 3 ]\n-> "))
#demande de la superficie de la maison (en m2)
superficie_foyer=int(input("Entrez la superficie de votre maison : \n-> "))
if choix == 1:
    print(par_consommation(superficie_foyer),"\n")
elif choix == 2:
    print(par_prix_payé(superficie_foyer),"\n")
elif choix == 3:
    print(par_superficie(superficie_foyer),"\n")
    
