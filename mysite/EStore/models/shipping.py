from django.db import models
from .order import Orders
from .transfer import TransferServices


class Shippings(models.Model):
    order = models.ForeignKey(to = Orders, on_delete = models.CASCADE)
    estimate_time = models.IntegerField(default = 1)
    shipper_name =  models.CharField(max_length = 50)
    transfer_company = models.ForeignKey(to = TransferServices, on_delete = models.CASCADE)

