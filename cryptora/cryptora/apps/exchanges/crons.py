from exchanges.models import Price, ExchangeCoin, Exchange, EXCHANGE_CHOICES
from transactions.models import *
from django.utils import timezone
import gdax
import sys, traceback

def importPrices():
    try:

        exchanges = Exchange.objects.all()
        for exchange in exchanges:
            exchangeCoins = ExchangeCoin.objects.filter(exchange=exchange)
            client = ImportClient(exchange)

            for exchangeCoin in exchangeCoins:
                newPrice = Price()
                price_value = client.getPriceForCoin(exchangeCoin)
                newPrice.exchange_coin = exchangeCoin
                newPrice.value = price_value
                newPrice.date = timezone.now()
                newPrice.save()

    except:
        traceback.print_exc()

class ImportClient():
    exchange = None
    public_client = None

    def __init__(self, exchange):
        self.exchange = exchange
        self.public_client = ImportClient.properClient(self.exchange.name)

    def getPriceForCoin(self, exchangeCoin):
        product_id = exchangeCoin.coin_change.coin.key+'-'+exchangeCoin.coin_change.coin_to_change.key
        return self.public_client.get_product_ticker(product_id=product_id)['price']

    def properClient(name):
        if name == 'GDAX':
            return gdax.PublicClient()

        return None
