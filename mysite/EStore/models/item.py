from django.db import models
from .shop import Shops

class Items(models.Model):
    item_name = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    stocking_status = models.BooleanField(default=False)
    unit = models.CharField(max_length=50)
    shop = models.ForeignKey(to=Shops, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)

    def __str__ (self):
        return self.item_name