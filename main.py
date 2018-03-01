from btcmarkets import BTCMarkets

import config

api_key = config.api_key
private_key = config.private_key

client = BTCMarkets (api_key, private_key)



#print client.order_detail([1234, 213456])

#print client.order_create('AUD', 'LTC', 100000000, 100000000, 'Bid', 'Limit', '1')

# print client.get_market_tick('ETH','AUD')

withdraw_currency = "ETC"
bithumb_account = "0xfb37daxxxxxxxx"

# print client.trade_history('AUD', 'ETC', 10, 1)

print client.withdrawCrypto(withdraw_currency,int(1000000),bithumb_account)
