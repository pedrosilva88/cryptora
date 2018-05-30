# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

CONTRACT_CHOICES = (
    ('6_MONTH', '6 Months'),
    ('1_YEAR', '1 Year'),
    ('2_YEAR', '2 Years'),
    ('UNLIMITED', 'Unlimited'),
)

class Account(models.Model):
    """
    User Account
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value_invested = models.FloatField(u"Value Insvested", blank=False, null=False)
    fee = models.PositiveSmallIntegerField(u"Fee", default=0)
    contract_duration = models.CharField(u"Contract Duration", choices=CONTRACT_CHOICES, default='1_YEAR', max_length=100)
    start_date = models.DateField(u"Start Date", auto_now=True, auto_now_add=False)
    value_current = models.FloatField(u"Current Value")
    updated_at = models.DateTimeField(u"Last Update", auto_now=True)
