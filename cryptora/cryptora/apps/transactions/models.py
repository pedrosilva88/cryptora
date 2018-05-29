# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from exchanges.models import ExchangeCoin
from people.models import UserProfile

TRANSACTION_CHOICES = (
    ('BUY', 'Buy'),
    ('SELL', 'Sell')
)

class TransactionMethod(models.Model):
    type = models.CharField(u'Transaction type', choices=TRANSACTION_CHOICES, default='BUY', max_length=20)

    def __str__(self):
        return self.type


class Transaction(models.Model):

    transaction_method = models.ForeignKey(TransactionMethod, on_delete=models.CASCADE, related_name="transaction_transaction_method", blank=False, null=False)
    exchange_coin = models.ForeignKey(ExchangeCoin, on_delete=models.CASCADE, related_name="transaction_exchange_coin", blank=False, null=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="transaction_price", blank=False, null=False)

    price_per_token = models.CharField(u'Price per token', max_length=20)
    n_tokens = models.CharField(u'Tokens', max_length=20)
    fees = models.CharField(u'fees', max_length=20)
    date = models.DateTimeField(u'Transaction Date', blank=False, null=False)

    class Meta:
        verbose_name = u'Transaction'
        verbose_name_plural = u'Transactions'

    def __str__(self):
        return self.transaction_method.type + ' --> ' + self.exchange_coin.coin_change.coin.name
