"""**********************************************************************

    Leshgo. The bois are gonna be rich

**********************************************************************"""

print('Hello World')


import alpaca_trade_api as tradeapi

# authentication and connection details
api_key = 'PKEQEBUVALFPUPCQZXTC'
api_secret = 'sKQDrJ2HKWBtez3JZtUSC7sFJKF066e0MIo1F6fK'
base_url = 'https://paper-api.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# obtain account information
account = api.get_account()
print(account)
