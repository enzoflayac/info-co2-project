#Dictionnaire des prix des différentes énergies en €
energie_Prix={"électricité":0.20,"gaz naturel":0.15,"gaz bouteille":0.15,"fioul":0.10,"bois buche":0.05, "bois briquettes": 0.12, "bois granulés": 0.12, "bois plaquettes":0.03}
#Dictionnaire des conversions des différentes énergie en kWh
energie_eq_kwh={"électricité":1,"fioul": 10, "gaz naturel": 11, "gaz bouteille": 13, "bois buche": 1700, "bois granulés": 5000, "bois briquettes": 5000, "bois plaquettes":2500}
energie_eq_co2={"électricité":0.08,"fioul": 0.32, "gaz naturel": 0.23, "gaz bouteille": 0.27, "bois buche": 0.03,"bois granulés": 0.03,"bois briquettes": 0.03,"bois plaquettes": 0.03}
unité_energie={"électricité":"kWh","fioul": "Litre", "gaz naturel": "m3", "gaz bouteille": "kg", "bois buche": "stères ou m3", "bois granulés": "tonne", "bois briquettes": "tonne", "bois plaquettes":"tonne"}
impact_carbone_par_transport={"bus": 30, "train thermique":30, "train électrique":3, "trolleybus":3, "métro": 3, "tramway": 3, "avion": 250}


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
    fonction="null"
    total=0
    while autre_energie_ou_pas!="oui" and autre_energie_ou_pas!="non":
        autre_energie_ou_pas=input("\nChauffez vous avec une autre énergie que l'électricité ? [ oui / non ] : \n-> ")
    if autre_energie_ou_pas == "oui":
        nbr_energie=int(input("\nCombien d'énergie différentes avez vous pour vous chauffez hormis l'électricité ? (nombre) :\n-> "))
        for i in range(nbr_energie+1):
            if i==0:
                fonction=input(f"\nQuelles informations avez vous sur l'électricité consommé, facture en kWh ou en euros € ? [ 1 = kWh / 2 = € ]\n-> ")
                if fonction == "1":
                    total+=par_consommation(energie)
                elif fonction == "2":
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
                        
                while fonction != "1" and fonction != "2":
                    fonction=input(f"\nQuelles informations avez vous sur le {energie} consommé, facture en {unité_energie[energie]} ou en euros € ? [ 1 = {unité_energie[energie]}] / 2 = € ]\n-> ") 
                if fonction == "1":
                    par_consommation(energie)
                elif fonction == "2":
                    total+=par_prix_payé(energie)
            fonction="null"
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
    kilomètres=int(input("\nCombien vous faites de km avec votre voiture par an ? \n-> "))
    conso=int(input(f"\nCombien votre véhicule consomme au 100km ? ({unité_energie[type_voiture]}/100km) :\n-> "))
    #conversion consommation du 100km au km
    conso/=100
    conso*=kilomètres
    if type_voiture=="fioul":
        conso*=10
    impact_transport+=conso*energie_eq_co2[type_voiture]  
    impact_transport=round(impact_transport)
    return conso
    

def voiture():
    total=0
    type_voiture="null"
    nbr_voiture=int(input("\nCombien avez vous de véhicules ? (nombre): \n-> "))
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
    
def calcul_transport_commun(type_transport_commun):
    global impact_transport
    kilomètres=int(input(f"\nCombien faites vous de km en {type_transport_commun} par an ? \n-> "))
    impact_transport+=kilomètres*impact_carbone_par_transport[type_transport_commun]
    

