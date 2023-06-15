from django.db import models

class Shops(models.Model):
    shop_name = models.CharField(max_length=50 ,unique=True)
    address = models.TextField(max_length=256)
    phone = models.CharField(max_length=15)

    def __str__ (self):
        return self.shop_name



