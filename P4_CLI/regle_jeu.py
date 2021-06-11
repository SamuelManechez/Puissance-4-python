from tabulate import tabulate
import os

def regle_jeu():
    #Règles du jeu
    print("\n\n                            Jeu du Puissance 4")
    print("\n_____________________________________________________________________________")
    print("\n                               Régles du jeu")
    print("_____________________________________________________________________________")

    print("\n  **Saisir un entier entre 0 et 6 qui correspond à une position de colonne")
    print("  **La vérification est uniquement horizontale et verticale")
    print("  **Il faut aligner 4 symboles")
    print("  **Appuyez sur [ctrl] + [z] pour arrêter le programme")


    print("\n Symbole des joueurs :")

    head = ["Type","Symbole"]
    datas = [["Humain","O"],
            ["Ordinateur","x"]]
    print(tabulate(datas,head, tablefmt='fancy_grid'))
    """print("Symbole de l'humain = O")
    print("Symbole de l'ordinateur = x\n\n")"""

    input("Appuyez sur la touche Entrée pour commencer...")
    os.system("clear")