# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from transactions.models import *

admin.site.register(TransactionMethod)
admin.site.register(Transaction)
