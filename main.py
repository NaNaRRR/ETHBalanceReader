#Needed to make a pop-up window
from tkinter import Tk, Label, Entry, Button, StringVar
import os

from curses import window
from app.WalletData import *
from app.WW import *

#Fix _tkinter.TclError: no display name and no $DISPLAY environment variable error
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0.0.0')

#Start the window
window=Tk()
balance= StringVar()

def get_balance():
    text = txtfld.get()
    if text == 'NaNa':
        text = example_address
    balance.set(f"€{int(get_wallet_data(text))}")
    

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