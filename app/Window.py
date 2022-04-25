#Needed to make a pop-up window
from tkinter import *
from curses import window

def window():
    window=Tk()
               
    #Creats text to show
    lbl=Label(window, text="Read ETH balance from any wallet in €", fg='black', font=("Helvetica", 16))
    lbl.place(x=60, y=50) 
        
    #Creats space to give the wallet address
    txtfld=Entry(window, text="Enter a wallet address", bd=5)
    txtfld.place(x=100, y=100)

    #Creat an entrypoint for the user's input

    #Creats a button to press   
    btn=Button(window, text="Get balance", fg='black')
    btn.place(x=160, y=150)

    window.title('NaNaTechdotcom')
    window.geometry("400x300+500+200")
    window.mainloop() 