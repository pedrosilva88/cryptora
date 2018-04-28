# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

CONTRACT_CHOICES = (
    ('6_MONTH', '6 Months'),
    ('1_YEAR', '1 Year'),
    ('2_YEAR', '2 Years'),
)

ROLES_CHOICES = (
    ('AD', 'Admin'),
    ('MN', 'Manager'),
    ('FU', 'User of the Fung'),
)


class UserProfile(User):
    role = models.CharField(u'User Profile', unique=True, choices=ROLES_CHOICES, default='FU')


class Account(models.Model):
    """
    Person Account
    """
    user = models.ForeignKey(u"User Profile", UserProfile, on_delete=models.CASCADE)
    value_invested = models.FloatField(u"Value Insvested", blank=False, null=False)
    fee = models.PositiveSmallIntegerField(u"Fee", default=0)
    contract_duration = models.CharField(u"Contract Duration", choices=CONTRACT_CHOICES, default='1_YEAR')
    start_date = models.DateField(u"Start Date", auto_now=True, auto_now_add=False)
    value_current = models.FloatField(u"Current Value")

    updated_at = models.DateTimeField(u"Last Update", auto_now=True)

    class Meta:
        ordering = 'first_name'
