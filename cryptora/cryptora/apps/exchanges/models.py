# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from coins.models import CoinChange

EXCHANGES = (
    ('ICO', 'ICO'),
    ('FUND', 'Fund'),
    ('GDAX', 'GDAX'),
    ('BINANCE', 'Binance'),
    ('BITTREX', 'Bittrex'),
    ('KUCOIN', 'Kucoin')
)

class Exchange(models.Model):
    name = models.CharField(u'Exchange Name', unique=True, blank=False, null=False, max_length=100)
    url = models.CharField(u'Exchange URL', max_length=100)

    def __str__(self):
        return self.name


class ExchangeCoin(models.Model):
    api = models.CharField(u'Exchange Api', unique=True, blank=False, null=False, max_length=100)
    coin_change = models.ForeignKey(CoinChange, on_delete=models.CASCADE, related_name="related_coin_change", blank=False, null=False)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, related_name="related_exchange", blank=False, null=False)

    def __str__(self):
        return '[' +self.exchange.name + '] ' + self.coin_change.__str__()


class Price(models.Model):
    exchange_coin = models.ForeignKey(ExchangeCoin, on_delete=models.CASCADE, related_name="price_exchange_coin", blank=False, null=False)
    value = models.DecimalField(u'Value', blank=False, null=False, max_digits=20, decimal_places=8)
    date = models.DateTimeField(u'Date', blank=False, null=False)

    def __str__(self):
        return self.exchange_coin.coin_change.__str__() + ' > ' + self.value
