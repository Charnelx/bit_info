from django.contrib.auth.models import User, Group
from .models import Coin, Symbol
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class SymbolSerializer(serializers.HyperlinkedModelSerializer):

    coins = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='coin-detail'
    )

    class Meta:
        model = Symbol
        fields = ('name', 'symbol', 'coins')

class CoinSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.SerializerMethodField('get_symbol_name')
    symb = serializers.SerializerMethodField('get_symbol_symbol')

    def get_symbol_name(self, model):
        return model.symbol.name

    def get_symbol_symbol(self, model):
        return model.symbol.symbol

    class Meta:
        model = Coin
        fields = ('id','name', 'symb', 'market_cap', 'supply', 'volume', 'hour_prc', 'day_prc', 'week_prc', 'update_date')