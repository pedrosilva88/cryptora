# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import *
from django.db.models import Sum
from transactions.portfolio import createPortfolio, Portfolio, CoinData
from people.models import Account

def updateUsersFundValue():    
    portfolio = createPortfolio()
    totalValue = Account.objects.all().aggregate(Sum('value_current')).get('value_current__sum')

    for account in Account.objects.all():
        percentage = (account.value_current / totalValue)
        value = portfolio.totalValue * Decimal(percentage)
        account.value_current = value
        account.save()
