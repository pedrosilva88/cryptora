# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from exchanges.models import ExchangeCoin, Exchange, Price
from people.models import Account
from transactions.models import Transaction, TransactionMethod
from coins.models import Coin
from people.fund import updateUsersFundValue
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

@receiver(pre_save, sender=Account)
def signalForPreSave(sender, instance, **kwargs):
    try:
        Account.objects.get(pk=instance.pk)
    except Account.DoesNotExist:
        updateUsersFundValue()

@receiver(post_save, sender=Transaction)
@receiver(post_save, sender=Account)
def signalForPostSave(sender, instance, created, **kwargs):
    if created:
        postObjectCreated(sender, instance, created, **kwargs)
    else:
        postObjectUpdated(sender, instance, created, **kwargs)


def postObjectCreated(sender, instance, created, **kwargs):
    if sender == Account:
        createTransaction(  instance,
                            TransactionMethod.objects.get(type='BUY'),
                            ExchangeCoin.objects.get(exchange=Exchange.objects.get(name='Fund')),
                            instance.value_invested,
                            1)
        updateUsersFundValue()
    elif sender == Transaction and instance.sync == True and instance.synced_transaction == None and instance.exchange_coin.exchange.name != 'Fund':
        method = TransactionMethod.objects.get(type='BUY') if instance.transaction_method.type == 'SELL' else TransactionMethod.objects.get(type='SELL')
        exchangeCoin = None
        pricePerToken = None

        if instance.exchange_coin.coin_change.coin_to_change.key == 'EUR':
            exchangeCoin = ExchangeCoin.objects.get( coin_change__coin = instance.exchange_coin.coin_change.coin_to_change,
                                                    coin_change__coin_to_change = None)
            pricePerToken = 1
        else:
            exchangeCoin = ExchangeCoin.objects.get(coin_change__coin = instance.exchange_coin.coin_change.coin_to_change,
                                                    coin_change__coin_to_change = (Coin.objects.get(key='EUR')))
            pricePerToken = Price.objects.filter(exchange_coin=exchangeCoin).earliest('date').value

        valueInvested = instance.n_tokens * instance.price_per_token
        instance.synced_transaction = createTransaction(instance, method, exchangeCoin, valueInvested, pricePerToken)
        instance.save()
        updateUsersFundValue()

def postObjectUpdated(sender, instance, created, **kwargs):
    if sender == Transaction and instance.synced_transaction != None and instance.exchange_coin.exchange.name != 'Fund':
        syncedTransaction = instance.synced_transaction
        if syncedTransaction.exchange_coin.coin_change.coin.key == 'EUR' or syncedTransaction.exchange_coin.coin_change.coin_to_change.key == 'EUR':
            syncedTransaction.n_tokens = instance.n_tokens * instance.price_per_token
        else:
            syncedTransaction.n_tokens = syncedTransaction.n_tokens / instance.price_per_token
        syncedTransaction.save()

def createTransaction(instance, methodType, exchangeCoin, valueInvested, pricePerToken):
    transaction = Transaction()
    transaction.transaction_method = methodType
    transaction.exchange_coin = exchangeCoin
    transaction.user = User.objects.get(username='pedrosilva')
    transaction.n_tokens = valueInvested
    transaction.price_per_token = pricePerToken
    transaction.fees = 0
    transaction.date = timezone.now()
    transaction.synced_transaction = None
    transaction.save()

    return transaction
