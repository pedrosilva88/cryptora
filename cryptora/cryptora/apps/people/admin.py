# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from people.models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'value_invested', 'value_current', 'contract_duration', 'start_date']
    ordering = ['-start_date']

admin.site.register(Account, AccountAdmin)
