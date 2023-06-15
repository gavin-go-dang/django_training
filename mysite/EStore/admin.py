from django.contrib import admin
from .models import Customers, Items, OrderDetail, Orders, TransferServices, Shops, Shippings
# Register your models here.

admin.site.register(Customers)
admin.site.register(Items)
admin.site.register(OrderDetail)
admin.site.register(Orders)
admin.site.register(TransferServices)
admin.site.register(Shops)
admin.site.register(Shippings)