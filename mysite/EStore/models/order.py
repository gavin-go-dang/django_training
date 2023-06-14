from django.db import models
from .customer import Customers

class Orders(models.Model):
    customer = models.ForeignKey(to = Customers, on_delete = models.CASCADE)
    date_create = models.DateField(auto_now_add = True)
    discount = models.FloatField(default = 0)




