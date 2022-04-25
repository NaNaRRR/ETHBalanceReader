#Needed to make a pop-up window
from ast import arg
from cProfile import label
from tkinter import *
from curses import window
from app.WalletData import *
from app.WW import *

window=Tk()
balance= StringVar()

def get_balance():
    tekst = txtfld.get()
    if tekst == 'NaNa':
        tekst = example_address
    balance.set(f"€{int(get_wallet_data(tekst))}")
    

window.title('NaNaTechdotcom')
window.geometry("400x300+500+200")

#Creats text to show
lbl=Label(window, text="Read ETH balance from any wallet in €", fg='black', font=("Helvetica", 16))
lbl.place(x=60, y=50) 

lbl2=Label(window,textvariable=balance)
lbl2.place(x=175, y=200)


#Creats space to give the wallet address
txtfld=Entry(window, bd=5)
txtfld.place(x=100, y=100)

#aarde = get_wallet_data(arg)
 #Creats a button to press   
btn=Button(window, text="Get balance", fg='black', command=get_balance)
btn.place(x=160, y=150)

window.mainloop()