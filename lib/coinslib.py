coins = {
    "KMD":{
        "min_swap": 0.01,
        "api-id": "komodo",
        "activate_with":"electrum",
        "tx_explorer":"https://www.kmdexplorer.io/tx",
        "electrum": [{"url":"electrum1.cipig.net:10001"},
                     {"url":"electrum2.cipig.net:10001"},
                     {"url":"electrum3.cipig.net:10001"}],
        "reserve_balance":1000,
        "premium":1.03,
        "min_swap":0.1,
        "minQty":"0.01000000",
        "maxQty":"90000000.00000000",
        "stepSize":"0.01000000",
        "bot_sell": True,
        "bot_buy": True
    },
    "DEX":{
        "min_swap": 0.1,
        "api-id": "",
        "activate_with":"electrum",
        "tx_explorer":"https://dex.explorer.dexstats.info/tx",
        "electrum": [{"url":"electrum1.cipig.net:10006"},
                     {"url":"electrum2.cipig.net:10006"},
                     {"url":"electrum3.cipig.net:10006"}],
        "bot_sell": False,
        "bot_buy": False
    },
    "VRSC":{        
        "min_swap": 0.1,
        "activate_with":"electrum",
        "tx_explorer":"https://explorer.veruscoin.io/tx",
        "electrum": [{"url":"el0.vrsc.0x03.services:10000"},
                     {"url":"el1.vrsc.0x03.services:10000"},
                     {"url":"electrum1.cipig.net:10021"},
                     {"url":"electrum2.cipig.net:10021"},
                     {"url":"electrum3.cipig.net:10021"}],
        "bot_sell": False,
        "bot_buy": False
    },
    "BTC":{
        "api-id": "bitcoin",
        "activate_with":"electrum",
        "tx_explorer":"https://explorer.bitcoin.com/btc/tx",
        "electrum": [{"url":"electrum1.cipig.net:10000"},
                     {"url":"electrum2.cipig.net:10000"},
                     {"url":"electrum3.cipig.net:10000"}],
        "bot_sell": False,
        "bot_buy": False
    },
    "BCH":{
        "min_swap": 0.01,
        "activate_with":"electrum",
        "tx_explorer":"https://explorer.bitcoin.com/bch/tx",
        "electrum": [{"url":"bch.imaginary.cash:50001"},
                     {"url":"electroncash.dk:50001"},
                     {"url":"electron-cash.dragon.zone:50001"}],
        "reserve_balance":2,
        "premium":1.03,
        "min_swap":0.01,
        "minQty":"0.00001000",
        "maxQty":"900000.00000000",
        "stepSize":"0.00001000",
        "bot_sell": True,
        "bot_buy": True
    },
    "ETH":{
        "api-id": "ethereum",
        "activate_with":"electrum",
        "min_swap": 0.01,
        "tx_explorer":"https://etherscan.io/tx",
        "electrum": ["http://eth1.cipig.net:8555",
                     "http://eth2.cipig.net:8555",
                     "http://eth3.cipig.net:8555"],
        "contract": "0x8500AFc0bc5214728082163326C2FF0C73f4a871",
        "reserve_balance":2,
        "premium":1.03,
        "min_swap":0.01,
        "minQty":"0.001000000",
        "maxQty":"100000.00000000",
        "stepSize":"0.001000000",
        "bot_sell": True,
        "bot_buy": True
    },
    "DASH":{
        "api-id": "dash",
        "min_swap": 0.01,
        "activate_with":"electrum",
        "tx_explorer":"https://explorer.dash.org/tx",
        "electrum":  [{"url":"electrum1.cipig.net:10061"},
                      {"url":"electrum2.cipig.net:10061"},
                      {"url":"electrum3.cipig.net:10061"}],
        "reserve_balance":2,
        "premium":1.03,
        "min_swap":0.01,
        "minQty":"0.00100000",
        "maxQty":"900000.00000000",
        "stepSize":"0.00100000",
        "bot_sell": True,
        "bot_buy": True
    },
    "LTC":{
        "api-id": "litecoin",
        "min_swap": 0.01,
        "activate_with":"electrum",
        "tx_explorer":"https://live.blockcypher.com/ltc/tx",
        "electrum": [{"url":"electrum-ltc.bysh.me:50001"},
                     {"url":"electrum.ltc.xurious.com:50001"},
                     {"url":"ltc.rentonisk.com:50001"},
                     {"url":"backup.electrum-ltc.org:50001"}],
        "reserve_balance":2,
        "premium":1.03,
        "min_swap":0.01,
        "minQty":"0.01000000",
        "maxQty":"100000.00000000",
        "stepSize":"0.01000000",
        "bot_sell": True,
        "bot_buy": True
    },
    "USDC":{
        "min_swap": 0.5,
        "api-id": "usd-coin",
        "activate_with":"electrum",
        "tx_explorer":"https://etherscan.io/tx",
        "electrum": ["http://eth1.cipig.net:8555",
                     "http://eth2.cipig.net:8555",
                     "http://eth3.cipig.net:8555"],
        "contract": "0x8500AFc0bc5214728082163326C2FF0C73f4a871",
        "bot_sell": False,
        "bot_buy": False
    },
    "DOGE":{
        "api-id": "dogecoin",
        "activate_with":"electrum",
        "tx_explorer":"https://live.blockcypher.com/doge/tx",
        "min_swap": 10,
        "electrum": [{"url":"electrum1.cipig.net:10060"},
                     {"url":"electrum2.cipig.net:10060"},
                     {"url":"electrum3.cipig.net:10060"}],
        "reserve_balance":20000,
        "premium":1.0377,
        "min_swap":10,
        "minQty":"1.00000000",
        "maxQty":"90000000.00000000",
        "stepSize":"1.00000000",
        "bot_sell": True,
        "bot_buy": True
    },
    "DGB":{
        "api-id": "digibyte",
        "min_swap": 10,
        "activate_with":"electrum",
        "tx_explorer":"https://digiexplorer.info/tx",
        "electrum": [{"url":"electrum1.cipig.net:10059"},
                     {"url":"electrum2.cipig.net:10059"},
                     {"url":"electrum3.cipig.net:10059"}],
        "bot_sell": False,
        "bot_buy": False
    },
    "QTUM":{
        "min_swap": 4,
        "activate_with":"electrum",
        "tx_explorer":"https://qtum.info/tx",
        "electrum": [{"url":"s1.qtum.info:50001"},
                     {"url":"s2.qtum.info:50001"},
                     {"url":"s3.qtum.info:50001"},
                     {"url":"s4.qtum.info:50001"},
                     {"url":"s5.qtum.info:50001"},
                     {"url":"s6.qtum.info:50001"},
                     {"url":"s7.qtum.info:50001"},
                     {"url":"s8.qtum.info:50001"},
                     {"url":"s9.qtum.info:50001"}
                     ],
        "reserve_balance":50,
        "premium":1.03,
        "min_swap":3.4,
        "minQty":"0.01000000",
        "maxQty":"10000000.00000000",
        "stepSize":"0.01000000",
        "bot_sell": True,
        "bot_buy": True
    },
    "RFOX":{
        "min_swap": 5,
        "activate_with":"electrum",
        "tx_explorer":"https://rfox.explorer.dexstats.info/tx",
        "electrum": [{"url":"electrum1.cipig.net:10034"},
                     {"url":"electrum2.cipig.net:10034"},
                     {"url":"electrum3.cipig.net:10034"}],
        "bot_sell": False,
        "bot_buy": False
    },
    "ZILLA":{
        "min_swap": 5,
        "activate_with":"electrum",
        "tx_explorer":"https://zilla.explorer.dexstats.info/tx",
        "electrum": [{"url":"electrum1.cipig.net:10028"},
                     {"url":"electrum2.cipig.net:10028"},
                     {"url":"electrum3.cipig.net:10028"}],
        "bot_sell": False,
        "bot_buy": False
    },
    "RVN":{
        "min_swap": 5,
        "activate_with":"electrum",
        "tx_explorer":"https://ravencoin.network/tx",
        "electrum": [{"url":"electrum1.cipig.net:10051"},
                     {"url":"electrum2.cipig.net:10051"},
                     {"url":"electrum3.cipig.net:10051"}],
        "reserve_balance":2500,
        "premium":1.03,
        "min_swap":1,
        "minQty":"1.00000000",
        "maxQty":"90000000.00000000",
        "stepSize":"1.00000000",
        "bot_sell": True,
        "bot_buy": True
    },
    "BAT":{
        "min_swap": 0.5,
        "activate_with":"electrum",
        "api-id": "basic-attention-token",
        "tx_explorer":"https://etherscan.io/tx",
        "electrum": ["http://eth1.cipig.net:8555",
                     "http://eth2.cipig.net:8555",
                     "http://eth3.cipig.net:8555"],
        "contract": "0x8500AFc0bc5214728082163326C2FF0C73f4a871",
        "reserve_balance":500,
        "premium":1.03,
        "min_swap":1,
        "minQty":"1.00000000",
        "maxQty":"90000000.00000000",
        "stepSize":"1.00000000",
        "bot_sell": False,
        "bot_buy": False
    },
    "LINK":{
        "min_swap": 0.5,
        "activate_with":"electrum",
        "api-id": "chainlink",
        "tx_explorer":"https://etherscan.io/tx",
        "electrum": ["http://eth1.cipig.net:8555",
                     "http://eth2.cipig.net:8555",
                     "http://eth3.cipig.net:8555"],
        "contract": "0x8500AFc0bc5214728082163326C2FF0C73f4a871",
        "reserve_balance":20,
        "premium":1.03,
        "minQty":"1.00000000",
        "maxQty":"90000000.00000000",
        "stepSize":"1.00000000",
        "bot_sell": False,
        "bot_buy": False
    },
    "LABS":{
        "min_swap": 5,
        "activate_with":"electrum",
        "tx_explorer":"https://labs.explorer.dexstats.info/tx",
        "electrum": [{"url":"electrum1.cipig.net:10019"},
                     {"url":"electrum2.cipig.net:10019"},
                     {"url":"electrum3.cipig.net:10019"}],
        "bot_sell": False,
        "bot_buy": False
    },
    "AXE":{
        "min_swap": 1,
        "api-id": "axe",
        "activate_with":"electrum",
        "tx_explorer":"https://etherscan.io/tx",
        "electrum": [{"url":"electrum1.cipig.net:10057"},
                     {"url":"electrum2.cipig.net:10057"},
                     {"url":"electrum3.cipig.net:10057"}],
        "bot_sell": False,
        "bot_buy": False
    },
    "HUSH":{
        "min_swap": 1,
        "api-id": "hush",
        "activate_with":"electrum",
        "tx_explorer":"https://hush3.komodod.com/t",
        "electrum": [{"url":"electrum1.cipig.net:10064"},
                     {"url":"electrum2.cipig.net:10064"},
                     {"url":"electrum3.cipig.net:10064"}],
        "bot_sell": False,
        "bot_buy": False
    }
}

# Input coins you want to trade here. 
# reserve_balance: excess funds will be sent to your Binance wallet
# premium: value relative to binance market rate to setprices as marketmaker.
# min/max/stepsize need to be set from values from 
# https://api.binance.com/api/v1/exchangeInfo

cointags = []
buy_list = []
sell_list = []
for ticker in coins:
  cointags.append(ticker)
  if coins[ticker]['bot_buy']:
    buy_list.append(ticker)
  if coins[ticker]['bot_sell']:
    sell_list.append(ticker)
trading_list = list(set(buy_list+sell_list))