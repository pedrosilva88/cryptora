# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Coin(models.Model):
    name = models.CharField(u'Coin name', unique=True, blank=False, null=False, max_length=100)
    key = models.CharField(u'Coin key', unique=True, blank=False, null=False, max_length=100)


class CoinChange(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="Coin")
    coin_to_change = models.ForeignKey(Coin, on_delete=models.CASCADE)
