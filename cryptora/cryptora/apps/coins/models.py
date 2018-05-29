# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Coin(models.Model):
    name = models.CharField(u'Coin name', unique=True, blank=False, null=False, max_length=100)
    key = models.CharField(u'Coin key', unique=True, blank=False, null=False, max_length=100)

    class Meta:
        verbose_name = u'Coin'
        verbose_name_plural = u'Coins'

    def __str__(self):
        return self.name + u' (' + self.key + u')'


class CoinChange(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="coinchange_coin", blank=False, null=False)
    coin_to_change = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="coinchange_coin_to_change", blank=False, null=False)

    def __str__(self):
        return self.coin.key + u'/' + self.coin_to_change.key
