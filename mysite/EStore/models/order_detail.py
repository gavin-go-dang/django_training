from django.db import models
from .order import Orders
from .item import Items
from .customer import Customers

class OrderDetail(models.Model):
    order_id = models.ForeignKey(to = Orders, on_delete = models.CASCADE)
    item_id = models.ForeignKey(to = Items, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
