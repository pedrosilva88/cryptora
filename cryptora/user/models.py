from django.db import models
from django.contrib.auth.models import User

CONTRACT_CHOICES = (
    ('6_MONTH', '6 Months'),
    ('1_YEAR', '1 Year'),
    ('2_YEAR', '2 Years'),
)


class Account(models.Model):

    """
    User Account
    """
    user = models.ForeignKey(u"User", )
    value_invested = models.FloatField(u"Value Insvested")
    fee = models.PositiveSmallIntegerField(u"Fee")
    contract_duration = models.CharField(u"Contract Duration", choices=CONTRACT_CHOICES, default='1_YEAR')
    start_date = models.DateField(u"Start Date", auto_now=True, auto_now_add=False)
    value_current = models.FloatField(u"Current Value")

    updated_at = models.DateTimeField(u"Last Update", auto_now=True)

    class Meta:
        proxy = True
        ordering = ('first_name',)
