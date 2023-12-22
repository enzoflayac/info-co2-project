"""
Code python écrit par Enzo FLAYAC en TP3

Programme en Python qui, à partir d’un certain nombre de questions posées, permet d’établir un bilan énergétique et un impact carbone d’un foyer et d’un individu.

Les questions avec des choix sont dans une boucle while pour permettre la véracité des informations et la bonne continuité du programme.

Correction de la conversion du gaz naturel en kWh, noté 1kWh sur la feuille d'information, rectifié à 10kWh.
"""


#Dictionnaire des prix des différentes énergies en €
energie_Prix={"électricité":0.20,"gaz naturel":0.15,"gaz bouteille":0.15,"fioul":0.10,"bois buche":0.05, "bois briquettes": 0.12, "bois granulés": 0.12, "bois plaquettes":0.03}
#Dictionnaire des conversions des différentes énergies en kWh
energie_eq_kwh={"électricité":1,"fioul": 10, "gaz naturel": 10, "gaz bouteille": 13, "bois buche": 1700, "bois granulés": 5000, "bois briquettes": 5000, "bois plaquettes":2500}
# Dictionnaire des conversions des différentes énergies en kgeqco2
energie_eq_co2={"électricité":0.08,"fioul": 0.32, "gaz naturel": 0.23, "gaz bouteille": 0.27, "bois buche": 0.03,"bois granulés": 0.03,"bois briquettes": 0.03,"bois plaquettes": 0.03}
# Dictionnaire des unités des différentes énergies
unité_energie={"électricité":"kWh","fioul": "Litre", "gaz naturel": "m3", "gaz bouteille": "kg", "bois buche": "stères ou m3", "bois granulés": "tonne", "bois briquettes": "tonne", "bois plaquettes":"tonne"}
# Dictionnaire des impacts des différents transports
impact_carbone_par_transport={"bus": 0.030, "train thermique":0.030, "train électrique":0.003, "trolleybus":0.003, "métro": 0.003, "tramway": 0.003, "avion": 0.25}
# Dictionnaire des moyennes d'impact de carbone
impact_carbone_moyenne={"Mondiale": 4080,"Française":4210,"Chinoise":7130,"Américaine":13560}
# Dictionnaire des moyennes de consommation d'énergie
conso_moyenne_hab={"Mondiale": 3265,"Française":7043,"Chinoise":5119,"Américaine":12744}

#fonction pour calculer la consommation d'énergie par rapport à la facture sortie en kWh/an
def par_prix_payé(energie):
    #déclaration variable conso pour faire une sortie de données de la fonction par la suite
    conso=0
    #import de la variable global impact_foyer 
    global impact_foyer
    #question pour rentrer  la facture d'énergie avec prise en charge du vocabulaire (d' ou de)
    if energie == "électricité":
        facture=int(input("\nEntrez votre facture d'électricité en € : \n-> "))
    else:
        facture=int(input(f"\nEntrez votre facture de {energie} en € : \n-> "))
    #calcul de la consommation total avec division de la facture par le prix de l'énergie correspondante dans le dictionnaire (voir ligne 2)
    conso += facture/energie_Prix[energie]
    #calcul de l'impact du total de l'énergie utilisé avec le dictionnaire correspondant à l'énergie (voir ligne 6)
    impact_foyer += conso*energie_eq_co2[energie]
    #arrondissement à l'entier avec round()
    conso = round(conso)
    impact_foyer = round(impact_foyer)
    #mise à zéro de la variable pour permettre de continuer la boucle de la fonction calcul_energie_foyer
    energie="null"
    return conso

#fonction pour calculer la consommation d'énergie par le choix des informations disponible (voir ligne 57), sortie de la valeur en kWh/an
def par_consommation(energie):
    #cf-l29
    global impact_foyer
    if energie == "électricité":
            quantité_energie=int(input(f"\nEntrez combien  vous avez consommé d'électricité en kWh : \n-> "))
    else:
            quantité_energie=int(input(f"\nEntrez combien  vous avez consommé de {energie} en {unité_energie[energie]} : \n-> "))
    #voir ligne 36
    conso=quantité_energie*energie_eq_kwh[energie]
    #voir ligne 38
    impact_foyer += conso*energie_eq_co2[energie]
    #voir ligne 40
    impact_foyer = round(impact_foyer)
    conso = round(conso)
    #voir ligne 43
    energie="null"
    return conso


