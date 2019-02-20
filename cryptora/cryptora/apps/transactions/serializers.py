from rest_framework import serializers
from transactions.portfolio import Portfolio, CoinData

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class CoinDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinData
        fields = '__all__'
