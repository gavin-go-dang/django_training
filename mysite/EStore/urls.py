from django.urls import path, include
from .views import ListUser, SumCostPerUser, FrequenceSell, CheapestItem, CustomerViewSet, CheapestItemViewSet, CostPerCustomerViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cheapest-item', CheapestItemViewSet)
# router.register(r'cost-per-customer', CostPerCustomerViewSet)

urlpatterns = [
    path('list-user', ListUser.as_view(), name='list-user'),
    path('sum-cost', SumCostPerUser.as_view(), name='sum-cost'),
    path('best-seller', FrequenceSell.as_view(), name='best-seller'),
    path('cheapest_item', CheapestItem.as_view(), name='cheapest_item'),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('cost_per_cust', CostPerCustomerViewSet.as_view(), name = 'costpercus')
] 