#fonction pour calculer l'énergie total consommé par le foyer 
def calcul_energie_foyer():
    #déclaration de la variable par l'énergie classique ( électricité )
    energie=autre_energie_ou_pas="électricité"
    #voir ligne 43
    fonction="null"
    total=0
    while autre_energie_ou_pas!="oui" and autre_energie_ou_pas!="non":
        autre_energie_ou_pas=input("\nChauffez vous avec une autre énergie que l'électricité ? [ oui / non ] : \n-> ")
    
    if autre_energie_ou_pas == "oui": #condition s'il y a d'autres énergies ou non
        nbr_energie=int(input("\nCombien d'énergie différentes avez vous pour vous chauffez hormis l'électricité ? (nombre) :\n-> "))
        #boucle avec nombre d'itérations égal au nombre d'energie différentes
        for i in range(nbr_energie+1):
            if i==0:
                fonction=input(f"\nQuelles informations avez vous sur l'électricité consommé, facture en kWh ou en euros € ? [ 1 = kWh / 2 = € ]\n-> ")
                if fonction == "1":#condition pour savoir quelle fonction appeler en rapport avec la réponse précédente
                    total+=par_consommation(energie)
                elif fonction == "2":
                    total+=par_prix_payé(energie)
                
            else:
                while energie!="gaz" and energie!="fioul" and energie!="bois":
                    energie = input(f"\nEntrez la {i+1}ème énergie que vous utilisez dans votre maison pour vous chauffer [ gaz / fioul / bois ] : \n-> ")
                    
                if energie == "bois" :#condition pour determiner le type de bois 
                    while energie != "bois buche" and energie != "bois granulés" and energie != "bois briquettes" and energie != "bois plaquettes":
                        energie = "bois " + input("\nEntrez quel type de bois que vous utilisez pour vous chauffer [ buche / granulés / briquettes / plaquettes ] : \n-> ")
                elif energie == "gaz" :#condition pour déterminer le type de gaz
                    while energie != "gaz naturel" and energie != "gaz bouteille":
                        energie = "gaz " + input("\nEntrez quel type de gaz que vous utilisez pour vous chauffer [ naturel / bouteille ] : \n-> ")
                        
                while fonction != "1" and fonction != "2":#cf-l83
                    fonction=input(f"\nQuelles informations avez vous sur le {energie} consommé, facture en {unité_energie[energie]} ou en euros € ? [ 1 = {unité_energie[energie]}] / 2 = € ]\n-> ") 
                if fonction == "1":
                    total+=par_consommation(energie)
                elif fonction == "2":
                    total+=par_prix_payé(energie)
            #cf-l43
            fonction="null"
    else :
        while fonction != "1" and fonction != "2":#cf-l83
            fonction=input(f"\nQuelles informations avez vous sur l'électricité consommé, facture en kWh ou en euros € ? [ 1 = kWh / 2 = € ]\n-> ")
        if fonction == "1":
            total+=par_consommation(energie)
        elif fonction == "2":
            total+=par_prix_payé(energie)
    #retour du total de consommation du foyer
    return total
    
def calcul_voiture(type_voiture):#fonction pour calculer l'impact et la consommation du véhicule
    #cf-l29
    global impact_transport
    #condition pour transformer le type de motorisation en énergie 
    if type_voiture=="électrique":
        type_voiture="électricité"
    else:
        type_voiture="fioul"
    kilomètres=int(input("\nCombien vous faites de km avec votre voiture par an ? \n-> "))
    #question pour déterminer la consommation au 100 du véhicule
    conso=int(input(f"\nCombien votre véhicule consomme au 100km ? ({unité_energie[type_voiture]}/100km) :\n-> "))
    #conversion consommation du 100km au km
    conso/=100
    #calcul total de l'énergie
    conso*=kilomètres
    if type_voiture=="fioul":
        conso*=10#pour 1litre consommé c'est équivalent à 10kwh
    #calcul de l'impact par rapport à l'énergie utilisé 
    impact_transport+=conso*energie_eq_co2[type_voiture]  
    #arrondissement à l'entier avec round()
    impact_transport=round(impact_transport)
    return conso
    
