from django.contrib import admin
from .models import Customers, Items, OrderDetail, Orders, TransferServices, Shops, Shippings
from django.db.models.functions import Substr
from .ProcessString import no_accent_vietnamese
# Register your models here.


class FirstLetterFilter(admin.SimpleListFilter):
    title = 'First Letter'
    parameter_name = 'first_letter'


    def lookups(self, request, model_admin):
        queryset = model_admin.get_queryset(request)
        first_letters = queryset.annotate(first_letter=Substr('item_name', 1, 1)).values_list('first_letter', flat=True).distinct()        
        return [(letter, letter.upper()) for letter in first_letters]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(item_name__istartswith=self.value())
        return queryset


class ItemsInline(admin.TabularInline):
    model = Items



@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price', 'stocking_status', 'unit', 'shop', 'rate')
    list_filter = (FirstLetterFilter,)
    search_fields = ('item_name',)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('stocking_status', 'shop', 'rate', 'price')
        return super(ItemsAdmin, self).get_form(request, obj, **kwargs)


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('cust_name', 'address', 'phone', 'gender',)
        

@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'address')
    search_fields = ('address',)


admin.site.register(OrderDetail)
admin.site.register(Orders)
admin.site.register(TransferServices)
admin.site.register(Shippings)


