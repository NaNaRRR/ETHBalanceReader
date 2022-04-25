import PySimpleGUI as sg
import ETHBalanceReader

obj = ETHBalanceReader.ETHtoEUR()

layout = [
[sg.Text("Hello from PySimpleGUI")], 
[sg.Text('', key='balanceText')],
[sg.Input(key='-myinput-')],
[sg.Button("ZOEK")], 
[sg.Button("CLOSE")]]

# Create the window
window = sg.Window("ETH Balance Reader", layout, size=(400, 200))

# Create an event loop
while True:
    event, values = window.read()

    # End program if user closes window or
    # presses the OK button
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break
    if event == "ZOEK":
    	balanceValue = obj.get_wallet_data(values['-myinput-'])
    	window.FindElement('balanceText').Update(balanceValue)

window.close()