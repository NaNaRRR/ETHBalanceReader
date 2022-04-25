#web3 library for Python
from web3 import Web3

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

#Ables us to read json format
import json

#Import API key and Infura URL
import WW

class ETHtoEUR():
    def get_wallet_data(self, arg):
            #Connection to web3 to interact with the blockchain
            infura_url = WW.Infura
            web3 = Web3(Web3.HTTPProvider(infura_url))
            connection = web3.isConnected()
            
            if connection:
                #Reading the ETH balance of the wallet
                if arg == 'alex':
                    address = WW.addressAlex
                else:
                    address = arg
                balance = web3.eth.getBalance(address) 
                ETH_balance = web3.fromWei(balance, "ether")

                #Address to get the data using the coinmarketcap API
                url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
                parameters = {
                'start':'2',
                'limit':'2',
                'convert':'EUR'
                }
                headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': WW.APIkey,
                }

                session = Session()
                session.headers.update(headers)

                try:
                    #Ask the API for the data
                    response = session.get(url, params=parameters)
                    data = json.loads(response.text)
    
                    #Searching through the results for the ETH price
                    x = int(data['data'][0]['quote']['EUR']['price'])
    
                    #The current value of your wallet is your ETH balance multiplied by the current ETH price
                    #tekst = ("This wallet is currently holding €",ETH_balance * x, " worth of ETH")
                    tekst = ETH_balance * x
                    return tekst
                
                #In the event of a connection error
                except (ConnectionError, Timeout, TooManyRedirects) as e:
                    print(e)
            
            #In the event that you are not connected to web3
            else:
                print("Not connected to web3")

func = ETHtoEUR()