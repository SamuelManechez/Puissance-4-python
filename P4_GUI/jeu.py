from tkinter import *
from quitG import *


def game(wn, user):
 
    wn1 = Tk()
    
    #Titre de la fenetre
    wn1.title("Puissance 4")

    #Création de la fenetre
    wn1.config(bg="#263D42")
    wn1.geometry("1920x1080")

    #Création d'un cadre
    c = Canvas(wn1, width =800, height = 800,bd=2)
    c.grid(row=1, columnspan =5, sticky="")
    c.place(relx=0.5, rely=0.5, anchor=CENTER)

    #Affichage du nom d'utilisateur
    label = Label(wn1, text="Username : " + user.get(), padx=20,
                  pady=10, font=("Arial", 16), bg="#263D42", fg="white")
    label.place(relx=0.15, rely=0.05, anchor=CENTER)

    #Génération de l'arrière plan du puissance 4
    c.config(bg="#333333")
    ovals = []
    for y in range(10, 770, 100):
        for x in range(10, 760, 100):
            ovals.append(c.create_oval(x, y, x + 80, y + 80, fill="white"))

    #Bouton pour quitter le jeu
    mQuit = Button(wn1, text='Quitter le jeu', padx=20, pady=8, fg="white",
                      bg="#263D42", font=("Arial", 13), command=lambda: [quitGame(wn1)])
    mQuit.place(relx=0.15, rely=0.95, anchor=CENTER)
    
     
    #Fermeture de la precedante fenetre (menu)
    wn.destroy()
    
    #Initialisation de la fenetre
    wn1.mainloop()
    
        
