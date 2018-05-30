# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from exchanges.models import *

class PriceAdmin(admin.ModelAdmin):

    list_display = ['Coin', 'value', 'date', 'Exchange']
    ordering = ['-date']
    list_filter = ('exchange_coin__exchange', 'exchange_coin__coin_change')

    def Exchange(self, obj):
        return obj.exchange_coin.exchange.name

    def Coin(self, obj):
        return obj.exchange_coin.coin_change

admin.site.register(Exchange)
admin.site.register(ExchangeCoin)
admin.site.register(Price, PriceAdmin)
