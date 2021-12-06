import pandas as pd
import sqlalchemy
from binance import Client
from binance import BinanceSocketManager

"""Api key and Api Secret Key for Binance"""
api_key = "thisisapikey"
api_secret_key = "thisisapisecretkey"

client = Client(api_key, api_secret_key)
bsm = BinanceSocketManager(client)


socket = bsm.trade_socket("BTCUSDT")


async def get_response():
    await socket.__aenter__()
    result = await socket.recv()
    print("response: ", result())
