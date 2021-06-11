from tkinter import *
from jeu import game


def mainMenu():
    wn = Tk()
    
    #Titre de la fenetre
    wn.title("Puissance 4")

    #Création de la fenetre
    wn.config(bg = "#263D42")
    wn.geometry("1920x1080")

    #Création d'un cadre blanc
    frame = Frame(wn, bg="white",bd=2)
    frame.place(relwidth=0.6,relheight=0.6, relx=0.2, rely=0.2)

    #Message de bienvenue
    label = Label(frame, text='Bienvenue sur le jeu du puissance 4',padx=100, pady=50,bg="white",font=("Arial", 20))
    label.place(relx=0.5, rely=0.3, anchor=CENTER)

    #Entrée pour la saisie du nom d'utilisateur
    usernameLabel = Label(frame, text='Username',bg="white")
    usernameLabel.place(relx=0.5, rely=0.45, anchor=CENTER)
    
    #Récupération du nom d'utilisateur
    userVar = StringVar()
    username = Entry (frame, width=20,textvariable=userVar)
    username.place(relx=0.5, rely=0.5, anchor=CENTER)
  
    #Bouton qui fait appel à jeu.py
    play = Button(frame, text='Jouer', padx=20, pady=8, fg="white" ,bg="#263D42", font=("Arial", 13),command=lambda:[game(wn, username)])
    play.place(relx=0.5, rely=0.7, anchor=CENTER)

    #Initialisation de la fenetre
    wn.mainloop()
    