#fonction pour déterminer le nombre de véhicule puis calculer pour chaque véhicule en appelant la fonction calcul_voiture()
def voiture():
    total=0
    #voir l43
    type_voiture="null"
    nbr_voiture=int(input("\nCombien avez vous de véhicules ? (nombre): \n-> "))
    if nbr_voiture>1:#condition pour orienter notre programme s'il y a pas de voiture, une seule ou plusieurs
        for i in range(nbr_voiture):#boucle s'il y a plusieurs véhicules
            if i==0:#condition pour la prise en compte du français avec 1er et Xème
                while type_voiture!="thermique" and type_voiture!="électrique":
                    type_voiture=input("\nQuel type de motorisation avez vous pour le 1er véhicule ? [ thermique / électrique ]: \n-> ")
                #ajout de la consommation au total en kWh 
                total+=calcul_voiture(type_voiture)
                type_voiture="null"#cf l43
            else:
                while type_voiture!="thermique" and type_voiture!="électrique":
                    type_voiture=input(f"\nQuel type de motorisation avez vous pour le {i+1}ème véhicule ? [ thermique / électrique ]: \n-> ")
                total+=calcul_voiture(type_voiture)#cf l151
                type_voiture="null"#cf l43
    elif nbr_voiture==1:
        while type_voiture!="thermique" and type_voiture!="électrique":
                    type_voiture=input("\nEntrez quel type de motorisation que vous avez dans votre véhicule [ thermique / électrique ]: \n-> ")
        total+=calcul_voiture(type_voiture)#cf l151
    else:
        pass#comme son nom l'indique, cela permet de passer cette condition si elle n'est pas remplie
    #cf l136
    total=round(total)
    return total
    
    
#fonction pour calculer l'impact carbone des transport en commun
def calcul_transport_commun(type_transport_commun):
    global impact_transport #cf l29
    kilomètres=int(input(f"\nCombien faites vous de km en {type_transport_commun} par an ? \n-> ")) #question pour déterminer le nombre de km effectué
    impact_transport+=kilomètres*impact_carbone_par_transport[type_transport_commun]#cf l36 calcul de l'impact de ce type de transport

def transport_commun(transport_commun_ou_non):#fonction pour déterminer les types de transports utilisé ou non
    type_transport_commun="null"
    #boucle pour le calcul d'émission co2 des transports en commun 
    while transport_commun_ou_non == "oui":
        while type_transport_commun != "bus" and type_transport_commun != "train" and type_transport_commun != "trolleybus" and type_transport_commun!= "métro"and type_transport_commun!="tramway" and type_transport_commun!="avion":
            type_transport_commun=input("\nEntrez quel type de transport en commun vous utilisez [ bus / train / trolleybus / tramway / métro / avion ]: \n-> ")
        if type_transport_commun == "train":
            #question pour savoir si c'est un train thermique ou électrique
            while type_transport_commun != "train thermique" and type_transport_commun != "train électrique":
                type_transport_commun+=" "+input("\nEntrez quel type de train vous utilisez [ thermique / électrique ]: \n-> ")
        #appel de la fonction pour calculer l'impact carbone du transport renseigné auparavant
        calcul_transport_commun(type_transport_commun)
        #remise à zéro de la variable pour poser la question s'il y a un autre transport en commun
        transport_commun_ou_non="null"
        #question s'il y a un autre transport en commun ou non
        while transport_commun_ou_non!="non" and transport_commun_ou_non!="oui":
            transport_commun_ou_non=input("\nPrenez vous un autre transport en commun ? [ oui / non ]: \n-> ")
            #remise à zéro de la variable type_transport_commun pour permettre de refaire la boucle s'il y a un autre type de transport envisagé
            type_transport_commun="null"
        
    
def transport():
    #mise à zéro des variables
    voiture_ou_non=transport_commun_ou_non="null"
    #questions avez vous une voiture
    while voiture_ou_non!="non" and voiture_ou_non!="oui":
        voiture_ou_non=input("\nAvez vous une voiture ? [ oui / non ]: \n-> ")
    if voiture_ou_non =="oui":#condition s'il a une voiture ou non
        conso_voiture=voiture()#appel de la fonction voiture() qui retourne la consommation énergetique du véhicule en kWh
    else:
        conso_voiture=0
    while transport_commun_ou_non!="non" and transport_commun_ou_non!="oui":
        transport_commun_ou_non=input("\nPrenez vous les transports en commun ? [ oui / non ]: \n-> ")
    if transport_commun_ou_non == "oui":
        transport_commun(transport_commun_ou_non)#appel de la fonction pour le calcul des transports en commun
    
    return conso_voiture

