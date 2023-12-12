#Dictionnaire des prix des différentes énergies en €
energie_Prix={"électricité":0.20,"gaz naturel":0.15,"gaz bouteille":0.15,"fioul":0.10,"bois buche":0.05, "bois briquettes": 0.12, "bois granulés": 0.12, "bois plaquettes":0.03}
#Dictionnaire des conversions des différentes énergie en kWh
energie_eq_kwh={"électricité":1,"fioul": 10, "gaz naturel": 11, "gaz bouteille": 13, "bois buche": 1700, "bois granulés": 5000, "bois briquettes": 5000, "bois plaquettes":2500}
energie_eq_co2={"électricité":0.08,"fioul": 0.32, "gaz naturel": 0.23, "gaz bouteille": 0.27, "bois buche": 0.03,"bois granulés": 0.03,"bois briquettes": 0.03,"bois plaquettes": 0.03}
unité_energie={"électricité":"kWh","fioul": "Litre", "gaz naturel": "m3", "gaz bouteille": "kg", "bois buche": "stères ou m3", "bois granulés": "tonne", "bois briquettes": "tonne", "bois plaquettes":"tonne"}

def par_consommation(energie):
    global impact_foyer
    if energie == "électricité":
            quantité_energie=int(input(f"\nEntrez combien  vous avez consommé d'électricité en kWh : \n-> "))
    else:
            quantité_energie=int(input(f"\nEntrez combien  vous avez consommé de {energie} en {unité_energie[energie]} : \n-> "))
    conso=quantité_energie*energie_eq_kwh[energie]
    impact_foyer += conso*energie_eq_co2[energie]
    impact_foyer = round(impact_foyer)
    conso = round(conso)
    energie="null"
    return conso
        
        
#fonction pour calculer la consommation d'énergie par rapport à la facture sortie en kWh/m2/an
def par_prix_payé(energie):
    conso=0
    global impact_foyer
    if energie == "électricité":
        facture=int(input("\nEntrez votre facture d'électricité en € : \n-> "))
    else:
        facture=int(input(f"\nEntrez votre facture de {energie} en € : \n-> "))
    
    conso += facture/energie_Prix[energie]
    impact_foyer += conso*energie_eq_co2[energie]
    
    conso = round(conso)
    impact_foyer = round(impact_foyer)
    energie="null"
    return conso

def calcul_energie_foyer():
    energie=autre_energie_ou_pas="électricité"
    total=fonction=0
    while autre_energie_ou_pas!="oui" and autre_energie_ou_pas!="non":
        autre_energie_ou_pas=input("\nChauffez vous avec une autre énergie que l'électricité ? [ oui / non ] : \n-> ")
    if autre_energie_ou_pas == "oui":
        nbr_energie=int(input("\nCombien d'énergie différentes avez vous pour votre foyer ? (nombre) :\n-> "))
        for i in range(nbr_energie):
            if i==0:
                fonction=int(input(f"\nQuelles informations avez vous sur l'électricité consommé, facture en kWh ou en euros € ? [ 1 = kWh / 2 = € ]\n-> "))   
                if fonction == 1:
                    total+=par_consommation(energie)
                elif fonction == 2:
                    total+=par_prix_payé(energie)
                
            else:
                while energie!="gaz" and energie!="fioul" and energie!="bois":
                    energie = input(f"\nEntrez la {i+1}ème énergie que vous utilisez dans votre maison pour vous chauffer [ gaz / fioul / bois ] : \n-> ")
                    
                if energie == "bois" :
                    while energie != "bois buche" and energie != "bois granulés" and energie != "bois briquettes" and energie != "bois plaquettes":
                        energie = "bois " + input("\nEntrez quel type de bois que vous utilisez pour vous chauffer [ buche / granulés / briquettes / plaquettes ] : \n-> ")
                elif energie == "gaz" :
                    while energie != "gaz naturel" and energie != "gaz bouteille":
                        energie = "gaz " + input("\nEntrez quel type de gaz que vous utilisez pour vous chauffer [ naturel / bouteille ] : \n-> ")
                        
                while fonction != 1 and fonction != 2:
                    fonction=int(input(f"\nQuelles informations avez vous sur le {energie} consommé, facture en {unité_energie[energie]} ou en euros € ? [ 1 = {unité_energie[energie]}] / 2 = € ]\n-> "))  
                if fonction == 1:
                    par_consommation(energie)
                elif fonction == 2:
                    total+=par_prix_payé(energie)
            fonction=0
    else :
        fonction=int(input(f"\nQuelles informations avez vous sur l'électricité consommé, facture en kWh ou en euros € ? [ 1 = kWh / 2 = € ]\n-> "))  
        if fonction == 1:
            total+=par_consommation(energie)
        elif fonction == 2:
            total+=par_prix_payé(energie)
            
    return total
    
