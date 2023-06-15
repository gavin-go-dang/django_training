from django.db import models

class TransferServices(models.Model):
    company_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=256)

    def __str__ (self):
        return self.company_name

   