def etiquettte_energie_foyer(conso_energetique_foyer,superficie_foyer):#fonction pour l'étiquette DPE
    print("Consommation énergetique du foyer \n")
    print(f"total du foyer : {conso_energetique_foyer} kWh/an")
    #calcul de la conso au m2 du foyer, arrondissement à l'entier avec round()
    conso_energetique_foyer_m2=round(conso_energetique_foyer/superficie_foyer)
    #liste des classes energetique
    niveau=["A","B","C","D","E","F","G"]
    if conso_energetique_foyer_m2<=50:#suite de condition pour déterminer quelle classe est la consommation énergétique du foyer
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
    for i in range(len(niveau)):#Boucle pour faire l'affichage des classes 
        print(niveau[i], end=" ")
        for j in range(i):#boucle pour l'affichage des pointillés en fonction de la ligne 
            print("-",end="")
        print(">", end="")#affiche du chapeau après les pointillés
        for j in range((len(niveau)+2)-i):#boucle pour laisser un espace après la classe affiché en prévision de la condition suivante
            print(" ",end="")
        if classement == niveau[i]:#condition pour afficher la valeur si elle correspond au niveau
            print(f"< {conso_energetique_foyer_m2} kWh/an/m2")
        else:#saute la ligne pour la prochaine classe si la condition n'est pas valide
            print("")
    print("")#saut de ligne pour affichage plus agréable
            
def etiquettte_impact_foyer(impact_foyer,superficie_foyer):#fonction pour l'étiquette GES
    #affichage
    print("Émission GES du foyer \n")
    print(f"total du foyer : {impact_foyer} kgeqCO2/an")
    #liste des différentes classes
    niveau=["A","B","C","D","E","F","G"]
    #calcul de l'impact au m2 du foyer, arrondissement à l'entier avec round()
    impact_foyer_m2=round(impact_foyer/superficie_foyer)
    if impact_foyer_m2<=5:#suite de condition pour déterminer quelle classe est l'impact de GES du foyer
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
    for i in range(len(niveau)): #Boucle pour faire l'affichage des classes 
        print(niveau[i], end=" ")
        for j in range(i):
            print("-",end="")
        print(">", end="")
        for j in range((len(niveau)+2)-i):#boucle pour laisser un espace après la la classe afficher en prévision de la condition suivante
            print(" ",end="")
        if classement == niveau[i]: #condition pour afficher la valeur si le classement correspond au niveau
            print(f"< {impact_foyer_m2} kgeqCO2/an/m2")
        else: #saute la ligne pour la prochaine classe si la condition n'est pas valide
            print("")
    print("")
            
            
def comparaison_Energie(habitat, transport): #fonction pour afficher le bargraphe
    print("Comparaison habitat et transport\n")
    print("Énergie")
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
    print(f" {pourcentage_transport}% transport\n")
    
            
            
def comparaison_GES(habitat, transport): #cf l284
    print("GES")
    total=habitat+transport
    #calcul du pourcentage de l'habitat et arrondissement à la dizaine puis arrondissement à l'entier pour avoir un integer
    pourcentage_habitat=round(round(habitat*100/total, -1))
    nbr_etoiles_habitat=round(pourcentage_habitat/10)
    #calcul du pourcentage du transport et arrondissement à la dizaine puis arrondissement à l'entier pour avoir un integer
    pourcentage_transport=round(round(transport*100/total, -1))
    nbr_etoiles_transport=round(pourcentage_transport/10)
    for i in range(nbr_etoiles_habitat*2):#affichage du nombre proportionnellement au pourcentage
        print("*",end="")
    print(f" {pourcentage_habitat}% habitat")#affichage du pourcentage 
    for i in range(nbr_etoiles_transport*2):#cf l312
        print("*",end="")
    print(f" {pourcentage_transport}% transport\n")#cf l314
    
