# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Coin(models.Model):
    name = models.CharField(u'Coin name', unique=True, blank=False, null=False)
    key = models.CharField(u'Coin key', unique=True, blank=False, null=False)


class CoinChange(models.Model):
    coin = models.ManyToManyField(u'Coin', Coin, on_delete=models.CASCADE)
    coin_to_change = models.ManyToManyField(u'Coin to change', Coin, on_delete=models.CASCADE)
