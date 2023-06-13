from django.urls import path
from .views import ListUser, SumCostPerUser, FrequenceSell, CheapestItem


urlpatterns = [
    path('list-user', ListUser.as_view(), name = 'list-user'),
    path('sum-cost', SumCostPerUser.as_view(), name = 'sum-cost'),
    path('best-seller', FrequenceSell.as_view(), name = 'best-seller'),
    path('cheapest_item', CheapestItem.as_view(), name = 'cheapest_item')
]