def transport_commun(transport_commun_ou_non):
    type_transport_commun="null"
    while transport_commun_ou_non == "oui":
        while type_transport_commun != "bus" and type_transport_commun != "train" and type_transport_commun != "trolleybus" and type_transport_commun!= "métro"and type_transport_commun!="tramway" and type_transport_commun!="avion":
            type_transport_commun=input("Entrez quel type de transport en commun vous utilisez [ bus / train / trolleybus / tramway / métro / avion ]: \n-> ")
        if type_transport_commun == "train":
            while type_transport_commun != "train thermique" and type_transport_commun != "train électrique":
                type_transport_commun+=" "+input("\nEntrez quel type de train vous utilisez [ thermique / électrique ]: \n-> ")
        #appel de la fonction pour calculer l'impact carbone du transport renseigné auparavant
        calcul_transport_commun(type_transport_commun)
        #remise à zéro de la variable pour poser la question s'il y a un autre transport en commun
        transport_commun_ou_non="null"
        #question s'il y a un autre transport en commun
        while transport_commun_ou_non!="non" and transport_commun_ou_non!="oui":
            transport_commun_ou_non=input("\nPrenez vous un autre transport en commun ? [ oui / non ]: \n-> ")
        
    
def transport():
    voiture_ou_non=transport_commun_ou_non="null"
    while voiture_ou_non!="non" and voiture_ou_non!="oui":
        voiture_ou_non=input("\nAvez vous une voiture ? [ oui / non ]: \n-> ")
    if voiture_ou_non =="oui":
        conso_voiture=voiture()
    else:
        conso_voiture=0
    while transport_commun_ou_non!="non" and transport_commun_ou_non!="oui":
        transport_commun_ou_non=input("\nPrenez vous les transports en commun ? [ oui / non ]: \n-> ")
    if transport_commun_ou_non == "oui":
        transport_commun(transport_commun_ou_non)
    
    return conso_voiture

def etiquettte_energie_foyer(conso_energetique_foyer,conso_energetique_foyer_m2):
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
            
def etiquettte_impact_foyer(impact_foyer,superficie_foyer):
    print(f"total du foyer : {impact_foyer} kgeqCO2/an")
    niveau=["A","B","C","D","E","F","G"]
    impact_foyer_m2=impact_foyer/superficie_foyer
    if impact_foyer_m2<=5:
        classement="A"
    elif impact_foyer_m2>=6 and impact_foyer_m2<=10:
        classement="B"
    elif impact_foyer_m2>=11 and impact_foyer_m2<=20:
        classement="C"
    elif impact_foyer_m2>=21 and impact_foyer_m2<=35:
        classement="D"
    elif impact_foyer_m2>=36 and impact_foyer_m2<=55:
        classement="E"
    elif impact_foyer_m2>=56 and impact_foyer_m2<=80:
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
            print(f"< {impact_foyer_m2} kgeqCO2/an/m2")
        else:
            print("")
            
            
def comparaison(habitat, transport):
    total=habitat+transport
    #calcul du pourcentage de l'habitat et arrondissement à la dizaine puis arrondissement à l'entier pour avoir un integer
    pourcentage_habitat=round(round(habitat*100/total, -1))
    nbr_etoiles_habitat=round(pourcentage_habitat/10)
    #calcul du pourcentage du transport et arrondissement à la dizaine puis arrondissement à l'entier pour avoir un integer
    pourcentage_transport=round(round(transport*100/total, -1))
    nbr_etoiles_transport=round(pourcentage_transport/10)
    for i in range(nbr_etoiles_habitat*2):
        print("*",end="")
    print(f" {pourcentage_habitat}% habitat")
    for i in range(nbr_etoiles_transport*2):
        print("*",end="")
    print(f" {pourcentage_transport}% transport")
#demande de la superficie de la maison (en m2)
superficie_foyer=int(input("\nEntrez la superficie de votre maison : \n-> "))
impact_foyer=impact_transport=0
conso_energetique_foyer=calcul_energie_foyer()
conso_voiture=transport()

etiquettte_energie_foyer(conso_energetique_foyer,superficie_foyer)
etiquettte_impact_foyer(impact_foyer, superficie_foyer)
comparaison(impact_foyer,impact_transport)

print("impact transport", impact_transport, "kgeqCO2/m2/an")
print("consommation voiture", conso_voiture, "kWh/an")