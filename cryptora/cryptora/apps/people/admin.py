# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from people.models import *

admin.site.register(UserProfile)
admin.site.register(Account)