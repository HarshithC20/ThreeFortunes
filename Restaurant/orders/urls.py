from django.urls import path, include
from orders.views import menu, place_order, table_entry
urlpatterns = [
    path('menu/', menu, name='Menu View'),
    path('placeOrder', place_order, name='place_order'),
    path('table-entry/', table_entry, name='table_entry'),

]