#Dictionnaire des prix des différentes énergies
energie_Prix={"électricité":0.20,"gaz":0.15,"fioul":0.10,"bois buche":0.05, "bois granulés/briquettes": 0.12, "bois plaquettes":0.03}
#consommation d'énergie par mètres carrés par an (kWh/m^2/an) par rapport au niveau d'isolation
niveau_isolation={"faible":110, "moyen":100,"bon":90}
#différent rendement par rapport au différent chauffage 
rendement={"gaz":0.60, "bois":0.7,"électrique":0.78}
facture=53
energie="électricité"

#fonction pour calculer la consommation d'énergie par rapport à la facture
def prix_payé(facture,energie):
    if energie == "électricité":
        conso=facture/energie_Prix["électricité"]
    elif energie == "gaz":
        conso=facture/energie_Prix["gaz"]
    elif energie == "fioul":
        conso=facture/energie_Prix["fioul"]
    elif energie == "bois buche":
        conso=facture/energie_Prix["bois buche"]
    elif energie == "bois granulés":
        conso=facture/energie_Prix["bois granulés/briquettes"]
    elif energie == "bois briquettes":
        conso=facture/energie_Prix["bois granulés/briquettes"]
    elif energie == "bois plaquettes":
        conso=facture/energie_Prix["bois plaquettes"]
    return conso
def calcul_energie():
    superficie_foyer=int(input("Entrez la superficie de votre maison"))
    isolation_foyer="null"
    while isolation_foyer != ("faible" or "moyen" or "bon"):
        isolation_foyer=input("Entrez le niveau d'isolation de votre maison [ faible / moyen / bon ]: ")
    if isolation_foyer == "faible":
        energie_surface=superficie_foyer*niveau_isolation["faible"]
    elif isolation_foyer == "moyen":
        energie_surface=superficie_foyer*niveau_isolation["moyen"]
    elif isolation_foyer == "bon":
        energie_surface=superficie_foyer*niveau_isolation["bon"]
    return energie_surface
    
print(calcul_energie())