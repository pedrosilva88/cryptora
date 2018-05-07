# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from coins.models import *

admin.site.register(Coin)
admin.site.register(CoinChange)
