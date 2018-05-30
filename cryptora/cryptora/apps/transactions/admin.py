# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from transactions.models import *

class TransactionAdmin(admin.ModelAdmin):

    list_display = ['ACTION', 'TOKENS', 'PRICE_PER_TOKEN', 'exchange_coin']
    # ordering = ['-date']
    list_filter = ('exchange_coin__exchange', 'exchange_coin__coin_change__coin')

    def ACTION(self, obj):
        return obj.transaction_method.type

    def TOKENS(self, obj):
        return str(round(obj.n_tokens, 2)) + ' ' + obj.exchange_coin.coin_change.coin.key

    def PRICE_PER_TOKEN(self, obj):
        coin = obj.exchange_coin.coin_change.coin.key
        if obj.exchange_coin.coin_change.coin_to_change is not None:
            coin = obj.exchange_coin.coin_change.coin_to_change.key

        return str(round(obj.price_per_token, 2)) + ' ' + coin

admin.site.register(TransactionMethod)
admin.site.register(Transaction, TransactionAdmin)
