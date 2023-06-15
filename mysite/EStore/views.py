
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import View
from django.views.generic import View, TemplateView
from django.db.models import Count,Sum, Max, Min

from .models import Customers, Items, OrderDetail, Orders, Shippings, TransferServices, Shops

class ListUser(TemplateView):
    template_name = 'list_user.html'

    def get_context_data(self, **kwargs):
        cust_list = Customers.objects.all()
        context  = {'cust_list' : cust_list}
        return context


class SumCostPerUser(TemplateView):
    template_name = 'sum_cost_per_cust.html'

    def get_context_data(self, **kwargs):
        transaction_data = OrderDetail.objects.select_related('order_id', 'item_id', 'order_id__customer')

        sum_list = []
        list_customer = [order.order_id.customer for order in transaction_data]


        sum_cost = {key: 0 for key in list_customer}
        for record in transaction_data:
            sum_cost[record.order_id.customer] += record.quantity * record.item_id.price * (1 - record.order_id.discount)
        context = {'sum_cost' : sum_cost}

        return context


class FrequenceSell(TemplateView):
    template_name = 'frequence_sell.html'

    def get_context_data(self, **kwargs):
        order_item = OrderDetail.objects.all().select_related('item_id')
        item_sell_aggregate = order_item.values('item_id__item_name').annotate(count= Count('quantity'))
        print(item_sell_aggregate)
        context = {'fre_item_list' : item_sell_aggregate}
        
        return context


class CheapestItem(TemplateView):
    template_name = 'cheapest_item.html'
    def get_context_data(self):
        min_price = Items.objects.all().aggregate(Min('price'))['price__min']
        cheapest_item = Items.objects.filter(price = min_price)
        context = {'cheapest_item' : cheapest_item, 'cheapest_price':min_price}
        return context


