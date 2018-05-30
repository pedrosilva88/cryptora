# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class TransactionsConfig(AppConfig):
    name = 'transactions'

    def ready(self):
        import transactions.signals
