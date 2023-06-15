from rest_framework import serializers
from .models.customer import Customers
from django.db import models
from .models.item import Items
from .models.order import Orders
from .models.shop import Shops

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Customers
        fields = ['url', 'cust_name', 'address', 'birthday', 'gender']


class CheapestItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ['item_name', 'price']


class CostPerCustomerSerializer(serializers.HyperlinkedModelSerializer):
    username = models.CharField(max_length=30)
    cost = models.IntegerField(default=0)