def inférieur_supérieur(total,comparateur):
    facteur=total/comparateur #calcul du coefficient pour savoir si c'est inférieur ou supérieur au comparateur (ex : Etat-unis)
    if facteur == 1:#conditions pour savoir si c'est X fois supérieur ou inférieur
        return "égal(e)"
    elif facteur<1 and facteur > 0.5:
        return "inférieur(e)"
    elif facteur<=0.5 and facteur>0.25:
        return "2 fois moins élevé(e)"
    elif facteur<=0.25 and facteur > 0.1:
        return "4 fois moins élevé(e)"
    elif facteur<=0.1:
        return "10 fois moins élevé(e)"
    facteur=round(facteur)
    if facteur == 1:
        return "égal(e)"
    else:
        return f"{facteur} fois plus élevé(e)"

def impact_moyen(total_impact):#fonction pour afficher les différentes comparaisons
    i=0
    print("Mes émissions de gaz à effet de serre sont : \n")
    for pays, valeur in impact_carbone_moyenne.items():
        i+=1
        if inférieur_supérieur(total_impact,valeur)=="égal(e)" or inférieur_supérieur(total_impact,valeur)=="inférieur(e)":
            print(f" - {inférieur_supérieur(total_impact,valeur)} à la moyenne {pays}")
        else:
            print(f" - {inférieur_supérieur(total_impact,valeur)} que la moyenne {pays}")
    print("")
    12
def energie_moyenne(total_energie):
    i=0
    print("Ma consommation d'énergie est : \n")
    for pays, valeur in conso_moyenne_hab.items():
        i+=1
        if inférieur_supérieur(total_energie,valeur)=="égal(e)" or inférieur_supérieur(total_energie,valeur)=="inférieur(e)":
            print(f" - {inférieur_supérieur(total_energie,valeur)} à la moyenne {pays}")
        else:
            print(f" - {inférieur_supérieur(total_energie,valeur)} que la moyenne {pays}")
        
    print("")

def accord_paris(impact_perso):
    accord=2800
    #calcul du facteur par rapport à l'accord de Paris arrondi à l'entier
    facteur = round(impact_perso/accord)
    if facteur <= 1:
        print("Je respecte les accords de Paris visant à maintenir le réchauffement climatique global en dessous de 2°C\n")
    elif facteur > 1:
        print(f"Je dois diviser par {facteur} mon empreinte carbonne pour respecter les accords de Paris visant à maintenir le réchauffement climatique global en dessous de 2°C\n")
#demande de la superficie de la maison (en m2)
superficie_foyer=int(input("\nEntrez la superficie de votre maison : \n-> "))
#nombre de personne dans le foyer
habitant_foyer=int(input("\nEntrez le nombre de personne vivant dans votre foyer : \n-> "))
#création de variables global
impact_foyer=impact_transport=0
#calcul de la consommation energetique du foyer
conso_energetique_foyer=calcul_energie_foyer()
#calcul de la consommation énergétique des véhicules personnels et des transport en commun
conso_voiture=transport()
#calcul de la consommation personnelle d'énergie avec arrondissement à l'entier avec round()
conso_perso=round(conso_energetique_foyer/habitant_foyer)
#calcul impact total avec ajout forfaitaire des biens de consommation(1900kgeqco2/pers/an), alimentation(1800kgeqco2/pers/an) et les services public (1100 kgeqco2/pers/an)
impact_perso=round(impact_transport+(impact_foyer/habitant_foyer)+4800)
#affichaghe des étiquettes DPE et GES du foyer
etiquettte_energie_foyer(conso_energetique_foyer,superficie_foyer)
etiquettte_impact_foyer(impact_foyer, superficie_foyer)

#affichage des émissions de GES du transport et de la consommation énergétique de(s) véhicule(s)
print("Émission gaz à effet de serre du transport :", impact_transport, "kgeqCO2/an\n")
print("Consommation énergétique véhicule(s) :", conso_voiture, "kWh/an\n")

#affichage des bargraphes habitat/transport, énergie puis GES
comparaison_Energie(conso_energetique_foyer,conso_voiture)
comparaison_GES(impact_foyer,impact_transport)

#affichage de l'empreinte individuelle
print("Empreinte individuelle (corrigée forfaitairement pour tenir compte de l'ensemble des produits et services)\n")
print("Energie :", conso_perso, "kWh/personne/an")
print("Carbone : ", impact_perso, "kgeqco2/personne/an\n")


#affichage des comparaisons de moyennes
impact_moyen(impact_perso)
energie_moyenne(conso_perso)

#affichage de la comparaison avec l'accord de paris
accord_paris(impact_perso)