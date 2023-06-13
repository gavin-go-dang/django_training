from django.db import models

# Create your models here.

class Shops(models.Model):
    shop_id = models.BigAutoField(primary_key = True)
    shop_name = models.TextField(max_length = 50, null = False, blank = False)
    address = models.TextField(max_length = 256, null = False, blank = False)
    phone = models.TextField(max_length = 15, null = False, blank = False)

    def __str__ (self):
        return self.shop_name


class Items(models.Model):
    item_id = models.BigAutoField(primary_key = True)
    item_name = models.TextField(max_length = 256, null = False, blank = False)
    price = models.IntegerField(default = 0, null = False, blank = False)
    stocking_status = models.BooleanField(default = False)
    unit = models.TextField(max_length = 50, null = False, blank = False)
    shop = models.ForeignKey(to = Shops, on_delete = models.CASCADE)
    rate = models.FloatField(default = 0, null = False, blank = False)

    def __str__ (self):
        return self.item_name



class Customers(models.Model):
    gender_choice = ((0, 'Female'), (1, 'Male'), (2, 'Other'))
    cust_id = models.BigAutoField(primary_key = True)
    cust_name = models.TextField(max_length = 50, null = False, blank = False)
    phone = models.TextField(max_length = 15, null = False, blank = False)
    address = models.TextField(max_length = 256, null = False, blank = False)
    birthday = models.DateField(default= '1/1/2000', null = True, blank = True)
    gender = models.CharField(gender_choice, max_length=10)

    def __str__ (self):
        return self.cust_name



class TransferServices(models.Model):
    transfer_id = models.BigAutoField(primary_key = True)
    company_name = models.TextField(max_length = 50, null = False, blank = False)
    phone = models.TextField(max_length = 15, null = False, blank = False)
    address = models.TextField(max_length = 256, null = False, blank = False)

    def __str__ (self):
        return self.company_name



class Orders(models.Model):
    order_id = models.BigAutoField(primary_key = True)
    customer = models.ForeignKey(to = Customers, on_delete = models.CASCADE, null = False, blank = False)
    date_create = models.DateField(auto_now_add = True, null = False, blank = False)
    discount = models.FloatField(default = 0, null = False, blank = False)

    def __str__ (self):
        return self.order_id



class OrderDetail(models.Model):
    detail_id = models.BigAutoField(primary_key = True)
    order_id = models.ForeignKey(to = Orders, on_delete = models.CASCADE, null = False, blank = False)
    item_id = models.ForeignKey(to = Items, on_delete = models.CASCADE, null = False, blank = False)
    quantity = models.IntegerField(default = 0, null = False, blank = False)

    def __str__ (self):
        return self.detail_id

    

class Shippings(models.Model):
    shipping_id = models.BigAutoField(primary_key = True)
    order = models.ForeignKey(to = Orders, on_delete = models.CASCADE, null = False, blank = False)
    estimate_time = models.IntegerField(default = 1, null = False, blank = False)
    shipper_name =  models.TextField(max_length = 256, null = False, blank = False)
    transfer_company = models.ForeignKey(to = TransferServices, on_delete = models.CASCADE)

    def __str__ (self):
        return self.shipping_id