def calcul_voiture(type_voiture):
    global impact_transport
    if type_voiture=="électrique":
        type_voiture="électricité"
    else:
        type_voiture="fioul"
    kilomètres=int(input("\nCombien vous faites de km avec votre voiture par an ? :\n->"))
    conso=int(input(f"\nCombien votre véhicule consomme au 100km ? ({unité_energie[type_voiture]}/100km) :\n->"))
    #conversion consommation du 100km au km
    conso/=100
    conso*=kilomètres
    if type_voiture=="fioul":
        conso*=10
    impact_transport+=conso*energie_eq_co2[type_voiture]  
    impact_transport=round(impact_transport)
    return conso
    
    
def transport():
    total=0
    type_voiture="null"
    nbr_voiture=int(input("Combien avez vous de véhicules ? (nombre): \n-> "))
    if nbr_voiture>1:
        for i in range(nbr_voiture):
            if i==0:
                while type_voiture!="thermique" and type_voiture!="électrique":
                    type_voiture=input("\nEntrez quel type de motorisation avez vous pour le 1er véhicule ? [ thermique / électrique ]: \n-> ")
                total+=calcul_voiture(type_voiture)
                type_voiture="null"
            else:
                while type_voiture!="thermique" and type_voiture!="électrique":
                    type_voiture=input(f"\nEntrez quel type de motorisation avez vous pour le {i+1}ème véhicule ? [ thermique / électrique ]: \n-> ")
                total+=calcul_voiture(type_voiture)
                type_voiture="null"
    elif nbr_voiture==1:
        while type_voiture!="thermique" and type_voiture!="électrique":
                    type_voiture=input("\nEntrez quel type de motorisation avez vous votre véhicule ? [ thermique / électrique ]: \n-> ")
        total+=calcul_voiture(type_voiture)
    else:
        pass
    total=round(total)
    return total
    
def etiquettte_foyer(conso_energetique_foyer,conso_energetique_foyer_m2):
    print(f"total du foyer : {conso_energetique_foyer} kWh/an")
    niveau=["A","B","C","D","E","F","G"]
    if conso_energetique_foyer_m2<=50:
        classement="A"
    elif conso_energetique_foyer_m2>=51 and conso_energetique_foyer_m2<=90:
        classement="B"
    elif conso_energetique_foyer_m2>=91 and conso_energetique_foyer_m2<=150:
        classement="C"
    elif conso_energetique_foyer_m2>=151 and conso_energetique_foyer_m2<=230:
        classement="D"
    elif conso_energetique_foyer_m2>=231 and conso_energetique_foyer_m2<=330:
        classement="E"
    elif conso_energetique_foyer_m2>=331 and conso_energetique_foyer_m2<=450:
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
            print(f"< {conso_energetique_foyer_m2} kWh/an/m2")
        else:
            print("")
#demande de la superficie de la maison (en m2)
superficie_foyer=int(input("\nEntrez la superficie de votre maison : \n-> "))
impact_foyer=impact_transport=0
#conso_energetique_foyer=calcul_energie_foyer()
#conso_energetique_foyer_m2=conso_energetique_foyer/superficie_foyer
conso_voiture=transport()
#print(conso_energetique_foyer, "kWh/an")
#print(conso_energetique_foyer_m2, "kWh/m2/an")
#etiquettte_foyer(conso_energetique_foyer,conso_energetique_foyer_m2)

print(impact_transport, "kgeqCO2/m2/an")
print(conso_voiture, "kWh/an")



