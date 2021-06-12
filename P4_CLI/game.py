from tabulate import tabulate
import os, random, time


def p4():
    #Initialisation et affichage de la grille
    headers = ["0", "1", "2", "3", "4", "5", "6"]
    data = [
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""]]

    print("\n\n               Puissance 4!")
    print("")
    print(tabulate(data,headers, tablefmt='fancy_grid'))

    #Déclaration de variables
    line = 6
    win = False
    irl = True

    while not win:
        
        # Saisit du choix de la case
        if irl == True :
            while True:
                try:
                    print ("\n Joueur = Humain")
                    print("Saisir la valeur de x :")
                    x = int(input())
                    v = 'O'
                    break
                except:
                    print("Ce n'est pas une entrée valide !")
        
        #Jeu aléatoire de l'ordinateur
        elif irl == False:
            print ("\n Joueur = Ordinateur")
            time.sleep(0.5)
            x = random.randint(1, 6)
            v = 'x'       

        # Emplier les symbole
        for i in range(5, 0, -1):
            if data[i][x] == "":
                data[i][x] = v
                """if line != i:
                    compteurLO =0
                    compteurLX =0"""
                line = i
                break
        
        #Clear du terminal
        os.system("clear")
        
        #Affichage du titre
        print("\n\n        Puissance 4!")
        print("")
        
    
        #Affichage de la grille
        print(tabulate(data,headers, tablefmt='fancy_grid'))

        
        #Vérification par colonne
        compteurCO =0
        compteurCX =0
        for j in range(5,0,-1):
            if data[j][x] == "O":
                compteurCO += 1
                compteurCX = 0
                if compteurCO == 4:
                    break
            elif data[j][x] == "x":
                compteurCX+= 1
                compteurCO = 0
                if compteurCX == 4:
                    break
            elif data[j][x] == "":
                compteurCX = 0
                compteurCO = 0
                
            
        #Vérification par ligne    
        compteurLO = 0
        compteurLX = 0 
        for k in range(7):
            if data[line][k] == "O":
                compteurLO += 1
                compteurLX = 0
                if compteurLO == 4:
                    break
            elif data[line][k] == "x":
                compteurLX+= 1
                compteurLO= 0 
                if compteurLX == 4:
                    break
            elif data[line][k] =="" :
                compteurLX = 0
                compteurLO= 0
                
        #Vérification par diagonale
        compteurDO = 0
        compteurDX = 0 
        """for l in range(6):
            compteurDO = 0
            compteurDX = 0  
            for m in range(6,1):
                if data[l][m] == "O" and l==0: 
                    compteurDO += 1
                    compteurDX = 0
                elif data[l+1][m+1] == "O":
                    compteurDO += 1
                    compteurDX = 0
                elif data[l][m] == "x" and l==0: 
                    compteurDO = 0
                    compteurDX += 1
                elif data[l+1][m+1] == "O":
                    compteurDO = 0
                    compteurDX += 1
                elif data[l+1][m+1] == "":
                    compteurDO = 0
                    compteurDX = 0"""
                
                
            #Vérification par diagonale en partant du bas
        compteurDBO = 0
        compteurDBX = 0  
        """for l in range(5,0,-1):
            compteurDBO = 0
            compteurDBX = 0
            for m in range(6,1,-1):
                if data[l][m] == "O" and l==6: 
                    compteurDBO += 1
                    compteurDBX = 0
                elif data[l-1][m-1] == "O":
                    compteurDBO += 1
                    compteurDBX = 0
                elif data[l][m] == "x" and l==6: 
                    compteurDBO = 0
                    compteurDBX += 1
                elif data[l-1][m-1] == "O":
                    compteurDBO = 0
                    compteurDBX += 1
                elif data[l-1][m-1] == "O":
                    compteurDBO = 0
                    compteurDBX = 0"""
                    
        """print(compteurLO)  
        print(compteurLX)
        print(compteurCO)
        print(compteurCX) """       
        #Switch du Joueur à l'ordinateur
        """if irl == True:
            irl = False
        else:
            irl = True   """
        irl = joueur(irl)
        #Condition qui déterminé la victoire
        if compteurLX == 4 or compteurCX==4 or compteurDX==4 or compteurDBX==4:  
            print(defaite())
            win = True
        elif compteurLO==4 or compteurCO==4 or compteurDO==4 or compteurDBO==4:
            print("\n_____________________________________________________________________________")
            print("\n                        Bravo : L'humain à gagné !")
            print("_____________________________________________________________________________\n\n")
            win = True
    
def joueur(irl):
    if irl:
        return False
    else:
        return True

def defaite():
    print("\n_____________________________________________________________________________")
    print("\n                       Dommage : L'ordinateur à gagné !")
    print("_____________________________________________________________________________\n\n")    
