#Dictionnaire des prix des différentes énergies en €
energie_Prix={"électricité":0.20,"gaz naturel":0.15,"gaz bouteille":0.15,"fioul":0.10,"bois buche":0.05, "bois briquettes": 0.12, "bois granulés": 0.12, "bois plaquettes":0.03}
#Dictionnaire des conversions des différentes énergie en kWh
energie_eq_kwh={"électricité":1,"fioul": 10, "gaz naturel": 11, "gaz bouteille": 13, "bois buche": 1700, "bois granulés": 5000, "bois briquettes": 5000, "bois plaquettes":2500}
energie_eq_co2={"électricité":0.08,"fioul": 0.32, "gaz naturel": 0.23, "gaz bouteille": 0.27, "bois buche": 0.03,"bois granulés": 0.03,"bois briquettes": 0.03,"bois plaquettes": 0.03}
unité_energie={"électricité":"kWh","fioul": "Litre", "gaz naturel": "m3", "gaz bouteille": "kg", "bois buche": "stères ou m3", "bois granulés": "tonne", "bois briquettes": "tonne", "bois plaquettes":"tonne"}

def par_consommation(superficie_foyer, energie):
    global impact
    if energie == "électricité":
            quantité_energie=int(input(f"\nEntrez combien  vous avez consommé d'électricité en kWh : \n-> "))
    else:
            quantité_energie=int(input(f"\nEntrez combien  vous avez consommé de {energie} en {unité_energie[energie]} : \n-> "))
    conso=quantité_energie*energie_eq_kwh[energie]
    impact += conso*energie_eq_co2[energie]
    conso/=superficie_foyer
    impact = round(impact)
    conso = round(conso)
    energie="null"
    return conso
        
        
#fonction pour calculer la consommation d'énergie par rapport à la facture sortie en kWh/m2/an
def par_prix_payé(superficie_foyer, energie):
    conso=0
    global impact
    if energie == "électricité":
        facture=int(input("\nEntrez votre facture d'électricité en € : \n-> "))
    else:
        facture=int(input(f"\nEntrez votre facture de {energie} en € : \n-> "))
    
    conso += facture/energie_Prix[energie]
    impact += conso*energie_eq_co2[energie]
    conso/=superficie_foyer
    
    conso = round(conso)
    impact = round(impact)
    energie="null"
    return conso

def calcul_energie_foyer(superficie_foyer):
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
                    total+=par_consommation(superficie_foyer, energie)
                elif fonction == 2:
                    total+=par_prix_payé(superficie_foyer, energie)
                
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
                    par_consommation(superficie_foyer, energie)
                elif fonction == 2:
                    total+=par_prix_payé(superficie_foyer, energie)
            fonction=0
    else :
        fonction=int(input(f"\nQuelles informations avez vous sur l'électricité consommé, facture en kWh ou en euros € ? [ 1 = kWh / 2 = € ]\n-> "))  
        if fonction == 1:
            total+=par_consommation(superficie_foyer, energie)
        elif fonction == 2:
            total+=par_prix_payé(superficie_foyer, energie)
            
    return total
    

#demande de la superficie de la maison (en m2)
superficie_foyer=int(input("\nEntrez la superficie de votre maison : \n-> "))
impact=0
conso_energetique_foyer=calcul_energie_foyer(superficie_foyer)
print(impact, "kgeqCO2/m2/an")
print(conso_energetique_foyer, "kWh/m2/an")
    

    
