from django.db import models

class Customers(models.Model):
    gender_choice = ((0, 'Female'), (1, 'Male'), (2, 'Other'))
    

    cust_name = models.TextField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=256)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(gender_choice, max_length=10)

    def __str__ (self):
        return self.cust_name

    def get_first_name(self):
        return self.cust_name.split()[-1]