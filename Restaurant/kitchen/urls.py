from django.urls import path, include
from kitchen.views import kitchen, kitchen_orders, kitchen_view
urlpatterns = [
    path('', kitchen_view, name='Kitchen View'),
    path('kitchenOrders/', kitchen_orders, name='kitchen_orders')

]