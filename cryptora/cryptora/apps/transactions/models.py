# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from exchanges.models import ExchangeCoin
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction_user", blank=False, null=False)

    price_per_token = models.DecimalField(u'Price per token', blank=False, null=False, max_digits=19, decimal_places=10)
    n_tokens = models.DecimalField(u'tokens', blank=False, null=False, max_digits=20, decimal_places=8)
    fees = models.DecimalField(u'fees', blank=False, null=False, max_digits=5, decimal_places=2)
    date = models.DateTimeField(u'Transaction Date', blank=False, null=False)
    sync = models.BooleanField(u'Synced Transaction', default=False, blank=False, null=False)
    synced_transaction = models.ForeignKey('self', on_delete=models.CASCADE, related_name="transaction_synced", null=True, blank=True)

    class Meta:
        verbose_name = u'Transaction'
        verbose_name_plural = u'Transactions'

    def __str__(self):
        return '[' + self.transaction_method.type + '] ' + str(round(self.n_tokens,2)) + ' ' + self.exchange_coin.coin_change.coin.key
