"""**********************************************************************

    Leshgo. The bois are gonna be rich

**********************************************************************"""

import alpaca_trade_api as tradeapi

class brokerAccount:

    def __init__(self, name, apiKey, apiSecretKey, baseURL):

        self.name = name
        self.apiKey = apiKey
        self.apiSecretKey = apiSecretKey
        self.base_url = baseURL


# Authentication and connection details
alpacaAPIKey = 'PKEQEBUVALFPUPCQZXTC'
alpacaAPISecret = 'sKQDrJ2HKWBtez3JZtUSC7sFJKF066e0MIo1F6fK'
alpacaBaseURL = 'https://paper-api.alpaca.markets'

# Instance of the broker account class
alpacaAccount = brokerAccount("Alpaca", alpacaAPIKey, alpacaAPISecret, alpacaBaseURL)

# Instantiate REST API for the Alpaca broker
alpacaAPI = tradeapi.REST(alpacaAccount.apiKey, alpacaAccount.apiSecretKey, 
    alpacaAccount.base_url, api_version='v2')

# obtain account information
alpacaAccountInfo = alpacaAPI.get_account()
print(alpacaAccountInfo)
