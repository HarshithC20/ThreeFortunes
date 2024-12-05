from django.urls import path, include
from .views import kitchen

urlpatterns = [
    path('kitchen/', kitchen, name='Kitchen View')
]
