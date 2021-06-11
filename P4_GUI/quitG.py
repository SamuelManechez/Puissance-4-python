from tkinter import *
import os

def quitGame(wn1):
    wn2 = Tk()
    wn2.title("Exit")

    wn2.config(bg = "red")
    wn2.geometry("600x200")

    label = Label(wn2, text='Est-vous sur de vouloir quitter ?',padx=100, pady=50,bg="red",fg="white",font=("Arial", 12))
    label.place(relx=0.5, rely=0.3, anchor=CENTER)
    
    bo = Button(wn2, text='Oui', padx=20, pady=8, fg="white" ,bg="grey", font=("Arial", 13), command=lambda:[quit()])
    bo.place(relx=0.4, rely=0.6, anchor=CENTER)
    
    bn = Button(wn2, text='Non', padx=20, pady=8, fg="white" ,bg="grey", font=("Arial", 13), command=lambda:[wn2.destroy()])
    bn.place(relx=0.6, rely=0.6, anchor=CENTER)
    
    
    
    wn2.mainloop()