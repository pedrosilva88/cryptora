# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from coins.models import CoinChange


class Exchange(models.Model):
    name = models.CharField(u'Exchange Name', unique=True, blank=False, null=False, max_length=100)
    url = models.CharField(u'Exchange URL', unique=True, blank=False, null=False, max_length=100)
    api = models.CharField(u'Exchange Api', unique=True, blank=False, null=False, max_length=100)
    coin_change = models.ManyToManyField(CoinChange)
