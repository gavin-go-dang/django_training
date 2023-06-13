
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import View
from django.views.generic import View, TemplateView
from django.db.models import Count,Sum, Max, Min
from .models import Customers, Orders, OrderDetail, Shippings, Shops, TransferServices, Items
# Create your views here.


class ListUser(TemplateView):
    def get(self, request):
        cust_list = Customers.objects.all()
        context  = {'cust_list' : cust_list}
        return render(request, 'list_user.html', context)


class SumCostPerUser(TemplateView):
    def get(self, request):
        transaction_data = OrderDetail.objects.select_related('order_id').select_related('item_id').select_related('order_id__customer')

        sum_list = []
        list_customer = [str(order.order_id.customer) for order in transaction_data]

 
        sum_cost = {key: 0 for key in list_customer}
        for record in transaction_data:
            sum_cost[record.order_id.customer.cust_name] += record.quantity * record.item_id.price * (1 - record.order_id.discount)
        context = {'sum_cost' : sum_cost}
        return render(request, 'sum_cost_per_cust.html', context)


class FrequenceSell(TemplateView):
    def get(self, request):
        order_item = OrderDetail.objects.all().select_related('item_id')
        item_sell_aggregate = order_item.values('item_id__item_name').annotate(count= Count('quantity'))
        print(item_sell_aggregate)
        context = {'fre_item_list' : item_sell_aggregate}
        
        return render(request, 'frequence_sell.html', context)



class CheapestItem(TemplateView):
    def get(self, request):
        min_price = Items.objects.all().aggregate(Min('price'))['price__min']
        cheapest_item = Items.objects.filter(price = min_price)
        context = {'cheapest_item' : cheapest_item, 'cheapest_price':min_price}

        return render(request, 'cheapest_item.html', context)

