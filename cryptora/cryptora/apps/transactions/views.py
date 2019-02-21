# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.shortcuts import render
from transactions.portfolio import createPortfolio
from transactions.serializers import PortfolioSerializer
from people.fund import	updateUsersFundValue
from rest_framework import generics

#class PortfolioListCreate(generics.ListCreateAPIView):

    #queryset = createPortfolio().coins
    #serializer_class = PortfolioSerializer
