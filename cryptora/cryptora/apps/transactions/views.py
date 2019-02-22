# -*- coding: utf-8 -*-
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework import generics


class TransatctionsListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
