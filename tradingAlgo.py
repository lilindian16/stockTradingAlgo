"""**********************************************************************

    Leshgo. The bois are gonna be rich

**********************************************************************"""

import alpaca_trade_api as tradeapi

class brokerAccount:

    def __init__(self, name, apiKey, apiSecretKey, baseURL, info):

        self.name = name
        self.apiKey = apiKey
        self.apiSecretKey = apiSecretKey
        self.base_url = baseURL
        self.info = info


# Authentication and connection details
alpacaAPIKey = 'PKEQEBUVALFPUPCQZXTC'
alpacaAPISecret = 'sKQDrJ2HKWBtez3JZtUSC7sFJKF066e0MIo1F6fK'
alpacaBaseURL = 'https://paper-api.alpaca.markets'

# Instance of the broker account class
alpacaAccount = brokerAccount("Alpaca", alpacaAPIKey, alpacaAPISecret, alpacaBaseURL, 0)

# Instantiate REST API for the Alpaca broker
alpacaAPI = tradeapi.REST(alpacaAccount.apiKey, alpacaAccount.apiSecretKey, 
    alpacaAccount.base_url, api_version='v2')

# obtain account information
alpacaAccount.info = alpacaAPI.get_account()
print(alpacaAccount.info)


