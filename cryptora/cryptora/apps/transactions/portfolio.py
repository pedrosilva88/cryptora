# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from transactions.models import Transaction, TransactionMethod
from coins.models import Coin, CoinChange
from exchanges.models import Price, Exchange, ExchangeCoin

def createPortfolio():
    dictionary = getAllTransactionsGroupedByCoinChange()
    portfolio = Portfolio()

    for key, value in dictionary.items():
        coindata = createCoinDataWithTransactions(value)
        portfolio.totalValue += coindata.cashValue
        portfolio.coins.append(coindata)
        print(str(round(coindata.tokens,2)) +' '+ coindata.coin_change.coin.key + ' (' + str(round(coindata.cashValue,2)) + '€)')

    print('Portfolio Value: ' + str(round(portfolio.totalValue,2))+'€')
    return portfolio

def createCoinDataWithTransactions(transactions):
    coindata = CoinData()
    transaction = transactions[0]
    coindata.coin_change = transaction.exchange_coin.coin_change

    for transaction in transactions:
        currentTokens = transaction.n_tokens

        if coindata.coin_change.coin.key != 'EUR':
            currentValue = getTotalCashValueForCoin(
                            getCashValueForCoin(transaction.exchange_coin.coin_change),
                            transaction.n_tokens
                            )
            if coindata.coin_change.coin_to_change.key != 'EUR':
                currentValue = currentValue * getCashValueForCoin(CoinChange.objects.get(coin=transaction.exchange_coin.coin_change.coin_to_change,
                                                                                        coin_to_change__key = 'EUR'))

        else:
            currentValue = transaction.n_tokens

        if transaction.transaction_method.type == 'SELL':
            currentTokens = -currentTokens
            currentValue = -currentValue

        coindata.tokens += currentTokens
        coindata.cashValue += currentValue
    return coindata

def getAllTransactionsGroupedByCoinChange():
    dictionary = {}
    for result in Transaction.objects.all():
        coin_id = result.exchange_coin.coin_change.id
        if coin_id not in dictionary:
            dictionary[coin_id] = [result]
        else:
            dictionary[coin_id].append(result)

    return dictionary

def getTotalCashValueForCoin(coinValue, nTokens):
    return coinValue*nTokens

def getCashValueForCoin(coin_change):
    exchangeCoin = ExchangeCoin.objects.get(coin_change=coin_change)
    price = Price.objects.filter(exchange_coin=exchangeCoin).latest('date')
    return price.value

class Portfolio():
    totalValue = 0
    coins = []


class CoinData():
    coin_change = None
    tokens = 0
    coinChangeValue = 0
    cashValue = 0
