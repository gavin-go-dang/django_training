from django.db import models
# Create your models here.


class Shops(models.Model):
    shop_name = models.CharField(max_length = 50)
    address = models.TextField(max_length = 256)
    phone = models.TextField(max_length = 15)

    def __str__ (self):
        return self.shop_name


class Items(models.Model):
    item_name = models.CharField(max_length = 50)
    price = models.IntegerField(default = 0)
    stocking_status = models.BooleanField(default = False)
    unit = models.CharField(max_length = 50)
    shop = models.ForeignKey(to = Shops, on_delete = models.CASCADE)
    rate = models.FloatField(default = 0)

    def __str__ (self):
        return self.item_name



class Customers(models.Model):
    gender_choice = ((0, 'Female'), (1, 'Male'), (2, 'Other'))
    cust_name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 15)
    address = models.TextField(max_length = 256)
    birthday = models.DateField(null = True, blank = True)
    gender = models.CharField(gender_choice, max_length=10)

    def __str__ (self):
        return self.cust_name



class TransferServices(models.Model):
    company_name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 15)
    address = models.CharField(max_length =100)

    def __str__ (self):
        return self.company_name



class Orders(models.Model):
    customer = models.ForeignKey(to = Customers, on_delete = models.CASCADE)
    date_create = models.DateField(auto_now_add = True)
    discount = models.FloatField(default = 0)




class OrderDetail(models.Model):
    order_id = models.ForeignKey(to = Orders, on_delete = models.CASCADE)
    item_id = models.ForeignKey(to = Items, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.order_id)
    

class Shippings(models.Model):
    order = models.ForeignKey(to = Orders, on_delete = models.CASCADE)
    estimate_time = models.IntegerField(default = 1)
    shipper_name =  models.CharField(max_length = 50)
    transfer_company = models.ForeignKey(to = TransferServices, on_delete = models.CASCADE)