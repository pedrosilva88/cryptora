from exchanges.models import Price, ExchangeCoin, Exchange
from transactions.models import *
from django.utils import timezone
import gdax
from binance.client import Client as BinanceClient
from kucoin.client import Client as KucoinClient
import sys, traceback

def importPrices():
    try:
        exchanges = Exchange.objects.all()
        for exchange in exchanges:
            if exchange.name == 'Fund' or exchange.name == 'ICO':
                continue

            exchangeCoins = ExchangeCoin.objects.filter(exchange=exchange)
            client = ImportClient(exchange)

            for exchangeCoin in exchangeCoins:
                newPrice = Price()
                price_value = client.getPriceForCoin(exchangeCoin)
                
                if price_value != None:
                    newPrice.exchange_coin = exchangeCoin
                    newPrice.value = price_value
                    newPrice.date = timezone.now()
                    newPrice.save()
                else:
                    print(str(exchangeCoin) + ' import failed! ')

    except:
        traceback.print_exc()

class ImportClient():
    exchange = None

    def __init__(self, exchange):
        self.exchange = exchange

    def getPriceForCoin(self, exchangeCoin):
        return ImportClient.getPriceForCoinWithProperClient(self.exchange.name, exchangeCoin)

    def getPriceForCoinWithProperClient(name, exchangeCoin):
        try:
            if name == 'Coinbase Pro':
                symbol = exchangeCoin.coin_change.coin.key+'-'+exchangeCoin.coin_change.coin_to_change.key
                return gdax.PublicClient().get_product_ticker(product_id=symbol)['price']
            elif name == 'Binance':
                symbol = exchangeCoin.coin_change.coin.key+exchangeCoin.coin_change.coin_to_change.key
                return BinanceClient("","").get_symbol_ticker(symbol=symbol)['price']
            elif name == 'Kucoin':
                symbol = exchangeCoin.coin_change.coin.key+'-'+exchangeCoin.coin_change.coin_to_change.key
                return KucoinClient("","").get_tick(symbol=symbol)['lastDealPrice']

            return None
        except:
            return None
